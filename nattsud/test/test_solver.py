#!/c/Users/David/AppData/Local/Programs/Python/Python37-32/python

import unittest

from nattsud.solver import Solver


class SolverTest(unittest.TestCase):

    def setUp(self):
        self.solver = Solver()

    def test_set_givens_returns_empty_list_if_no_cells_provided(self):
        no_cells = {}
        given_cells = self.solver.set_givens(no_cells)
        self.assertEqual(no_cells, given_cells)
