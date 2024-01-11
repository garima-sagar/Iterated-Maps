# Introduction

The basic idea behind iterated maps involves taking an initial value, applying a defined function to it, and then using the result as the new input for the next iteration. This process is repeated indefinitely, generating a sequence of values that represents the system's trajectory through its state space.

Iterated maps can exhibit a variety of behaviors, ranging from stable fixed points and periodic orbits to chaotic and unpredictable trajectories. The study of iterated maps helps researchers understand the underlying dynamics of systems and predict their long-term behavior under different conditions.

______________________________________________________________________________________________________________________________________________

# Logistic Map


The logistic map is a mathematical model that describes the population growth of a species. It is a discrete-time dynamical system, meaning it evolves over time in discrete steps. The formula for the logistic map is given by:
<img width="224" alt="image" src="https://github.com/garima-sagar/Iterated-Maps/assets/145219684/7d51ec7e-8d9b-4127-8e19-831c436dfc11">


## Understanding the Formula

<img width="494" alt="image" src="https://github.com/garima-sagar/Iterated-Maps/assets/145219684/e4846548-1434-47f5-86f3-7287bc4531e2">

## Parameter r 

The parameter  r plays a crucial role in determining the behavior of the logistic map. Different values of r can lead to various dynamic behaviors, including stable equilibrium, periodic oscillations, and chaotic patterns.

- For  0 < r < 1 , the population converges to a stable equilibrium.
- For 1 < r < 3 , the population exhibits periodic oscillations.
- Beyond  r = 3 , the system can enter chaotic behavior, displaying sensitivity to initial conditions.


### Example Usage in Python:

```python
def logistic_map(x0, r, num_iterations):
    result = [x0]
    for _ in range(num_iterations):
        x0 = r * x0 * (1 - x0)
        result.append(x0)
    return result
```


_______________________________________________________________________________________________________________________________________________________

# Hénon Map



The Hénon map is a discrete-time, two-dimensional dynamical system that exhibits chaotic behavior. The map is defined by the following recursive equations:

<img width="629" alt="image" src="https://github.com/garima-sagar/Iterated-Maps/assets/145219684/0848c7ac-f63a-49fa-a35f-d38cb0aaab06">


## Understanding the Equations

<img width="494" alt="image" src="https://github.com/garima-sagar/Iterated-Maps/assets/145219684/d75af5c4-d5c0-4e96-91f8-3202bbf0f0d2">


### Example Usage in Python:

```python
def henon_map(x0, y0, a, b, num_iterations):
    result_x = [x0]
    result_y = [y0]
    for _ in range(num_iterations):
        xn = 1 - a * result_x[-1]**2 + result_y[-1]
        yn = b * result_x[-1]
        result_x.append(xn)
        result_y.append(yn)
    return result_x, result_y
```

