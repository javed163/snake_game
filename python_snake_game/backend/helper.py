def plot(scores, mean_scores):
    import matplotlib.pyplot as plt
    import numpy as np

    plt.figure(figsize=(10, 5))
    plt.plot(np.arange(len(scores)), scores, label='Scores', color='blue')
    plt.plot(np.arange(len(mean_scores)), mean_scores, label='Mean Scores', color='orange')
    plt.title('Scores and Mean Scores Over Time')
    plt.xlabel('Games')
    plt.ylabel('Scores')
    plt.legend()
    plt.show()