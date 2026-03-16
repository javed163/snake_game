const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const BLOCK_SIZE = 20;

function drawGame(state) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = 'green';
    state.snake.forEach(point => {
        ctx.fillRect(point[0], point[1], BLOCK_SIZE, BLOCK_SIZE);
    });
    ctx.fillStyle = 'red';
    ctx.fillRect(state.food[0], state.food[1], BLOCK_SIZE, BLOCK_SIZE);
    document.getElementById('score').innerText = `Score: ${state.score}`;
}

async function updateGame() {
    const response = await fetch('/get_state');
    const state = await response.json();
    drawGame(state);
    if (!state.done) {
        setTimeout(updateGame, 100);
    }
}

document.getElementById('startBtn').addEventListener('click', async () => {
    await fetch('/start', { method: 'POST' });
    updateGame();
});
document.getElementById('trainBtn').addEventListener('click', async () => {
    await fetch('/train', { method: 'POST' });
});
document.getElementById('stopBtn').addEventListener('click', async () => {
    await fetch('/stop', { method: 'POST' });
});
document.getElementById('saveBtn').addEventListener('click', async () => {
    await fetch('/save_model', { method: 'POST' });
});