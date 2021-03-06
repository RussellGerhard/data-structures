"""
Author:  Russell Gerhard
Purpose: This script will import all tests for all collections and run them.
"""

import unittest
import concretelisttests
import concretebagtests
import concretesettests
import concretestacktests
import concretequeuetests
import concreteBSTtests
import concreteheaptests
import concretedicttest

# Initialize test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add tests to test suite
# Sets inherit from bags, so their tests run bag tests beforehand
suite.addTests(loader.loadTestsFromModule(concretelisttests))
suite.addTests(loader.loadTestsFromModule(concretebagtests))
suite.addTests(loader.loadTestsFromModule(concretesettests))
suite.addTests(loader.loadTestsFromModule(concretestacktests))
suite.addTests(loader.loadTestsFromModule(concretequeuetests))
suite.addTests(loader.loadTestsFromModule(concreteBSTtests))
suite.addTests(loader.loadTestsFromModule(concreteheaptests))
suite.addTests(loader.loadTestsFromModule(concretedicttest))

# Initialize test runner, pass in suite and run
runner = unittest.TextTestRunner(verbosity = 1)
result = runner.run(suite)
