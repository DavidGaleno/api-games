# games-database api

## Introdução
O projeto é uma api que permite a transmissão de informações sobre jogos de video-game.
A api poderá ser utilizada por 3 públicos: Acionistas, Fans e Programadores

### Objetivo

A API atua tanto procurando dados na base de dados, quanto filtrando os dados de acordo com o público consumidor.

**Cada público terá seu próprio objetivo:**

- Acionistas terão uma prioridade por informações financeiras, que serão utilizadas para manejar seus investimentos
- Fans utilizaram somente por diversão, para saber meus sobre seus jogos favoritos
- Os programadores irão procurar informações técnicas sobre os jogos, seja para se basearem para seus próprios jogos, seja por curiosidade

## Arquitetura
- Por ser uma API que irá lidar somente com um tipo de entidade, iremos utilizar uma arquitetura monolítica
- Iremos utilizar dois bancos para comparações, visto que foi pedido por nosso professor
![Arquitetura Games Database API](https://github.com/DavidGaleno/games-database-API/assets/92187957/bc809d81-23d4-4663-9e50-ddbbb3f29be0)

## Requisitos

### Ambiente

É necessário a instalação do Python, MySQL e Insomnia <br />

Segue abaixo o link para download de cada uma das ferramentas:

[Python](https://www.python.org/downloads/)
[PostgreSQL](https://www.postgresql.org/download/)
[Insomnia](https://insomnia.rest/download)

### Execução

1. Crie um database com o nome games_database_api no postgreSQL
2. Selecione o local da sua máquina onde deseja salvar o projeto
3. Abra o powershell ou cmd no local selecionado
4. Digite  ```git clone https://github.com/DavidGaleno/games-database-API.git``` para clonar o repositório
5. Digite cd games_database_api
6. Digite ```pip install -r requirements.txt``` para instalar as dependências
7. Digite ```python manage.py runserver``` para executar a api
8. Acesse o link ```http://localhost:8000/``` para ver quais entidades e as operações que podem ser realizadas com cada uma delas
9. Agora abra o Insomnia e realize as requisições na URI desejada
10. Por fim, leia os cuidados abaixo
#### Cuidados

*** Ao excluir um item da tabela genre, franchis, developer ou publisher que está sendo usado por um item da tabela game, ambos serão excluídos <br>


## Contribuidores
<table>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/92187957?v=4" width="100px;" alt=""/><br /><sub><b>David Galeno</b></sub></td>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/128062428?s=48&v=4" width="100px;" alt=""/><br /><sub><b>Leonardo Vitor</b></sub></td>
  </tr>
</table>
