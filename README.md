This library implements the core components of Reinforcement Learning agents.
The goal is to have reusable components that can be composed flexibly together
to tackle a wide range of scenarios.

## Installation
Checkout this package and install it to your Python distribution.
```commandline
$ git clone https://github.com/tomasruizt/Reinforcement-Learning.git
$ cd Reinforcement-Learning
$ pip install .
```
## Usage
The library is structured in a hierarchy. You can import components from each hierachy
and compose your Reinforcement Learning agents that way. For example:
```python
from rl.policy.EpsilonGreedy import EpsilonGreedy
from rl.estimation_updater.MonteCarlo import MonteCarlo

mc = MonteCarlo()

```