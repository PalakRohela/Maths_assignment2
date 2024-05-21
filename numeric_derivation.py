def derive(f, x, h=0.001):
    """
    Calculate the numerical derivative of function f at point x.

    Args:
    f (function): The function to differentiate.
    x (float): The point at which to evaluate the derivative.
    h (float): A small step size. Default is 0.001.

    Returns:
    float: The numerical derivative of f at point x.
    """
    print(f"Calculating derivative for f at x={x} with h={h}")  # Add this line
    result = (f(x + h) - f(x - h)) / (2 * h)
    print(f"f(x + h)={f(x + h)}, f(x - h)={f(x - h)}, result={result}")  # Add this line
    return result
