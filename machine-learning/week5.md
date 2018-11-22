<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {inlineMath: [["$","$"],["\\(","\\)"]]}
  });
</script>
<script async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# Week 5: Neural Networks - Back-propagation

## Cost Function

Common variables
- `L` = total number of layers in the network
- $ s_l $ = number of units (not counting bias unit) in layer `l`
- `K` = number of output units/classes

Classification types

- **binary** $ y = 0 \text{ or } 1 $ with 1 output unit
- **multi-class** $ y \epsilon R^K $ with K output units

Cost function for neural networks:

$ J(\Theta) = $

$ -\frac{1}{m} \sum_{i=1}^m \sum_{k=1}^K [ $

$ \log ((h_\Theta (x^{(i)}))_k) * y^{(i)}_k + $

$ \log (1 - (h_\Theta(x^{(i)}))_k)) * (1 - y^{(i)}_k)] $ 

$ + \frac{\lambda}{2m}\sum_{l=1}^{L-1} \sum_{i=1}^{s_l} \sum_{j=1}^{s_{l+1}} ( \Theta_{j,i}^{(l)})^2 $

- 1st part: additional nested summation that loops through the number of output nodes
  - **double sum** adds up the logistic regression costs calculated for each cell in the output layer
- 2nd part: account for multiple theta matrices
  - **triple sum** adds up the squares of all the individual Θs in the entire network

## Gradient computation - Forward propagation

- $ a^{(1)} = x ​$
- $ z^{(2)} = \Theta^{(1)}a^{(1)} $
- $ a^{(2)} = g(z^{(2)}) $ (add $a_0^{(2)}$)
- $ z^{(3)} = \Theta^{(2)}a^{(2)} $
- $ a^{(3)} = g(z^{(3)}) $ (add $a_0^{(3)}$)
- $ z^{(4)} = \Theta^{(3)}a^{(3)} $
- $ a^{(4)} = h_\Theta(x) = g(z^{(4)}) $

## Gradient computation - Back propagation

Let $ \delta_j^{(l)} $ be the error of node `j` in layer `l`

- $ \delta_j^{(4)} = a_j^{(4)} - y_j $
- $ \delta^{(3)} = (\Theta^{(3)})^T \delta^{(4)}.*g'(z^{(3)}) $
- $ \delta^{(2)} = (\Theta^{(2)})^T \delta^{(3)}.*g'(z^{(2)}) $

## Back-Propagation Algorithm

**Back-propagation** is neural-network terminology for minimizing our cost function.

Example with 2 training examples $ (x^{(1)}, y^{(1)})  $ and  $ (x^{(2)}, y^{(2)})  $

- FP using $ x^{(1)} $ followed by BP using $y^{(1)} $
- FP using $ x^{(2)} $ followed by BP using $y^{(2)} $

Minimise cost function for neural network:

$ \dfrac {\partial} {\partial\Theta^{(l)}_{ij}} J(\Theta) = $

$ D^{(l)}_{ij} $ 

Forward propagation: $ \delta_2^{(2)} = \Theta_{12}^{(2)}\delta_1^{(3)} $

## Matlab

- `optTheta = fminunc(@costFunction, initialTheta, options)`
- `function [jVal, gradient] = costFunction(theta)`
- `DVec = [D1(:); D2(:); D3(:)];`
- Back-propagation
  - `D1 = reshape(DVec(1:110), 10, 11);`
  - `D2 = reshape(DVec(111:220), 10, 11);`
  - `D3 = reshape(DVec(221:231), 1, 11);` 

Example

- Create 3 seperate matrices

  - `D1 = ones(10, 11)`
  - `D2 = 2*ones(10,11)`
  - `D3 = 3*ones(1,11)`

- Combine all the 3 matrices

  - `DVec = [D1(:); D2(:); D3(:)]; # a very long vector` 

- Reshape into 3 seperate matrices

  - `reshape(DVec(1:110), 10, 11)`
  - `reshape(DVec(111:220), 10, 11)`
  - `reshape(thetaVec(221:231), 1, 11)`

  ​