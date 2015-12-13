# -*- coding: utf-8 -*-

import unittest
import coverage


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='.')
    cov = coverage.Coverage(omit='*test_*.py')
    cov.start()
    runner.run(suite)
    cov.stop()
    cov.report()