<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {inlineMath: [["$","$"],["\\(","\\)"]]}
  });
</script>
<script async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# Week 2: Linear Regression

## Multiple variables

- number of features: $ n $
- number of training examples: $ m $
- feature vector of i-th training example: $ x^{(i)} $
- value of feature j in i-th training example: $ x^{(i)}_j $
- hypothesis: $h_\theta (x) = \theta_0 x_0 + \theta_1 x_1 + + \theta_2 x_2 + … + + \theta_n x_n$
- features vector x:  $ \begin{bmatrix}   x_{0} \\  x_{1} \\  \vdots \\ x_{n} \end{bmatrix}  $
- parameters vector $ \theta $ : $ \begin{bmatrix}   \theta_{0} \\  \theta_{1} \\  \vdots \\ \theta_{n} \end{bmatrix}$
- short notation for hypothesis: $ h_\theta (x) = \Theta^T x $

## Gradient descent for multiple variables

## Gradient descent in practice I: Feature Scaling

- Make sure features are on same scale
- Approximate range: $ -1 ≲ x_i ≲ 1 $
- Mean normalisation: $ \dfrac {x_1 - \mu_1}{x_{max} -x_{min}} $

## Gradient descent in practice II: Learning rate

- Learning rate: $ \alpha $
- Gradient descent for each $ \theta $: $ \theta_j = \alpha \dfrac {\delta}{\delta \theta_j} J(\theta) $
- Graph of number of iterations by $ J_\theta $
  - Fast convergence: $ \alpha $ is just right
  - Slow convergence $ \alpha $ is too small
  - Oscillates: $ \alpha $ is too big
  - When to stop: $ J(\theta) $ decreases by less than $ 10^{-3} $
  - Values of $ \alpha $ to try: 0.001, 0.01, 0.1, 1

## Features and polynomial regression

- Some features could be combined E.g. length and breadth can be combined to area

## Normal equation

- Alternative to gradient descent
- $ \theta = (X^T X)^{-1} X^Ty $
- octave: `pinv(X'*X) *X'*y`

|            | Gradient descent | Normal Equation    |
| ---------- | ---------------- | ------------------ |
| α          | need to choose   | no need to use     |
| iterations | many             | none               |
| n is large | works well       | slow in comptation |


## Normal equation and non-invertibility (optional)

When is $ X^T X $ non-invertible?

- redundant features $ n $
  - features are linearly dependant on each other
- too many feature
  - $ m ≦ n $
  - delete some features or use regularisation
