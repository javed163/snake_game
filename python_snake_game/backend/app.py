from flask import Flask, jsonify, request
# from backend.agent import Agent
from backend.game import SnakeGame
from backend.agent import Agent

app = Flask(__name__)
agent = Agent()
game = SnakeGame()

@app.route('/start', methods=['POST'])
def start_game():
    global game
    game.reset()
    agent.n_games = 0
    return jsonify({"message": "Game started!"})

@app.route('/train', methods=['POST'])
def train_agent():
    global game, agent
    while True:
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)
        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()
            return jsonify({"message": "Training step completed!", "score": score})

@app.route('/save_model', methods=['POST'])
def save_model():
    agent.model.save()
    return jsonify({"message": "Model saved!"})

@app.route('/stop', methods=['POST'])
def stop_training():
    return jsonify({"message": "Training stopped!"})

if __name__ == '__main__':
    app.run(debug=True)