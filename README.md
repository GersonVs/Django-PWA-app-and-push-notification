# Django-PWA-app-and-push-notification

## Passo a passo para rodar o projeto

1. Criar uma virtualenv e instalar o requirements.txt
2. Ativar a virtualenv
3. Migrar o banco de dados
4. Criar um superusuário com o nome **admin**
5. Executar o servidor do projeto
6. Instalar o [ngrok](https://ngrok.com/download). 
> Necessário para criar uma rede com certificado ssl.
7. Criar o domínio publico apontando para o servidor local `ngrok http {porta onde o projeto esta sendo execudo}`
8. Acessar o caminho em **Forwarding**
9. Fazer login
10. Voltar para a tela inicial `/` e enviar um mensagem
