# Projeto de Implementação de Notificações com Django REST Framework

## Sobre o Projeto

Este projeto foi desenvolvido como parte de um exercício prático da disciplina de Manutenção de Software, com o objetivo de implementar uma funcionalidade comum em aplicações web: **notificações de usuário via e-mail**, utilizando o framework **Django REST Framework (DRF)**.

A funcionalidade foi construída após um minicurso introdutório sobre DRF e visa demonstrar a criação de endpoints RESTful integrados a um serviço externo de envio de e-mails.

## Tecnologias Utilizadas

* **Django**
* **Django REST Framework (DRF)**
* **Python**

## Funcionalidades Implementadas

O projeto implementou os seguintes passos exigidos no escopo do trabalho:

1.  **Configuração do Projeto DRF:** Inicialização de um projeto Django e configuração do DRF.
2.  **Endpoint de Notificação:** Criação de um endpoint REST (`POST /api/notificar/`, por exemplo) que recebe os parâmetros necessários para o envio da notificação (e.g., destinatário, assunto, corpo da mensagem).
3.  **Configuração da API de E-mail:** Integração e configuração de um serviço de envio de e-mails no *backend* Django.
4.  **Testes Integrados:** Verificação do fluxo completo, desde a requisição ao endpoint até o envio bem-sucedido do e-mail.

## Como Configurar e Rodar o Projeto

### Pré-requisitos

* Python (3.x)
* pip

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://gitlab.com/manutencao_software/api-notificacao.git
    cd api-notificacao
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # ou
    venv\Scripts\activate     # Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuração do Serviço de E-mail

O projeto utiliza o serviço de e-mail SMTP do Gmail. As credenciais e configurações devem ser definidas no arquivo `settings.py` ou, preferencialmente, através de variáveis de ambiente.

**Exemplo de Variáveis de Ambiente Necessárias (adapte conforme seu uso):**

| Variável | Descrição | Exemplo |
| :--- | :--- | :--- |
| `EMAIL_HOST` | Servidor SMTP | `smtp.exemplo.com` |
| `EMAIL_PORT` | Porta do Servidor SMTP | `587` |
| `EMAIL_HOST_USER` | Usuário do E-mail | `seu.email@exemplo.com` |
| `EMAIL_HOST_PASSWORD` | Senha/App Password | `sua_senha_secreta` |

### Execução

1.  **Execute as migrações do banco de dados (se houver):**
    ```bash
    python manage.py migrate
    ```

2.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
    O servidor estará disponível em `http://127.0.0.1:8000/`.

## Como Testar a Funcionalidade

Para testar o envio de notificações, utilize o endpoint `POST` criado.

**Endpoint:** `/api/notificar/` (ou o que você definiu)

**Método:** `POST`

**Corpo da Requisição (JSON de Exemplo):**

```json
{
    "destinatario": "teste@exemplo.com",
    "assunto": "Sua Nova Notificação",
    "mensagem": "Este é o corpo da mensagem enviada pelo DRF."
}