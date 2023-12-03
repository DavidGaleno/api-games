const { performSearch } = require("./BuscarJogos");
const { fireEvent } = require("@testing-library/dom");

describe("performSearch", () => {
  document.body.innerHTML = `
    <div class="divPrincipal">
    <div class="divPesquisa">
      <input
        class="inputJogos"
        type="text"
        id="input"
        placeholder="Busque o jogo que quiser!"
      />
      <button class="material-symbols-outlined">search</button>
    </div>
    <div class="progress-container">
      <div class="progress-bar" id="myBar"></div>
    </div>
    <div class="data">
      <h2>Informações do Jogo</h2>
      <div class="data-content"></div>
    </div>
  </div>
    `;

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

  test("deve exibir uma mensagem se o campo de busca estiver vazio", async () => {
    inputField.value = "";

    fireEvent.click(searchButton);

    expect(dataContent.innerHTML).toBe("<h3>Preencha o campo de Busca</h3>");
  });

  test("deve exibir uma mensagem se nenhum jogo for encontrado", async () => {
    inputField.value = "jogoQueNãoExiste";

    fireEvent.click(searchButton);

    setTimeout(() => {
      expect(dataContent.innerHTML).toBe("<h3> Jogo não Encontrado</h3>");
    }, 3000);
  });

  test("deve detectar que há jogos adicionados no DOM", async () => {
    inputField.value = "res";

    fireEvent.click(searchButton);

    setTimeout(() => {
      const jogos = document.querySelectorAll("dados-jogo");

      expect(jogos.length).toBeGreaterThan(0);
    }, 3000);
  });
});
