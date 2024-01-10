import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x, num_iterations):
    orbit = [x]
    for _ in range(num_iterations):
        x = r * x * (1 - x)
        orbit.append(x)
    return orbit

def generate_feigenbaum_fractal(r_min, r_max, num_points, num_iterations):
    x_values = []
    r_values = np.linspace(r_min, r_max, num_points)

    for r in r_values:
        orbit = logistic_map(r, 0.5, num_iterations)[-100:]
        x_values.extend([(r, x) for x in orbit])

    return np.array(x_values)

def plot_feigenbaum_fractal(data):
    plt.scatter(data[:, 0], data[:, 1], c=data[:, 1], cmap='viridis', marker='.', s=1)
    plt.title('Feigenbaum Fractal')
    plt.xlabel('r')
    plt.ylabel('Population')
    plt.colorbar(label='Color by Population')
    plt.show()

if __name__ == "__main__":
    # Set parameters for the Feigenbaum fractal
    r_min = 2.8
    r_max = 4.0
    num_points = 500
    num_iterations = 1000

    # Generate Feigenbaum fractal data
    fractal_data = generate_feigenbaum_fractal(r_min, r_max, num_points, num_iterations)

    # Plot colorful Feigenbaum fractal
    plot_feigenbaum_fractal(fractal_data)
