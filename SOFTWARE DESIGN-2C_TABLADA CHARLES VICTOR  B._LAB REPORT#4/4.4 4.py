class SummationSolver():
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self._max_len = len(c)
        self._count = 0

    def _t2i(self, text, lookup):
        total = 0
        length = len(text)
        for i in range(length):
            total += int(lookup[text[i]]) * 10 ** (length - i - 1)

        return total

    def summation_check(self, a, b, c, U):

        if self._t2i(a, U) + self._t2i(b, U) == self._t2i(c, U):
            self._count += 1
            print(
                f'One solution is: {self._t2i(a, U)} + {self._t2i(b, U)} = {self._t2i(c, U)}.  Check:{self._t2i(a, U) + self._t2i(b, U)}')
            print('Dictionary is :', U)
            print('\n')
            return True
        else:
            return False

    def _solver_r(self, a, b, c, S, index, U, nums):
        if index >= len(S):

            return self.summation_check(a, b, c, U)
        elif S[index] in U:
            return self._solver_r(a, b, c, S, index + 1, U, nums)
        else:
            for number in nums.copy():
                U[S[index]] = number
                nums.remove(number)
                ans = self._solver_r(a, b, c, S, index + 1, U, nums)
                nums.add(number)
                del U[S[index]]

    def solve(self):
        U = {}
        nums = set(range(10))
        S = list(self._a) + list(self._b) + list(self._c)
        self._count = 0

        self._solver_r(self._a, self._b, self._c, S, 0, U, nums)

        if self._count == 0:
            print('Sorry, no solution found! :(')

        else:
            print(f'There are a total of {self._count} solutions')


# a = SummationSolver('pot', 'pan', 'bib')
# a = SummationSolver('boy', 'girl', 'babys')
a = SummationSolver('boy', 'girl', 'babysda')
a.solve()
