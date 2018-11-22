<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {inlineMath: [["$","$"],["\\(","\\)"]]}
  });
</script>
<script async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# Week 3: Logistic Regression

## Hypothesis representation for Classification

- Results: $ y \in \{ 0,1 \} $
- Hypothesis: $ 0 \leqslant  h_\theta(x) \leqslant 1 $
- Logistic function or Sigmoid function: $ h_\theta(x) = g(z) = g(\dfrac {1}{1 + e^{-z}}) $
  - when $ z=0, e^{0}=1 \Rightarrow g(z)=1/2 $
  - when $ z \to \infty, e^{-\infty} \to 0 \Rightarrow g(z)=1 $
  - when $ z \to -\infty, e^{\infty}\to \infty \Rightarrow g(z)=0 $
- Probability: $ P(y = 0 \| x;\theta) + P(y = 1 \| x ; \theta) = 1$

## Cost Function

- $ Cost(h_\theta(x),y) = -\log(h_\theta(x)), \text{if y = 1} $
- $ Cost(h_\theta(x),y) = -\log(1-h_\theta(x)), \text{if y = 0} $


 ## Gradient Descent

- Repeat: $ \theta_j := \theta_j - \alpha \dfrac{\partial}{\partial \theta_j}J(\theta) $
- Repeat: $ \theta_j := \theta_j - \frac{\alpha}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)} $
- Vectorised: $ \theta := \theta - \frac{\alpha}{m} X^{T} (g(X \theta ) - \vec{y}) $

## Multi class

- $ y \in \lbrace0, 1 ... n\rbrace $
- $ h_\theta^{(0)}(x) = P(y = 0 \| x ; \theta) $
- $ h_\theta^{(1)}(x) = P(y = 1 \| x ; \theta) $
- $ h_\theta^{(n)}(x) = P(y = n \| x ; \theta) $
- $ {prediction} = \max_i( h_\theta ^{(i)}(x) ) $

## Overfitting

2 main options to address the issue of overfitting:

1. Reduce the number of features:
  - Manually select which features to keep.
  - Use a model selection algorithm (studied later in the course).
2. Regularization
  - Keep all the features, but reduce the magnitude of parameters $ \theta_j $
  - Regularization works well when we have a lot of slightly useful features.

## Regularization

- $ \lambda $ lambda, is the **regularization parameter**. It determines how much the costs of our theta parameters are inflated.

### Regularise Linear Regression

#### Gradient descent

- Repeat: $ \theta_0 := \theta_0 - \alpha\ \frac{1}{m}\ \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})x_0^{(i)}  \ j \in  0 $
- Repeat: $ \theta_j := \theta_j - \alpha\ \left[ \left( \frac{1}{m}\ \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)} \right) + \frac{\lambda}{m}\theta_j \right]  \ j \in \lbrace 1,2...n\rbrace $

#### Normal Equation

$ \theta = \left( X^TX + \lambda \cdot L \right)^{-1} X^Ty $

$ \text{where}\ \ L = \begin{bmatrix} 0 & & & & \newline & 1 & & & \newline & & 1 & & \newline & & & \ddots & \newline & & & & 1 \newline\end{bmatrix} $



### Regularise Logistic Regression
