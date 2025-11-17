# legacy_system.py
from services.crypto_service import decrypt_data, encrypt_data
from services.xml_service import parse_xml_to_dict

# Simula um "banco de dados" simples
SIMULATED_DATABASE = {}

def process_client_registration_xml(xml_request: str) -> str:
    # 1. Receber XML e Descriptografar dados sensíveis [cite: 17]
    data = parse_xml_to_dict(xml_request)
    
    # Supondo que o CPF venha criptografado
    encrypted_cpf = data['Cliente']['CPF_Criptografado']
    decrypted_cpf = decrypt_data(encrypted_cpf) # Dados criptografados: CPF 
    
    # 2. Simulação de processamento
    client_id = f"CLI-{len(SIMULATED_DATABASE) + 1}"
    SIMULATED_DATABASE[client_id] = {
        'nome': data['Cliente']['Nome'],
        'email': data['Cliente']['Email'],
        'cpf': decrypted_cpf # Armazena o CPF descriptografado no "banco"
    }

    # 3. Retorna XML de sucesso
    return f"""
    <RespostaLegado>
        <Status>SUCESSO</Status>
        <Mensagem>Cliente cadastrado com sucesso!</Mensagem>
        <ID_Confirmacao>{client_id}</ID_Confirmacao>
    </RespostaLegado>
    """

def get_client_data_xml(xml_request: str) -> str:
    # 1. Receber XML e extrair ID
    data = parse_xml_to_dict(xml_request)
    client_id = data['ConsultaCliente']['ID']
    
    # 2. Simulação de busca
    client_data = SIMULATED_DATABASE.get(client_id)
    
    if client_data:
        # 3. Montar XML de resposta com dados sensíveis criptografados [cite: 39]
        encrypted_cpf_response = encrypt_data(client_data['cpf']) # Criptografa o CPF novamente
        
        return f"""
        <RespostaLegado>
            <Status>OK</Status>
            <ID_Cliente>{client_id}</ID_Cliente>
            <Nome>{client_data['nome']}</Nome>
            <Email>{client_data['email']}</Email>
            <CPF_Criptografado>{encrypted_cpf_response}</CPF_Criptografado> 
        </RespostaLegado>
        """
    else:
        return f"""
        <RespostaLegado>
            <Status>ERRO</Status>
            <Mensagem>Cliente não encontrado.</Mensagem>
        </RespostaLegado>
        """