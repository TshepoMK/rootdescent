# RootDescent

rootdescent is a Python package for numerical analysis, offering tools for approximating roots and performing numerical integration.

## Features

rootdescent currently includes the following classes and methods:

### RootApproximator

This class provides methods for finding the roots of functions using various numerical approximation techniques. The available methods are:

- Bisection method (`bisection`)
- Fixed-point iteration (`fixed_point_iteration`)
- Regula Falsi method (`regula_falsi`)
- Newton-Raphson method (`newton_raphson`)
- Secant method (`secant`)

### Integration

This class provides methods for approximating definite integrals of functions using various numerical integration techniques. The available methods are:

- Trapezoidal rule (`trapezoidal_rule`)
- Simpson's 1/3 rule (`simpsons_13_rule`)
- Simpson's 3/8 rule (`simpsons_38_rule`)

## Usage

Here's an example of how to use rootdescent to approximate the root of a function and the integral of another function:

```python
from rootdescent import RootApproximator, Integration

# Define the functions for root approximation and integration
def f(x):
    return x**2 - 4

def g(x):
    return x**3 - 6 * x**2 + 4 * x + 12

# Initialize the RootApproximator and Integration classes
root_approx = RootApproximator()
integration = Integration()

# Approximate the root of f(x) using the bisection method
root = root_approx.bisection(f, 0, 4, error=1e-6, display_iterations=False)
print(f"Root: {root}")

# Approximate the integral of g(x) using the trapezoidal rule
integral = integration.trapezoidal_rule(g, 1, 4, n=100)
print(f"Integral: {integral}")

## Installation

To install RootDescent, download the package and run the following command in your terminal or command prompt:





Replace my_function with your desired function and adjust the initial guesses and error according to your needs.

Contributing
Contributions are welcome! Please submit pull requests with bug fixes or new features.

License
This project is released under the MIT License.

