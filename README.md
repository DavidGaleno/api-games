# games-database api

## Introdução
O projeto é uma api que permite a transmissão de informações sobre jogos de video-game. Fizemos um front-end para demonstrar o uso dessa API para os usuários

### Objetivo

A API procura oferecer uma base de informações de jogos para ser utilizada ou personalizada por outros usuários na informação de dados e estatísticas

## Arquitetura
![Arquitetura Games Database API drawio](https://github.com/DavidGaleno/games-database-API/assets/92187957/b77eefdc-1970-4aaf-92bc-fa4bc98efefa)

## Requisitos

### Ambiente

É necessário a instalação do Python, MySQL e Insomnia <br />

Segue abaixo o link para download de cada uma das ferramentas:

[Python](https://www.python.org/downloads/)
[PostgreSQL](https://www.postgresql.org/download/)
[Insomnia](https://insomnia.rest/download)

### Execução

#### Back-End:
1. Abra o PGAmin4 e crie no postgre uma database chamada ```games_database_api```
2. Selecione o local da sua máquina onde deseja salvar o projeto
3. Abra o powershell ou cmd no local selecionado
4. Digite  ```git clone https://github.com/DavidGaleno/games-database-API.git``` para clonar o repositório
5. Digite cd games_database_api
6. Digite ```pip install -r requirements.txt``` para instalar as dependências
7. Entre na pasta setup e acesse o arquivo settings.py
8. Procure por DATABASES e altere o USER para o seu usuário do postgre e o PASSWORD para sua senha do postgre
9. Caso esteja usando Linux, altere o HOST para  ``` 127.0.0.1 ```
10. Execute o comando ``` python manage.py migrate ``` para criar as tabelas no banco de dados 
11. Execute o comando ``` python populate_script.py ``` para popular o banco de dados 
12. Digite ```python manage.py runserver``` para executar a api
13. Acesse o link ```http://localhost:8000/docs``` (Windows) ```http://127.0.0.1:8000/docs``` (Linux) para ver quais entidades e quais são as rotas da API
14. Agora abra o Insomnia e realize as requisições na URI desejada
15. Por fim, leia os cuidados abaixo
#### Cuidados

*** Caso exclua, por exemplo, um item da tabela gênero, todos os jogos que possuem esse gênero serão excluídos. Isso vale para todas as relações de chave estrangeira <br>

#### Front-End:
1. Insira no terminal npm install  para instalar as dependências
2. Copie o caminho do arquivo ```Dashboard.html``` ou ```BuscaJogos.html``` e insira no navegador. Você pode também utilizar a extensão LiveServer no Visual Studio Code.

## Contribuidores
<table>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/92187957?v=4" width="100px;" alt=""/><br /><sub><b>David Galeno</b></sub></td>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/128062428?s=48&v=4" width="100px;" alt=""/><br /><sub><b>Leonardo Vitor</b></sub></td>
  </tr>
</table>
