const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

const resolution = 10;  //разрешение
// canvas.width = 800;
// canvas.height = 800;

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const COLS = canvas.width / resolution;
const ROWS = canvas.height / resolution;

//сетка, которая представляет собой каждую живую клеку
function buildGrid() {
  return new Array(COLS).fill(null) //заполняем массив нулями чтобы иметь возможность редактировать
    .map(() => new Array(ROWS).fill(null) //создаем для каждого элемента еще одним массив (чтобы сделать матрицу)(я не знаю почему нельзя сделать просто двумерный массив, мб просто чел из тутора долбаеб)
      .map(() => Math.floor(Math.random() * 2))); //рандомно заполняем массив (первые живые клетки)
}

let grid = buildGrid();

requestAnimationFrame(update);

//обнавляем поколения
function update() {
  grid = nextGen(grid); //меняем поколение
  render(grid); //показать грид 
  requestAnimationFrame(update);
}

//реализация алгоритма игры
function nextGen(grid) {
  //делаем копию грида, чтобы обнавлять поколения
  const nextGen = grid.map(arr => [...arr]);

  for (let col = 0; col < grid.length; col++) {
    for (let row = 0; row < grid[col].length; row++) {
      const cell = grid[col][row];
      let numNeighbours = 0;  //кол-во соседей
      //проходимся по соседям (находим их) (проходим по клеткам вокруг точки)
      for (let i = -1; i < 2; i++) {
        for (let j = -1; j < 2; j++) {
          //если индексы 0, 0 - это наша основная клетка, поэтому мы ее пропускаем
          if (i === 0 && j === 0) {
            continue;
          }
          //чтобы не вылетать за границы грида
          const x_cell = col + i; //координаты соседа
          const y_cell = row + j;

          //проверяем что координаты соседа находятся в пределах грида
          if (x_cell >= 0 && y_cell >= 0 && x_cell < COLS && y_cell < ROWS) {
            const currentNeighbour = grid[col + i][row + j];  //определяем соседа
            numNeighbours += currentNeighbour;  //считаем количество соседей
          }
        }
      }

      //правила игры
      if (cell === 1 && numNeighbours < 2) {  //если клетка живая и у нее меньше 2 соседей, она умирает от одиночества
        nextGen[col][row] = 0;
      } else if (cell === 1 && numNeighbours > 3) { //если клетка живая и у нее больше 3 соседей, она умирает от перенаселения
        nextGen[col][row] = 0;
      } else if (cell === 0 && numNeighbours === 3) { //если клетка метрвая и у нее 3 соседа, она оживает
        nextGen[col][row] = 1;
      }
    }
  }
  return nextGen;
}

function render(grid) {
  for (let col = 0; col < grid.length; col++) {
    for (let row = 0; row < grid[col].length; row++) {
      const cell = grid[col][row];

      //размещаем на канве
      ctx.beginPath();
      ctx.rect(col * resolution, row * resolution, resolution, resolution); //координа х, у, ширина канваса, высота канваса
      ctx.fillStyle = cell ? '#9773ff' : '#242424'; //если клетка не пустая, заливаем ее черным
      ctx.fill(); //показываем залитые клетки
      // ctx.stroke(); //сетка
    }
  }
}

