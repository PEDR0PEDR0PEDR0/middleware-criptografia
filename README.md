📘 Middleware Web Service – Criptografia + XML + REST

Este projeto implementa um Middleware Web Service que funciona como intermediário entre:

Clientes externos (aplicações web/mobile usando JSON via REST)

Sistema legado interno (processa apenas XML)

O objetivo é garantir segurança, tradução de formatos e isolamento arquitetural, conforme os requisitos do exercício baseado nos capítulos 9 e 13 do livro Sistemas Distribuídos — Colouris.

🚀 1. Funcionalidades do Middleware

✔ Expor uma API REST para clientes externos
✔ Converter JSON → XML e XML → JSON
✔ Criptografar dados sensíveis (CPF) usando AES-256 CBC
✔ Autenticação por Token no cabeçalho
✔ Enviar e consumir XML simulando o sistema legado
✔ Devolver respostas organizadas em JSON

🧱 2. Arquitetura Geral

O projeto segue uma arquitetura em três camadas:

1. Cliente Externo

Simulado via Postman/Insomnia usando JSON.

2. Middleware (API REST) – este projeto

Recebe JSON

Valida os dados

Converte para XML

Criptografa informações sensíveis

Envia para o legado

Recebe XML criptografado

Descriptografa

Retorna JSON ao cliente

3. Sistema Legado Simulado

Feito em legacy_system.py, que representa o processamento interno.

🛠️ 3. Tecnologias Utilizadas
Tecnologia	Uso
Python 3.x	Linguagem principal
Flask	API REST
PyCryptodome	Criptografia AES-256
XML (ElementTree)	Manipulação de XML
Postman/Insomnia	Testes de API
⚙️ 4. Instalação e Execução

Certifique-se de que possui Python 3 instalado.

✔ 4.1 Instale as dependências
pip install -r requirements.txt

✔ 4.2 Execute o servidor
python app.py


A API ficará disponível em:

http://127.0.0.1:5000/

🔐 5. Segurança e Criptografia
✔ Algoritmo

AES-256

Modo CBC

IV aleatório por operação

✔ Chave de criptografia

Definida em config.py

Armazenada em Base64

Convertida para 32 bytes (requisito do AES-256)

✔ Dados criptografados

Apenas CPF

Aparece como Base64 no XML

✔ Autenticação

A API exige o header:

Authorization: my-secret-api-token-12345

✔ HTTPS

Em produção, o Middleware deve ficar atrás de um Nginx/Apache fazendo o TLS termination.
A explicação está documentada no README conforme o requisito do exercício.

🌐 6. Endpoints da API
🔹 POST /cliente – Cadastro
URL
POST http://127.0.0.1:5000/cliente

Headers
Authorization: my-secret-api-token-12345
Content-Type: application/json

Body
{
  "nome": "João Silva",
  "cpf": "12345678900",
  "email": "joao@exemplo.com"
}

🔹 GET /cliente/{cpf_criptografado} – Consulta
URL
GET http://127.0.0.1:5000/cliente/<cpf_criptografado>

Header
Authorization: my-secret-api-token-12345

🧾 7. Estruturas XML Utilizadas
✔ 7.1 XML – Requisição de Cadastro
<CadastroCliente>
    <Nome>João Silva</Nome>
    <Email>joao.silva@exemplo.com</Email>
    <CPF_Criptografado>hx5IIrLVq42KbXWDcPWvLCqt8nvDeuLRKKlnvbrtQ3o=</CPF_Criptografado>
</CadastroCliente>

✔ 7.2 XML – Resposta de Consulta

(Exemplo gerado pelo legado)

<ClienteInfo>
    <Nome>João Silva</Nome>
    <Email>joao.silva@exemplo.com</Email>
    <CPF>12345678900</CPF>
</ClienteInfo>


Arquivos incluídos no repositório:

requisicao_cadastro.xml

resposta_consulta.xml

📦 8. Coleção Postman/Insomnia

Incluída no repositório:

Middleware_Criptografia_Colecao.json


Atende ao requisito do exercício:

Contém a requisição de cadastro

Contém a requisição de consulta

Exibe as respostas da API

📁 9. Estrutura do Projeto
middleware-criptografia/
│   app.py
│   config.py
│   legacy_system.py
│   requirements.txt
│   README.md
│   requisicao_cadastro.xml
│   resposta_consulta.xml
│   Middleware_Criptografia_Colecao.json
│
├── services/
│     ├── crypto_service.py
│     └── xml_service.py

🧪 10. Testes

Use ferramentas como:

Postman

Insomnia

cURL

A coleção exportada facilita a reprodução dos testes.

📚 11. Referências

Sistemas Distribuídos — Colouris, capítulos 9 e 13

Documentação Flask

Documentação PyCryptodome

✔️ 12. Conclusão

Este Middleware implementa todos os requisitos do exercício:

API REST funcional

Conversão JSON ↔ XML

Criptografia AES-256

Autenticação por Token

Simulação de sistema legado

Dois exemplos XML

Exportação Postman