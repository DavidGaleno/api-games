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

![image](https://github.com/DavidGaleno/games-database-API/assets/92187957/75cc8e05-6d1a-4aa7-9157-0e4dc94c1df1)

## Diagrama de Classes
![games-database api _ Classes UML](https://github.com/DavidGaleno/games-database-API/assets/92187957/86f4e79e-3c26-4349-b65e-1c7ce68476b5)

## Requisitos

### Funcionamento

É necessário a instalação do Python, MySQL, Redis, FastAPI e Insomnia

[Python](https://www.python.org/downloads/)
[MySQL](https://dev.mysql.com/downloads/workbench/)
[Insomnia](https://insomnia.rest/download)



## Contribuidores
<table>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/92187957?v=4" width="100px;" alt=""/><br /><sub><b>David Galeno</b></sub></td>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/128062428?s=48&v=4" width="100px;" alt=""/><br /><sub><b>Leonardo Vitor</b></sub></td>
  </tr>
</table>
