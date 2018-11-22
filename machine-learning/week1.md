<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {inlineMath: [["$","$"],["\\(","\\)"]]}
  });
</script>
<script async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# Week 1: Cost function and Gradient Descent

## Introduction

> A computer is said to learn from **experience E** with respect to some **task T** and some **performance measure P**, if its performance on T as measured by P, improved with experience E.

- Supervised learning
  - regression (continuous value)
  - classification (discrete value)
- Unsupervised learning
  - clustering

## Model representation

- Supervised learning
- Regression problem

## Cost function

- Parameters $ \theta $
- Inputs or features $ x $
- Hypothesis $ h_\theta(x) $
- Equation: $ h_\theta = \theta_0 + \theta_1x $

## Cost function intuition

Cost function: $ J(\theta_1) = \dfrac {1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2 $

## Gradient descent

- Minimise $ J(\theta_0, \theta_1) $
- Steps for each gradient descent $ \alpha $
- $ \theta_j := \theta_j - \alpha \dfrac \alpha {\delta}{\delta \theta_j} J(\theta_0, \theta_1) $

## Gradient descent intuition

- if $ \alpha $ is too small, gradient descent can be slow
- If $ \alpha $ is too large, gradeint descent can overshoot the minimum or diverge
- As we approach the local minimum, the gradient descent will automatically take smaller steps

## Linear algebra

- Matrix dimension: row X columns
- Vector: `n X 1` matrix
- `A + B = C`, where `A`, `B` and `C` have same dimensions
- Scalar multiplication has `scalar X A`
- Matrix multiplication `p by q * q by r` where first matrix's **column** = second matrix's **row** is same
- Matrix-matrix multiplication `A X B = C`
  - `A` has `m x n` dimension
  - `B` has `n x b` dimension
  - `C` has `m x o` dimension
- `A x B ≠ B x A` not commutative, unless `B` is an identity matrix
- $ AA^{-1} = A^{-1}A = I$
