class Collatz:

    def __init__(self, n):
        self.n = n
        self.array = []
        self.collatz()

    def collatz(self):
        while not self.n == 4:
            self.array.append(self.n)
            self.n = self.apply_rules(self.n)
        self.array.extend([4, 2, 1])

    def apply_rules(self, n):
        """
        :param n: int number
        :return: rules:
        { f(n + 1) = n / 2, n is even
        { f(n + 1) = 3*n + 1, n is odd
        """
        return int(n / 2) if n % 2 == 0 else int(3 * n + 1)


def is_int(value):
    try:
        int(value)
        return True
    except:
        return False


def main():
    while True:
        ui = input("Type int / quit / press 'enter': ")
        if is_int(ui):
            c = Collatz(int(ui))
            print(f"{c.array}\nCollatz converged, steps made {len(c.array) - 1}")
        elif ui == "quit":
            break
        else:
            for i in range(10 ** 999):
                c = Collatz(i + 1)
                print(f"{i + 1}\nCollatz converged, steps made {len(c.array) - 1}")


if __name__ == "__main__":
    main()
