"""
Author:  Russell Gerhard
Purpose: This script will import all tests for all collections and run them.
"""

import unittest
import concretelisttests
import concretebagtests
import concretesettests
import concretestacktests

# Initialize test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add tests to test suite
# Sets inherit from bags, so their tests run bag tests beforehand
suite.addTests(loader.loadTestsFromModule(concretelisttests))
suite.addTests(loader.loadTestsFromModule(concretesettests))
suite.addTests(loader.loadTestsFromModule(concretestacktests))
#suite.addTests(loader.loadTestsFromModule(concretebagtests))


# Initialize test runner, pass in suite and run
runner = unittest.TextTestRunner(verbosity = 1)
result = runner.run(suite)
