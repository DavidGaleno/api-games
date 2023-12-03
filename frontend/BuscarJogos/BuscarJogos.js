function performSearch(
  progressBar,
  progressContainer,
  dataContent,
  inputField
) {
  const searchTerm = inputField.value.trim().toLowerCase();
  if (searchTerm.length === 0) {
    return (dataContent.innerHTML = "<h3>Preencha o campo de Busca</h3>");
  }

  dataContent.innerHTML = "";

  // Exibir a barra de progresso
  progressContainer.style.display = "block";

  // Iniciar a barra de progresso
  let width = 0;

  //Inicia intervalo de loading
  const interval = setInterval(async function () {
    if (width >= 100) {
      clearInterval(interval);

      //Pega os jogos que contêm os caracteres inseridos na busca
      const jogosArray = await fetch(
        `http://127.0.0.1:8000/games/name/${searchTerm}`,
        {
          method: "GET",
          mode: "cors",
        }
      )
        .then((res) => res.json())
        .then((data) => data);

      const genresArray = await fetch(`http://127.0.0.1:8000/genres`, {
        method: "GET",
        mode: "cors",
      })
        .then((res) => res.json())
        .then((data) => data);

      // Lógica para verificar se o jogo foi encontrado no array.
      const jogoSelecionado = jogosArray.filter((jogo) =>
        jogo.name.startsWith(searchTerm)
      );

      //Lógica para capitalizar os nomes do banco de dados
      function capitalizeWords(str) {
        const array = str.includes("/") ? str.split("/") : str.split(" ");
        return array
          .map((word) =>
            word.replace(/\b\w/, function (char) {
              return char.toUpperCase();
            })
          )
          .join(" ");
      }

      // Se o jogo foi encontrado, preencha as informações
      if (jogoSelecionado.length > 0) {
        jogoSelecionado.map(async (jogo) => {
          const jogoDOM = `
                  <div class="dados-jogo">
                    <p>
                      Nome do Jogo:
                      <span id="nomeJogo">${capitalizeWords(jogo.name)}</span>
                    </p>
                    <p>
                      Ano de lançamento:
                      <span id="dataLancamento">
                        ${new Date(jogo.release_date)
                          .getDay()
                          .toString()
                          .padStart(2, "0")}/${(
            new Date(jogo.release_date).getMonth() + 1
          )
            .toString()
            .padStart(2, "0")}/${new Date(jogo.release_date).getFullYear()}
                      </span>
                    </p>
                    <p>
                      Franquia:
                      <span id="franquia">
                        ${await fetch(
                          `http://127.0.0.1:8000/franchises/${jogo.franchise}`
                        )
                          .then((res) => res.json())
                          .then((data) => capitalizeWords(data.name))}
                      </span>
                    </p>
                    <p>
                      Gênero:
                      <span id="genero">
                        ${capitalizeWords(
                          await fetch(`http://127.0.0.1:8000/game_genres`)
                            .then((res) => res.json())
                            .then(
                              (gameGenres) =>
                                genresArray.find(
                                  (genre) =>
                                    genre.id ===
                                    gameGenres.find(
                                      (gameGenre) => gameGenre.game === jogo.id
                                    ).genre
                                ).name
                            )
                        )}
                      </span>
                    </p>
                    <p>
                      Publicadora:
                      <span id="publicadora">
                        ${await fetch(
                          `http://127.0.0.1:8000/publishers/${jogo.publisher}`
                        )
                          .then((res) => res.json())
                          .then((data) => capitalizeWords(data.name))}
                      </span>
                    </p>
                    <p>
                      Desenvolvedora:
                      <span id="desenvolvedora">
                        ${await fetch(
                          `http://127.0.0.1:8000/developers/${jogo.developer}`
                        )
                          .then((res) => res.json())
                          .then((data) => capitalizeWords(data.name))}
                      </span>
                    </p>
                    <p>
                      Engine:
                      <span id="engine">
                        ${await fetch(
                          `http://127.0.0.1:8000/game_engine/${jogo.gameEngine}`
                        )
                          .then((res) => res.json())
                          .then((data) => capitalizeWords(data.name))}
                      </span>
                    </p>
                  </div>
                `;
          dataContent.innerHTML += jogoDOM;
        });
      } else {
        dataContent.innerHTML += "<h3> Jogo não Encontrado</h3>";
      }

      // Resetar a barra de progresso após a conclusão da pesquisa
      width = 0;
      progressBar.style.width = width + "%";

      // Ocultar a barra de progresso após a conclusão da pesquisa
      progressContainer.style.display = "none";
    } else {
      width++;
      progressBar.style.width = width + "%";
    }
  }, 10);
}
document.addEventListener("DOMContentLoaded", function () {
  const searchButton = document.querySelector(".material-symbols-outlined");
  const dataContent = document.querySelector(".data-content");
  const inputField = document.getElementById("input");
  const progressBar = document.getElementById("myBar");
  const progressContainer = document.querySelector(".progress-container");

  // Event listener para o botão de pesquisa
  searchButton.addEventListener("click", function () {
    performSearch(progressBar, progressContainer, dataContent, inputField);
  });

  // Event listener para o campo de entrada para lidar com a tecla Enter
  inputField.addEventListener("keypress", function (event) {
    // Verificar se a tecla pressionada é Enter (código 13)
    if (event.key === "Enter") {
      performSearch(progressBar, progressContainer, dataContent, inputField);
    }
  });

  // Função para realizar a pesquisa
});

// Exporte a função para os testes
if (typeof module !== "undefined" && module.exports) {
  module.exports = { performSearch };
}
