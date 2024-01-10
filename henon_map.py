import matplotlib.pyplot as plt

def henon_map(x, y, a=1.4, b=0.3):
    new_x = 1 - a * x**2 + y
    new_y = b * x
    return new_x, new_y

def generate_henon_map(x0, y0, num_iterations):
    x_values = [x0]
    y_values = [y0]

    for _ in range(num_iterations):
        x, y = henon_map(x_values[-1], y_values[-1])
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

def plot_henon_map(x_values, y_values):
    plt.scatter(x_values, y_values, s=1, c='blue', marker='.')
    plt.title('Hénon Map')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

if __name__ == "__main__":
    # Set initial conditions and number of iterations
    x0, y0 = 0, 0
    num_iterations = 10000

    # Generate Hénon map
    x_values, y_values = generate_henon_map(x0, y0, num_iterations)

    # Plot Hénon map
    plot_henon_map(x_values, y_values)
