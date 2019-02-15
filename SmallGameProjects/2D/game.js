var canvas = document.getElementById("gameCanvas");
var ctx = canvas.getContext("2d");

var ballX = canvas.width/2;
var ballY = canvas.height-30;

var dx = 2;
var dy = -2;
var ballRadius = 10;

function drawBall(){
    if(ballX + ballRadius >= canvas.width)
        dx=-1*dx;
    else if(ballX - ballRadius <= 0)
        dx = -1*dx;
    if(ballY - ballRadius <= 0)
        dy = -1*dy;
    else if(ballY + ballRadius >= canvas.height)
        dy = -1*dy;
    ctx.beginPath();
    ctx.arc(ballX, ballY, ballRadius, 0, Math.PI*2);
    ctx.fillStyle = "#FFEE00";
    ctx.fill();
    ctx.closePath();
}

var batHeight = 20;
var batWidth = 100;
var batX = (canvas.width-batWidth)/2;

function drawbat(){
    if(rightPressed)
        batX += 7;
    else if(leftPressed)
        batX -= 7;
    if(rightPressed && batX < canvas.width-batWidth)
        batX += 7;
    else if(leftPressed && batX > 0)
        batX -= 7;
    ctx.beginPath();
    ctx.rect(batX, -1*(canvas.height/10) + canvas.height-batHeight, batWidth, batHeight);
    ctx.fillStyle = "#000000";
    ctx.fill();
    ctx.closePath();
}

function keyDownHandler(e) {
    if(e.key == "Right" || e.key == "ArrowRight") {
        rightPressed = true;
    }
    else if(e.key == "Left" || e.key == "ArrowLeft") {
        leftPressed = true;
    }
}

var rightPressed = false;
var leftPressed = false;

document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

function keyUpHandler(e) {
    if(e.key == "Right" || e.key == "ArrowRight") {
        rightPressed = false;
    }
    else if(e.key == "Left" || e.key == "ArrowLeft") {
        leftPressed = false;
    }
}

function draw(){
    ctx.clearRect(0,0, canvas.width, canvas.height);
    drawBall();
    drawbat();
    ballX += dx;
    ballY += dy;
}
setInterval(draw, 16);
//60FPS=16 ms
