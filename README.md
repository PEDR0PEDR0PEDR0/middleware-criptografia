Middleware Web Service – Criptografia AES + XML + REST


Este projeto implementa um Middleware Web Service que funciona como intermediário entre:

Clientes externos (JSON/REST)

Sistema legado interno (XML)

O middleware:

Converte JSON para XML e XML para JSON,

Aplica criptografia AES-256,

Implementa autenticação por token,

Simula comunicação com um sistema legado.

O projeto cumpre todos os requisitos definidos pelo exercício baseado nos capítulos 9 e 13 do livro "Sistemas Distribuídos – Colouris".

2. Arquitetura do Sistema
Cliente Externo (JSON/REST)
            ↓
   Middleware Flask
 → Valida requisição
 → Converte JSON → XML
 → Criptografa CPF
 → Envia ao Sistema Legado
 → Recebe XML criptografado
 → Descriptografa
 → Retorna JSON
            ↓
Sistema Legado Simulado (XML)

3. Tecnologias Utilizadas
Tecnologia	Descrição
Python 3.x	Linguagem principal
Flask	API REST
PyCryptodome	Criptografia AES-256
XML (ElementTree)	Manipulação de XML
Postman / Insomnia	Testes de API
4. Como Executar

Instale as dependências:

pip install -r requirements.txt


Execute o servidor:

python app.py


A API estará disponível em:

http://127.0.0.1:5000/

5. Segurança e Criptografia

Algoritmo utilizado:

AES-256, modo CBC

IV gerado automaticamente

Chave:

Definida em config.py

Armazenada em Base64

Convertida para 32 bytes conforme especificação do AES-256

Dados criptografados:

Campo CPF

Autenticação da API (obrigatória):

Authorization: my-secret-api-token-12345


HTTPS:
Em produção, recomenda-se que o middleware opere atrás de um servidor como NGINX ou Apache, que realiza o TLS termination.

6. Endpoints da API
POST /cliente

URL:

http://127.0.0.1:5000/cliente


Body:

{
  "nome": "João Silva",
  "cpf": "12345678900",
  "email": "joao@exemplo.com"
}

GET /cliente/{cpf_criptografado}

Exemplo:

http://127.0.0.1:5000/cliente/hx5IIrLVq42KbXWDcPWvLCqt8nvDeuLRKKlnvbrtQ3o=

7. Estruturas XML
XML – Requisição de Cadastro
<CadastroCliente>
    <Nome>João Silva</Nome>
    <Email>joao.silva@exemplo.com</Email>
    <CPF_Criptografado>...</CPF_Criptografado>
</CadastroCliente>

XML – Resposta de Consulta
<ClienteInfo>
    <Nome>João Silva</Nome>
    <Email>joao.silva@exemplo.com</Email>
    <CPF>12345678900</CPF>
</ClienteInfo>

8. Coleção Postman

Incluída no repositório:

Middleware_Criptografia_Colecao.json


A coleção contém:

Requisição de cadastro,

Requisição de consulta,

Headers,

Bodies,

Respostas da API.

Atende ao requisito do exercício.

9. Estrutura do Projeto
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
└── services/
      ├── crypto_service.py
      └── xml_service.py

10. Testes

Ferramentas recomendadas:

Postman

Insomnia

cURL

O repositório inclui a coleção Postman para facilitar os testes.

11. Referências

Sistemas Distribuídos – Colouris

Documentação Flask

Documentação PyCryptodome

12. Conclusão

O Middleware cumpre integralmente os requisitos do exercício, incluindo:

API REST funcional

Conversão JSON ↔ XML

Criptografia AES-256

Autenticação via token

Simulação de sistema legado

Exemplos de XML

Coleção Postman