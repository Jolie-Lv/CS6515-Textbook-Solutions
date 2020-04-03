'''Unit test 2x2 utility functions'''

import unittest
import util

class TestStringMethods(unittest.TestCase):
    '''Testing programmable textbook solutions'''
    def test_problem1(self):
        '''Problem 6.1'''
        def answer(a):
            sums = []
            seqs = []
            for i in a:
                if not sums:
                    sums.append(i)
                    seqs.append([i])
                else:
                    _sum = sums[-1] + i
                    if i > _sum:
                        sums.append(i)
                        seqs.append([i])
                    else:
                        sums.append(sums[-1] + i)
                        seqs.append(seqs[-1] + [i])
            max_in = sums.index(max(sums))
            return sums[max_in], seqs[max_in]

        states = [5, 15, -30, 10, -5, 40, 10,]
        return_val = answer(states)
        self.assertEqual(return_val, (55, [10, -5, 40, 10]))

    def test_problem2(self):
        '''Problem 6.2 - hotels problem'''
        def answer(a):
            s = [0.]
            for i, _ in enumerate(a):
                if s[-1] is a[-1]:
                    return s[1:]
                s.append(min(a[i:], key=lambda x: pow(s[-1] + 200 - x, 2)))
            return s[1:]

        arg = [170, 200, 390, 401, 599, 601]
        self.assertEqual(answer(arg), [200, 401, 601])

    def test_problem10(self):
        '''Problem 6.10 - Counting heads
            Written solution:
            The probability of k heads from n (biased) coin tosses, given biases p_1, ..., p_n can be solved using dynamic programming

            Rather, consider probability for j heads and i tosses. Given any sample input j and i,
            the probability would be one of two possibilities:
            Option 1. that the jth toss was heads, thus achieving j heads on i toss, or
            Option 2. that the jth toss was tails, thus j heads was already achieved prior to the ith toss

            Given the function L(i, j) to represent any given probability,
            L(i, j) = option 1 OR option 2
                    = option 1 + option 2
                    = the ith heads was reached + the ith heads was ALREADY reached
                    = p_i * L(i-1, j-1) + (1 - p_i) * L(i-1, j)

            Also note: if p_i is the bias for heads of that coin, (1 - p_i) is the bias for tails of that coin.
            Code to represent the answer seen below.
        '''
        def answer(n, k, p):
            # Probability Matrix
            pm = [[0] * (k + 1) for _ in range(n + 1)]
            pm[0][0] = 1

            # Big O complexity of N + N**2 == O(N**2)
            for i, _p in enumerate(p):
                pm[i + 1][0] = 1 - _p
            for _j in range(k - 1):
                j = _j + 1
                for i in range(n):
                    if i == 0 or j == 0 or j > i:
                        continue
                    heads_probability = p[i - 1] * pm[i - 1][j - 1]
                    tails_probability = (1 - p[i - 1]) * pm[i - 1][j]
                    util.log('L({}, {}) = {} * {} + {} * {} = {} + {} = {}'.format(i, j, p[i - 1], pm[i - 1][j - 1], (1 - p[i - 1]), pm[i - 1][j], heads_probability, tails_probability, heads_probability + tails_probability))
                    pm[i][j] = heads_probability + tails_probability
            return pm

        ps = [.4, .3, .5, .4, .7, .2, .5, .6]
        self.assertEqual(answer(len(ps), 4, ps), [
            [1, 0, 0, 0, 0],
            [0.6, 0.4, 0, 0, 0],
            [0.7, 0.45999999999999996, 0.12, 0, 0],
            [0.5, 0.58, 0.29, 0.06, 0],
            [0.6, 0.548, 0.40599999999999997, 0.152, 0],
            [0.30000000000000004, 0.5844, 0.5054, 0.3298, 0],
            [0.8, 0.5275200000000001, 0.5212, 0.36492, 0],
            [0.5, 0.6637600000000001, 0.52436, 0.44306, 0],
            [0.4, 0, 0, 0, 0],
        ])

if __name__ == '__main__':
    unittest.main()
