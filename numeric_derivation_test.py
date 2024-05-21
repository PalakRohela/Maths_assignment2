from numeric_derivation import derive

# List of test cases: (function, point, expected_derivative)
tests = [
    (lambda x: x, 2, 1),         # f(x) = x, f'(x) = 1
    (lambda x: 1, 2, 0),         # f(x) = 1, f'(x) = 0
    (lambda x: x**2, 2, 4),      # f(x) = x^2, f'(x) = 2x => f'(2) = 4
    (lambda x: x**3, 2, 12),     # f(x) = x^3, f'(x) = 3x^2 => f'(2) = 12
    (lambda x: x**4, 2, 32),     # f(x) = x^4, f'(x) = 4x^3 => f'(2) = 32
    (lambda x: x**2, 1, 2),      # f(x) = x^2, f'(x) = 2x => f'(1) = 2
    (lambda x: x**3, 1, 3),      # f(x) = x^3, f'(x) = 3x^2 => f'(1) = 3
    (lambda x: 3-4*x**2, 1, -8), # f(x) = 3 - 4x^2, f'(x) = -8x => f'(1) = -8
    (lambda x: 3-4*x**2, 2, -16),# f(x) = 3 - 4x^2, f'(x) = -8x => f'(2) = -16
]

# Function to run tests
def t_derive(n):
    for f, x, expected in tests[:n]:
        actual = derive(f, x)
        print(f"Testing f at x={x}: expected={expected}, actual={actual}")
        assert abs(actual - expected) < .01, "Expected %s, got %s; %s" % (expected, actual, f)

# Individual test functions
def test_derive():
    t_derive(1)

def test_derive2():
    t_derive(2)

def test_derive3():
    t_derive(len(tests))

# To test the results locally
if __name__ == "__main__":
    test_derive()
    test_derive2()
    test_derive3()
