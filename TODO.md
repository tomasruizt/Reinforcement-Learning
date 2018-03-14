## Design
* Deprecate the Interfaces.py file.
* Complete / deprecate the valueApproximator, policy and learning_strategy packages
* Is it possible to decouple the ValueApproximator (e.g. linear model, NN) from the ValueUpdateStrategy interface (e.g. TDLambda, semi-gradient, OLS)
* Should a ValueUpdateStrategy offer the get_information() API? It may be necessary to implement both a contextual linear model as well a a context-free model before seeing how the APIs are similar.
## Testing
* Test the SequentialGame
* Test action_scores validation
