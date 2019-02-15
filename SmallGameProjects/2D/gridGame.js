var gridGameCanvas = document.getElementById("gridGameCanvas");
var ctxt = gridGameCanvas.getContext("2d");

var grid = [
            [1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
]

var cellLength = 60;

function drawGrid(){
    //draws border
    ctxt.beginPath();
    ctxt.rect(5,5,canvas.width-1,canvas.height-1);
    ctxt.fillStyle = "#222222";
    ctxt.closePath();

    //drawing all the squares
    var i = 0;
    var j = 0;
    var temp1;
    var temp2;
    for(i=0; i < grid.length; i++){
        for(j=0; j < grid[i].length; j++){
            temp1 = cellLength*i;
            temp2 = cellLength*j;
            if(grid[i][j]==0){
                drawEmptyCell(temp1, temp2);
            }
            else if(grid[i][j]==1){
                drawCell(temp1, temp2);
            }
        }
    }
}

function drawEmptyCell(x, y){
    ctxt.beginPath();
    ctxt.rect(x,y,cellLength,cellLength);
    ctxt.fill();
    ctxt.fillStyle = "#DEEDEE";
    ctxt.closePath();
}

function drawCell(x, y){
    ctxt.beginPath();
    ctxt.rect(x,y,cellLength,cellLength);
    ctxt.fill();
    ctxt.fillStyle = "#FFFFFF";
    ctxt.closePath();
}

function draw(){
    drawGrid();
}
setInterval(draw, 16);
