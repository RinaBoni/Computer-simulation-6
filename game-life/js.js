var canvas = document.getElementById('c1');  //получаем канвас
var ctx = canvas.getContext('2d');           //получаем контекст канваса
var mas=[];     //массив - игровое поле
var count = 0;   //счетчик поколений
var timer;
var n=80, m=80;

//при клике срабатывает функция
//работаем с событием event
canvas.onclick = function (event){
    //определяем координату х и у, по которым произошел клик
    var x = event.offsetX;
    var y = event.offsetY;
    console.log(x);
    console.log(y);
    
    //переводим координаты в кубики
    x = Math.floor(x/10);   //300/10 = 30
    y = Math.floor(y/10);

    mas[y][x] = 1;   //заполнение игрового поля
    console.log(mas);
    drawField();

}
//создание поля.массив, который будет имитировать игровое поле
function goLife (){
    for (var i = 0; i<m; i++){
        mas[i]=[];  //объявляем пустой массив
        for (var j=0; j<n; j++){
            mas[i][j]=0;
        }
    }
}


goLife();


//рисуем точку
function drawField(){
    ctx.clearRect(0, 0, 800, 800);  //очищаем канвас
    //проходимся и рисуем точку
    for (var i = 0; i<m; i++){
        for (var j=0; j<n; j++){
            if (mas[i][j]==1){
                ctx.fillRect(j*10, i*10, 10, 10);
            }
        }
    }
}


//моделирование жизни
function startLife(){
    var mas2 = [];
    for (var i = 0; i<m; i++){
        mas2[i]=[];  //объявляем пустой массив
        for (var j=0; j<n; j++){
            //проверяем наличие соседей
            var neighbors = 0;  //соседи

            //делаем бесконечное поле
            if (mas[fpm(i)-1][j]==1) neighbors++;//верхний сосед
            if (mas[i][fpp(j)+1]==1) neighbors++;//сосед справа
            if (mas[fpp(i)+1][j]==1) neighbors++;//нижний сосед
            if (mas[i][fpm(j)-1]==1) neighbors++;//сосед слева
            if (mas[fpm(i)-1][fpp(j)+1]==1) neighbors++;//по диагонали вправо вверх
            if (mas[fpp(i)+1][fpp(j)+1]==1) neighbors++;//по диагонали вправо вниз
            if (mas[fpp(i)+1][fpm(j)-1]==1) neighbors++;//по диагонали влево вниз
            if (mas[fpm(i)-1][fpm(j)-1]==1) neighbors++;//по диагонали влево вверх

            //прирост соседей
            (neighbors==2  || neighbors==3) ? mas2[i][j]=1 : mas2[i][j]=0;          
        }
    }
    mas = mas2;
    drawField();
    count++;
    document.getElementById('count').innerHTML = count;
    timer = setTimeout(startLife, 800);
}


//если индекс равен 0, эта ф-я возвращает 30 (чтобы поле было как бы бесконечное)
function fpm(i){
    if (i==0) return 80;
    else return i;
}

//если индекс равен 29, эта ф-я возвращает -1 (чтобы поле было как бы бесконечное)
function fpp(i){
    if (i==79) return -1;
    else return i;
}

document.getElementById('start').onclick = startLife;