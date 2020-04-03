'''Utility functions for tests'''

from sys import argv

def log(*args, end=None):
    '''logger, use this rather than print to enable silent/verbose'''
    if '--verbose' in argv:
        print(*args, end=end)
    else:
        pass
