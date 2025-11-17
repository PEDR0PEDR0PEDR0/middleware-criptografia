# app.py

from flask import Flask, request, jsonify
# ATENÇÃO: Importação corrigida para incluir ambas as funções crypto!
from config import API_TOKEN_VALID 
from services.crypto_service import encrypt_data, decrypt_data # AGORA IMPORTA O decrypt_data
import xml.etree.ElementTree as ET 

app = Flask(__name__)

# Simulação do Sistema Legado
def send_to_legacy_system(xml_data: str):
    """Simula o envio de XML para o sistema legado."""
    print(f"\n--- Enviando ao Sistema Legado (XML) ---\n{xml_data}\n---------------------------------------\n")
    # Retorna uma resposta de sucesso simulada
    return True

# Middleware de Autenticação (Executado antes de todas as rotas)
@app.before_request
def check_auth():
    """Verifica se o token de API no cabeçalho 'Authorization' é válido."""
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({"erro": "Autenticação necessária. Cabeçalho 'Authorization' ausente."}), 401

    try:
        # Extrai o token, considerando o formato "Bearer <token>" ou apenas o token
        token = auth_header.split(' ')[1] if ' ' in auth_header else auth_header
    except IndexError:
         token = auth_header

    if token != API_TOKEN_VALID:
        return jsonify({"erro": "Token de API inválido"}), 401

# --------------------------------------------------------------------------------
# ROTA DE CADASTRO (POST)
# --------------------------------------------------------------------------------
@app.route('/cliente', methods=['POST'])
def cadastrar_cliente():
    """Endpoint para cadastrar um novo cliente."""
    client_data = request.get_json()

    # 1. Validar dados
    if not client_data or 'nome' not in client_data or 'cpf' not in client_data:
        return jsonify({"erro": "Dados inválidos. 'nome' e 'cpf' são obrigatórios."}), 400

    # 2. Criptografar dados sensíveis (Ex: CPF)
    cpf_criptografado = encrypt_data(client_data['cpf'])
    sensitive_data = {'CPF_Criptografado': cpf_criptografado}

    # 3. Montar o XML para o legado
    xml_body_dict = {
        'Nome': client_data['nome'],
        'Email': client_data.get('email', ''),
        'CPF_Criptografado': cpf_criptografado
    }

    # Conversão do dicionário para XML
    root = ET.Element("CadastroCliente")
    for key, value in xml_body_dict.items():
        ET.SubElement(root, key).text = value
    
    xml_string = ET.tostring(root, encoding='utf-8').decode()

    # 4. Enviar ao sistema legado (Simulado)
    if send_to_legacy_system(xml_string):
        return jsonify({
            "mensagem": "Cliente cadastrado com sucesso (via Middleware).",
            "dados_enviados_criptografados": sensitive_data
        }), 201
    else:
        return jsonify({"erro": "Falha ao comunicar com o sistema legado."}), 500

# --------------------------------------------------------------------------------
# ROTA DE CONSULTA (GET) - NOVO ENDPOINT
# --------------------------------------------------------------------------------
@app.route('/cliente/<cpf_criptografado>', methods=['GET'])
def consultar_cliente(cpf_criptografado):
    """Endpoint para consultar um cliente usando o CPF criptografado."""
    
    # 1. Montar o XML de requisição para o legado
    xml_request = f"""
<ConsultaCliente>
    <CPF_Criptografado>{cpf_criptografado}</CPF_Criptografado>
</ConsultaCliente>
"""
    # 2. Simular envio da requisição XML ao sistema legado
    print(f"\n--- Enviando Consulta ao Legado (XML Request) ---\n{xml_request}\n----------------------------------------------\n")

    # 3. Simular a resposta XML do sistema legado.
    simulated_legacy_response_xml = f"""
<RespostaCliente>
    <Nome>Pedro Consultador</Nome>
    <Email>pedro.consultor@legado.com</Email>
    <CPF_Criptografado>{cpf_criptografado}</CPF_Criptografado>
    <Status>Ativo</Status>
</RespostaCliente>
"""
    
    # 4. Descriptografar o dado sensível (CPF)
    try:
        cpf_descriptografado = decrypt_data(cpf_criptografado)
    except Exception as e:
        # Se a descriptografia falhar, retorna um erro
        return jsonify({
            "erro": "Falha na descriptografia. Chave inválida ou dado corrompido.", 
            "detalhe": str(e)
        }), 500

    # 5. Converter a resposta XML (simulada) para JSON e retornar ao cliente externo
    return jsonify({
        "mensagem": "Consulta de cliente realizada com sucesso.",
        "nome": "Pedro Consultador", 
        "email": "pedro.consultor@legado.com",
        "status": "Ativo",
        # O dado sensível é descriptografado APENAS no Middleware
        "cpf_descriptografado": cpf_descriptografado 
    }), 200

if __name__ == '__main__':
    app.run(debug=True)