# snake_game
---

## Project Overview

The project consists of three main components:

1. **Game Logic (`game.py`)**  
   - Implements the classic Snake game using Pygame.  
   - Handles snake movement, collision detection, food spawning, and scoring.  

2. **AI Agent (`agent.py`)**  
   - Implements a **Deep Q-Learning agent** that interacts with the game.  
   - Maintains memory for past experiences and trains both short-term and long-term.  
   - Selects moves using an **epsilon-greedy policy** to balance exploration and exploitation.  

3. **Neural Network (`model.py`)**  
   - Defines a **Linear Q-Network** using PyTorch.  
   - Predicts Q-values for each possible action.  
   - Includes a `QTrainer` class to perform training steps.  

4. **Helper Functions (`helper.py`)**  
   - Plotting game scores and mean scores.  
   - Additional utilities used by the agent.  

---

## Features

- Classic Snake game with real-time display using Pygame.  
- AI agent learns autonomously using **Deep Q-Learning**.  
- Supports:
  - Short-term memory training (per move)  
  - Long-term memory training (batch replay)  
  - Epsilon-greedy exploration with decay  
  - Model saving for new record scores  
- Real-time plotting of scores and mean scores during training.  
- Adjustable hyperparameters like learning rate, batch size, gamma, and memory size.  

---

## Requirements

- Python 3.11+  
- [Pygame](https://www.pygame.org/)  
- [PyTorch](https://pytorch.org/)  
- NumPy  

Install dependencies with:

```bash
pip install pygame torch numpy