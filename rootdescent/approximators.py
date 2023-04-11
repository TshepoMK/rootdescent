class RootApproximator:
    def regula_falsi(self, func, a, b, error, display_guesses=False):
        """
        Approximate the root of a given function using the Regula Falsi method.

        Parameters:
        func (function): The function for which to find the root.
        a (float): The lower bound of the interval containing the root.
        b (float): The upper bound of the interval containing the root.
        error (float): The desired error tolerance for the approximation.
        display_guesses (bool, optional): If True, prints the guesses at each iteration. Defaults to False.

        Returns:
        float: The approximated root of the function.
        """
        if func(a) * func(b) >= 0:
            raise ValueError("Initial guesses do not bracket the root.")

        c = a
        num_guesses = 0
        while abs(func(c)) > error:
            num_guesses += 1
            c = (a * func(b) - b * func(a)) / (func(b) - func(a))
            if func(c) * func(a) < 0:
                b = c
            else:
                a = c

            if display_guesses:
                print(f"Guess {num_guesses}: {c}")

        return c

    def fixed_point_iteration(self, func, x0, error, display_guesses=False):
        """
        Approximate the fixed point of a given function using fixed-point iteration.

        Parameters:
        func (function): The function for which to find the fixed point.
        x0 (float): The initial guess for the fixed point.
        error (float): The desired error tolerance for the approximation.
        display_guesses (bool, optional): If True, prints the guesses at each iteration. Defaults to False.

        Returns:
        float: The approximated fixed point of the function.
        """
        x1 = func(x0)
        num_guesses = 0
        while abs(x1 - x0) > error:
            num_guesses += 1
            x0 = x1
            x1 = func(x0)

            if display_guesses:
                print(f"Guess {num_guesses}: {x1}")

        return x1

    def bisection_method(self, func, a, b, error, display_guesses=False):
        """
        Approximate the root of a given function using the Bisection method.

        Parameters:
        func (function): The function for which to find the root.
        a (float): The lower bound of the interval containing the root.
        b (float): The upper bound of the interval containing the root.
        error (float): The desired error tolerance for the approximation.
        display_guesses (bool, optional): If True, prints the guesses at each iteration. Defaults to False.

        Returns:
        float: The approximated root of the function.
        """
        if func(a) * func(b) >= 0:
            raise ValueError("Initial guesses do not bracket the root.")

        c = (a + b) / 2
        num_guesses = 0
        while abs(func(c)) > error:
            num_guesses += 1
            if func(c) * func(a) < 0:
                b = c
            else:
                a = c
            c = (a + b) / 2

            if display_guesses:
                print(f"Guess {num_guesses}: {c}")

        return c

    def newton_raphson(self, func, dfunc, x0, error, display_guesses=False):
        """
        Approximate the root of a given function using the Newton-Raphson method.

        Parameters:
        func (function): The function for which to find the root.
        dfunc (function): The derivative of the function for which to find the root.
        x0 (float): The initial guess for the root.
        error (float): The desired error tolerance for the approximation.
        display_guesses (bool, optional): If True, prints the guesses at each iteration. Defaults to False.

        Returns:
        float: The approximated root of the function.
        """
        x1 = x0 - func(x0) / dfunc(x0)
        num_guesses = 0
        while abs(x1 - x0) > error:
            num_guesses += 1
            x0 = x1
            x1 = x0 - func(x0) / dfunc(x0)

            if display_guesses:
                print(f"Guess {num_guesses}: {x1}")

        return x1

    def secant_method(self, func, x0, x1, error, display_guesses=False):
        """
        Approximate the root of a given function using the Secant method.

        Parameters:
        func (function): The function for which to find the root.
        x0 (float): The first initial guess for the root.
        x1 (float): The second initial guess for the root.
        error (float): The desired error tolerance for the approximation.
        display_guesses (bool, optional): If True, prints the guesses at each iteration. Defaults to False.

        Returns:
        float: The approximated root of the function.
        """
        num_guesses = 0
        while abs(x1 - x0) > error:
            num_guesses += 1
            x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
            x0 = x1
            x1 = x2

            if display_guesses:
                print(f"Guess {num_guesses}: {x1}")

        return x1
