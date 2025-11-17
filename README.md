# Middleware Web Service com Criptografia e Integração XML

## 1. Descrição do Projeto

Este projeto implementa um **Middleware Web Service** baseado em **Python + Flask**, funcionando como uma camada intermediária entre:

* **Clientes Externos (Web/Mobile via JSON/REST)**
* **Sistema Legado Interno (XML)**

O Middleware garante **segurança**, **compatibilidade** e **isolamento**, atendendo aos requisitos de uma arquitetura distribuída conforme os capítulos 9 e 13 do livro *Sistemas Distribuídos – Colouris*.

### Funções principais

1. **API REST** para comunicação com clientes externos.
2. **Conversão JSON ↔ XML** entre cliente e sistema legado.
3. **Criptografia AES-256** do campo **CPF**.
4. **Autenticação via Token**.
5. **Encapsulamento** e **proteção** do sistema legado.

---

## 2. Tecnologias Utilizadas

* **Python 3.x**
* **Flask (framework web)**
* **PyCryptodome (biblioteca Crypto)** para criptografia AES
* Manipulação de **XML** usando `xml.etree.ElementTree`

---

## 3. Configuração e Execução

### 3.1 Pré-requisitos

* Python 3 instalado

### 3.2 Instalar dependências

Você pode usar o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Ou instalar manualmente:

```bash
pip install Flask pycryptodome
```

### 3.3 Executar o servidor

```bash
python app.py
```

Servidor disponível em:

```
http://127.0.0.1:5000/
```

---

## 4. Segurança e Criptografia

### 4.1 Autenticação via Token

* Todas as requisições passam por um `@app.before_request`.
* O token é verificado contra o valor definido em **config.py**.
* Cabeçalho obrigatório:

```
Authorization: Bearer <TOKEN>
```

### 4.2 Criptografia do CPF

* Algoritmo: **AES-256 (CBC)**
* Apenas o **CPF** é criptografado.
* A chave é armazenada em **Base64** em `config.py`.
* No módulo `crypto_service.py`, a chave é decodificada para **32 bytes**, garantindo compatibilidade com o AES-256.

### 4.3 HTTPS (Ambiente Real)

Em produção:

* O Middleware opera atrás de um **Proxy Reverso** (NGINX/Apache).
* O proxy faz o **TLS Termination**, garantindo comunicação segura para o cliente externo.
* O tráfego entre Proxy ↔ Middleware pode ser interno (rede privada).

---

## 5. Exemplos de Requisições

### 5.1 POST /cliente — Cadastro

**Objetivo:** Cadastrar um novo cliente

**URL:**

```
POST http://127.0.0.1:5000/cliente
```

**Headers:**

```
Authorization: my-secret-api-token-12345
Content-Type: application/json
```

**Body (JSON):**

```json
{
  "nome": "João Silva",
  "cpf": "12345678900",
  "email": "joao.silva@exemplo.com"
}
```

---

### 5.2 GET /cliente/{cpf_criptografado}

**Objetivo:** Consultar cliente pelo CPF criptografado

**Exemplo de URL:**

```
GET http://127.0.0.1:5000/cliente/hx5IIrLVq42KbXWDcPWvLCqt8nvDeuLRKKlnvbrtQ3o=
```

**Header:**

```
Authorization: my-secret-api-token-12345
```

**Body:** vazio

---

## 📜6. Estruturas XML (Exemplos)

Os arquivos XML foram disponibilizados também como:

* `xml_requisicao_cadastro.xml`
* `xml_resposta_consulta.xml`

### 6.1 XML de Requisição (Cadastro)

```xml
<CadastroCliente>
    <Nome>João Silva</Nome>
    <Email>joao.silva@exemplo.com</Email>
    <CPF_Criptografado>hx5IIrLVq42KbXWDcPWvLCqt8nvDeuLRKKlnvbrtQ3o=</CPF_Criptografado>
</CadastroCliente>
```

---

##  7. Estrutura de Pastas

```
middleware-project/
│   app.py
│   config.py
│   crypto_service.py
│   requirements.txt
│   README.md
│
├── xml_examples/
│     ├── xml_requisicao_cadastro.xml
│     └── xml_resposta_consulta.xml
```

---

##  8. Testes

* Teste com ferramentas como: **Postman**, **Insomnia**, **cURL**.
* Valide a criptografia testando `/cliente` → `/cliente/{cpf}`.

---

##  9. Referências

* *Sistemas Distribuídos — Colouris*, Capítulos 9 e 13
* Documentação Flask
* Documentação PyCryptodome

---

##  10. Conclusão

Este Middleware implementa segurança, interoperabilidade e isolamento, garantindo comunicação segura entre clientes modernos e sistemas legados baseados em XML, com criptografia robusta e arquitetura distribuída adequada.
