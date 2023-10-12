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

1. Selecione o local da sua máquina onde deseja salvar o projeto
2. Abra o powershell ou cmd no local selecionado
5. Digite  ```git clone <link do repositório>``` para clonar o repositório
6. Abra a pasta do projeto, depois abra a pasta core e por fim abra o arquivo ```configs.py``` em um editor de texto ou em uma IDE
7. Modifique a linha ```DB_URL: str = 'postgresql+asyncpg://postgres:ipe%402023@localhost:5432/games_database_api'```, substituindo ```postgres:ipe%402023``` por seu usuário do postgre antes dos dois pontos e pela sua senha após os dois pontos
8. Volte para o Powershell ou CMD e digite ```cd games-database-API``` para entrar na pasta do arquivo
9. Digite ```pip install -r requirements.txt``` para instalar as dependências
10. Digite ```python create_table.py``` para criar as tabelas no banco de dados
11. Digite ```python main.py``` para executar a api
12. Acesse o link ```http://localhost:8000/docs``` para ver quais entidades e as operações que podem ser realizadas com cada uma delas
13. Por fim, abra o Insomnia e realize as requisições na URI desejada
#### Cuidados

*** Ao excluir um item da tabela gênero que está sendo usado por um item da tabela jogo, ambos serão excluídos <br>
*** É necessário digitar os campos de gênero, franquia, desenvolvedora e publicadora exatamente como estão nas tabelas ou ocorrerá um erro. Por isso, realize um GET em cada uma das entidades para saber como se escreve exatamente antes de realizar a operação de POST no jogo.


## Contribuidores
<table>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/92187957?v=4" width="100px;" alt=""/><br /><sub><b>David Galeno</b></sub></td>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/128062428?s=48&v=4" width="100px;" alt=""/><br /><sub><b>Leonardo Vitor</b></sub></td>
  </tr>
</table>
