# Neural Tactics: Perfecting Play with Q-Learning AI

This project showcases the application of Q-learning, a model-free reinforcement learning algorithm, to the ancient game of Nim. By simulating thousands of games between different strategic engines, we aim to refine the AI's ability to win from both advantageous and disadvantageous starting positions.

## Project Overview

- **Strategic Learning**: Implements Q-learning to improve strategy over time.
- **Multiple Opponents**: Tests the AI against both random moves and a deterministic "guru" strategy.
- **Performance Evaluation**: Monitors win rates as the AI's experience grows.
- **Visualization**: Provides clear graphical representations of learning progress.

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

## Simulation Results

The Q-learner's performance is evaluated against both random players and a deterministic guru. The win rates from these simulations are plotted to visualize the AI's learning curve.

- Winning Starting Position: Shows the AI's increasing proficiency when beginning with an advantageous position.
- Losing Starting Position: Demonstrates the AI's capability to gradually recover and win from a less favorable start.


![Qlearner Performance Comparison in Winning Starting Position](/mnt/data/Screenshot from 2024-01-20 21-32-28.png)

![Qlearner Performance Comparison in Losing Starting Position](/mnt/data/Screenshot from 2024-01-20 21-33-22.png)


## Q-Table Logging

For a detailed inspection of the learning process, Q-table logs are generated at various intervals, providing insights into the AI's decision-making process.

## Further Development

This project is open to contributions. Interested parties can fork the repository, push their enhancements, and create a pull request for review.

## Acknowledgments

This project stands on the shoulders of classic AI research and aims to make such foundational knowledge accessible and engaging through practical application in a simple yet intriguing game.

For a detailed understanding of how the Q-learning algorithm is applied within the game of Nim, please refer to the in-code documentation and comments provided within the scripts.
