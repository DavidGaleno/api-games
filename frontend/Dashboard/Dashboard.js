const createCharts = async () => {
  const jogos = await fetch("http://127.0.0.1:8000/games/")
    .then((res) => res.json())
    .then((data) => data);
  const generos = await fetch("http://127.0.0.1:8000/genres/")
    .then((res) => res.json())
    .then((data) => data);
  const jogosGeneros = await fetch("http://127.0.0.1:8000/game_genres/")
    .then((res) => res.json())
    .then((data) => data);

  const jogosDates = jogos.map((jogo) => {
    const date = new Date(jogo.release_date);
    return date.getFullYear();
  });
  const jogosDatesUnique = [...new Set(jogosDates)].sort();

  var optionsAnos = {
    chart: {
      type: "line",
    },
    series: [
      {
        name: "",
        data: jogosDatesUnique.map(
          (yearUnique) =>
            jogosDates.filter((year) => year === yearUnique).length
        ),
      },
    ],
    responsive: [
      {
        breakpoint: 633,
        options: {
          chart: {
            width: 400,
          },
          legend: {
            position: "bottom",
          },
        },
      },
      {
        breakpoint: 447,
        options: {
          chart: {
            width: 300,
          },
          legend: {
            position: "bottom",
          },
        },
      },
      {
        breakpoint: 375,
        options: {
          chart: {
            width: 250,
          },
          legend: {
            position: "bottom",
          },
        },
      },
    ],
    xaxis: {
      categories: [...new Set(jogosDates)].sort(),
    },
  };

  var chartLine = new ApexCharts(
    document.querySelector("#chartline"),
    optionsAnos
  );

  chartLine.render();

  var optionsGeneros = {
    chart: {
      type: "donut", // 'pie' para um gráfico de pizza ou 'donut' para um gráfico de donut
    },
    series: generos.map(
      (genero) =>
        jogosGeneros.filter((jogoGenero) => jogoGenero.genre === genero.id)
          .length
    ),
    labels: generos.map((genero) => genero.name),
    responsive: [
      {
        breakpoint: 633,
        options: {
          chart: {
            width: 400,
          },
          legend: {
            position: "right",
          },
        },
      },
      {
        breakpoint: 447,
        options: {
          chart: {
            width: 350,
          },
          legend: {
            position: "right",
          },
        },
      },
      {
        breakpoint: 400,
        options: {
          chart: {
            width: 320,
          },
          legend: {
            position: "bottom",
          },
        },
      },
    ],
  };

  // Inicializar o gráfico
  var chartDonut = new ApexCharts(
    document.getElementById("chartdonut"),
    optionsGeneros
  );
  chartDonut.render();
};
createCharts();
