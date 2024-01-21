# Neural Tactics: Advancing Nim with AI

This project delves into the realm of data science and artificial intelligence to tackle the strategic optimization of the Nim game using Q-learning. Through iterative learning and data-driven decision-making, the initiative aims to enhance the gameplay of an AI agent. It encapsulates the core data science process: collecting game state data, learning from this data through reinforcement learning, and validating the strategy through extensive simulation and statistical analysis.

## Project Overview

- **Strategic Learning**: Implements Q-learning to improve strategy over time.
- **Multiple Opponents**: Tests the AI against both random moves and a deterministic "guru" strategy.
- **Performance Evaluation**: Monitors win rates as the AI's experience grows.
- **Visualization**: Provides clear graphical representations of learning progress.

## Data Science Integration

- **Data Collection**: During gameplay, each state and the resulting moves are recorded, generating a vast dataset of game scenarios.
- **Statistical Learning**: Utilizing Q-learning, an AI agent incrementally improves by updating a Q-table based on the reward structure, a quintessential example of learning from data.
- **Data Visualization**: The project employs advanced visualization techniques to graphically represent the AI's performance, making the learning process transparent and interpretable.
- **Performance Metrics**: Win rates serve as the key metric for evaluating the AI's strategy, reflecting improvements and guiding further optimizations.

## Dependencies

The project requires the following libraries:

- numpy
- random
- matplotlib

## Installation and Execution

Clone the repository and navigate to the project directory. Run the Python scripts provided to simulate games and visualize the results.

```
git https://github.com/malsuwailm/q-learning-strategy-optimization.git
cd q-learning-strategy-optimization
python nim_qlearning.py
```

## Analysis and Results

![Qlearner Performance Comparison in Winning Starting Position](https://github.com/malsuwailm/q-learning-strategy-optimization/blob/main/plots/winning.png)

![Qlearner Performance Comparison in Losing Starting Position](https://github.com/malsuwailm/q-learning-strategy-optimization/blob/main/plots/losing.png)

The AI's performance is critically assessed through its win rate against both random moves and a pre-programmed expert strategy, visualized through two different plots:

1. **Winning Starting Position**: The first plot shows the AI's win rate when starting from a position deemed advantageous. A clear upward trend is observed as the number of training games increases, demonstrating the AI's ability to capitalize on favorable conditions.

2. **Losing Starting Position**: The second plot reveals the AI's ability to overturn a losing start into a win. Despite the challenging circumstances, there's a marked improvement in performance, which is a testament to the AI's learning capacity and the effectiveness of the Q-learning algorithm.

### Analysis of Plots

- In the context of a winning starting position, the AI's learning curve exhibits a saturating increase, indicating a plateau in strategy refinement as it approaches an optimal gameplay strategy.

- Conversely, the losing starting position presents a more volatile learning process, with notable fluctuations in win rate. This variability suggests the complexity of learning under disadvantageous conditions and points to the potential for further fine-tuning of the Q-learning parameters or strategy.

These graphical insights not only quantify the AI's learning trajectory but also highlight the intricate balance between exploration and exploitation in machine learning.


## Q-Table Logging

For a detailed inspection of the learning process, Q-table logs are generated at various intervals, providing insights into the AI's decision-making process.

## Further Development

The project invites collaboration for those keen on exploring the intersection of AI and game theory, offering opportunities to enhance the Q-learning algorithm and explore other data-driven techniques to elevate game strategy.

## Acknowledgments

This project is a modern intersection of game theory, AI, and data science, paying homage to the rich history of both the game of Nim and the field of artificial intelligence. Through a data-centric lens, it aims to contribute to the continuous dialogue between strategic gaming and computational intelligence.
