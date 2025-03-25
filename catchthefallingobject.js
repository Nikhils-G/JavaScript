const canvas = document.createElement("canvas");
const ctx = canvas.getContext("2d");
document.body.appendChild(canvas);
canvas.width = 400;
canvas.height = 500;

const basket = {
    x: 175,
    y: 450,
    width: 50,
    height: 20,
    speed: 5,
};

const apple = {
    x: Math.random() * 350,
    y: 0,
    radius: 10,
    speed: 2,
};

let score = 0;

document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft" && basket.x > 0) {
        basket.x -= basket.speed;
    } else if (event.key === "ArrowRight" && basket.x < canvas.width - basket.width) {
        basket.x += basket.speed;
    }
});

function update() {
    apple.y += apple.speed;
    
    if (apple.y > canvas.height) {
        apple.y = 0;
        apple.x = Math.random() * 350;
    }

    if (
        apple.y + apple.radius > basket.y &&
        apple.x > basket.x &&
        apple.x < basket.x + basket.width
    ) {
        score++;
        apple.y = 0;
        apple.x = Math.random() * 350;
    }
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    ctx.fillStyle = "red";
    ctx.beginPath();
    ctx.arc(apple.x, apple.y, apple.radius, 0, Math.PI * 2);
    ctx.fill();
    
    ctx.fillStyle = "brown";
    ctx.fillRect(basket.x, basket.y, basket.width, basket.height);
    
    ctx.fillStyle = "black";
    ctx.fillText("Score: " + score, 10, 20);
}

function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

gameLoop();
