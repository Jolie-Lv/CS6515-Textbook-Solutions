'''Unit test 2x2 utility functions'''

import unittest

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

if __name__ == '__main__':
    unittest.main()
