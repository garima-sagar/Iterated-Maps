# Introduction

The basic idea behind iterated maps involves taking an initial value, applying a defined function to it, and then using the result as the new input for the next iteration. This process is repeated indefinitely, generating a sequence of values that represents the system's trajectory through its state space.

Iterated maps can exhibit a variety of behaviors, ranging from stable fixed points and periodic orbits to chaotic and unpredictable trajectories. The study of iterated maps helps researchers understand the underlying dynamics of systems and predict their long-term behavior under different conditions.

______________________________________________________________________________________________________________________________________________

# Logistic Map

The logistic map is a mathematical model that describes the population growth of a species. It is a discrete-time dynamical system, meaning it evolves over time in discrete steps. The formula for the logistic map is given by:
x 
n+1
​
 =r⋅x 
n
​
 ⋅(1−x 
n
​
 )

\[ x_{n+1} = r \cdot x_n \cdot (1 - x_n) \]

where:
- \( x_n \) is the population at time \( n \),
- \( r \) is the growth rate parameter.

## Understanding the Formula

1. **Population Update Rule:** The term \( r \cdot x_n \) represents the population's growth potential, where \( r \) is the growth rate and \( x_n \) is the current population.

2. **Logistic Term (1 - \( x_n \)):** This term introduces a self-limiting factor, as it models the resource constraints or competition for resources within the population. It ensures that the population cannot exceed 1.

3. **Iteration:** The formula is iteratively applied, meaning the population at each time step is used as the input for the next iteration, leading to a sequence of population values.

## Parameter \( r \)

The parameter \( r \) plays a crucial role in determining the behavior of the logistic map. Different values of \( r \) can lead to various dynamic behaviors, including stable equilibrium, periodic oscillations, and chaotic patterns.

- For \( 0 < r < 1 \), the population converges to a stable equilibrium.
- For \( 1 < r < 3 \), the population exhibits periodic oscillations.
- Beyond \( r = 3 \), the system can enter chaotic behavior, displaying sensitivity to initial conditions.


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

\[ x_{n+1} = 1 - a \cdot x_n^2 + y_n \]
\[ y_{n+1} = b \cdot x_n \]

where:
- \( (x_n, y_n) \) represents the state of the system at time \( n \),
- \( a \) and \( b \) are parameters that determine the map's behavior.

## Understanding the Equations

1. **Quadratic Term \(x_{n+1} = 1 - a \cdot x_n^2\):**
   - The term \(1 - a \cdot x_n^2\) introduces a quadratic dependence on the current state \(x_n\).
   - It creates a nonlinear effect, contributing to the chaotic behavior of the system.

2. **Linear Term \(y_{n+1} = b \cdot x_n\):**
   - The term \(b \cdot x_n\) represents a linear coupling between \(x\) and \(y\).
   - It provides a simple but effective way to link the evolution of both variables.

3. **Parameter Tuning:**
   - The parameters \(a\) and \(b\) play a crucial role in determining the dynamics of the Hénon map.
   - Different values of \(a\) and \(b\) lead to various behaviors, including stable points, periodic orbits, and chaotic trajectories.



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

