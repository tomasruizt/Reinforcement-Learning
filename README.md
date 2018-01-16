The goal of this is to benchmark the performance of TD-Learning and Monte-Carlo based learning methods.

* Playing field is a 10x10 cell field. Starting point lower left (0,0) and finishing point on the upper right (9,9). The goal of the agent is to maximize its reward.

* Entering each cell has a specific reward with variance 1. The cell's mean reward is based on the cell's position. The cell on the upper left (0, 9) has mean 0. The cell on the lower right (9,0) has mean 1. The mean reward in the rest of the cells is based on a plane supported by these two points symmetric to starting and finishing points.

* -1 reward per step incentivizes agent to finish
* f: finish, s: start


 - - -
|0| |f|
 - - -
| | | |
 - - -
|s| |1|
 - - -