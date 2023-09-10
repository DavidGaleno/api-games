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
![Arquitetura Games Database API drawio](https://github.com/DavidGaleno/games-database-API/assets/92187957/e7d30be1-91d7-4002-abe5-e844cb8b0be9)



## Diagrama de Classes
![games-database api Classes UML](https://github.com/DavidGaleno/games-database-API/assets/92187957/4c2e9d08-2ae9-487b-a7fa-0c8ec56b6f4b)

## Requisitos

### Ambiente

É necessário a instalação do Python, MySQL e Insomnia <br />

Segue abaixo o link para download de cada uma das ferramentas:

[Python](https://www.python.org/downloads/)
[MySQL](https://dev.mysql.com/downloads/workbench/)
[Insomnia](https://insomnia.rest/download)

#### Fast API

Para instalar o fastapi, basta abrir o terminal e entrar na pasta do projeto com o comando ``` cd api ``` e executar o comando ``` pip install fastapi ```

#### Uvicorn

Para instalar o uvicorn, basta abrir o terminal e entrar na pasta do projeto com o comando ``` cd api ``` e executar o comando ``` pip install uvicorn ```

## Contribuidores
<table>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/92187957?v=4" width="100px;" alt=""/><br /><sub><b>David Galeno</b></sub></td>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/128062428?s=48&v=4" width="100px;" alt=""/><br /><sub><b>Leonardo Vitor</b></sub></td>
  </tr>
</table>
