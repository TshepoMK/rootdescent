class Integration:
    def trapezoidal_rule(self, func, a, b, n):
        """
        Approximate the definite integral of a function using the trapezoidal rule.

        Parameters:
        func (function): The function to integrate.
        a (float): The lower bound of the integration interval.
        b (float): The upper bound of the integration interval.
        n (int): The number of subintervals to use for the approximation.

        Returns:
        float: The approximated integral value.
        """
        h = (b - a) / n
        result = (func(a) + func(b)) / 2

        for i in range(1, n):
            result += func(a + i * h)

        return result * h

    def simpsons_13_rule(self, func, a, b, n):
        """
        Approximate the definite integral of a function using Simpson's 1/3 rule.

        Parameters:
        func (function): The function to integrate.
        a (float): The lower bound of the integration interval.
        b (float): The upper bound of the integration interval.
        n (int): The number of subintervals to use for the approximation (must be even).

        Returns:
        float: The approximated integral value.

        Raises:
        ValueError: If n is not an even integer.
        """
        if n % 2 != 0:
            raise ValueError("n must be an even integer for Simpson's 1/3 rule.")

        h = (b - a) / n
        result = func(a) + func(b)

        for i in range(1, n, 2):
            result += 4 * func(a + i * h)

        for i in range(2, n - 1, 2):
            result += 2 * func(a + i * h)

        return result * h / 3

    def simpsons_38_rule(self, func, a, b, n):
        """
        Approximate the definite integral of a function using Simpson's 3/8 rule.

        Parameters:
        func (function): The function to integrate.
        a (float): The lower bound of the integration interval.
        b (float): The upper bound of the integration interval.
        n (int): The number of subintervals to use for the approximation (must be a multiple of 3).

        Returns:
        float: The approximated integral value.

        Raises:
        ValueError: If n is not a multiple of 3.
        """
        if n % 3 != 0:
            raise ValueError("n must be a multiple of 3 for Simpson's 3/8 rule.")

        h = (b - a) / n
        result = func(a) + func(b)

        for i in range(1, n, 3):
            result += 3 * (func(a + i * h) + func(a + (i + 1) * h))

        for i in range(3, n - 2, 3):
            result += 2 * func(a + i * h)

        return result * 3 * h / 8
