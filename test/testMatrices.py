import unittest
from UnitTesting.shorthand import *
import numpy as np
from FDM.source.matrices import *
from scipy.sparse import csr_matrix, identity

class TestMatrices(unittest.TestCase):
    def testDxx(self):
        desiredMatrix = csr_matrix(np.array([
        [-2., 1., 0., 0., 0., 0., 0., 0., 0.],
        [1., -2., 1., 0., 0., 0., 0., 0., 0.],
        [0., 1., -2., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., -2., 1., 0., 0., 0., 0.],
        [0., 0., 0., 1., -2., 1., 0., 0., 0.],
        [0., 0., 0., 0., 1., -2., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., -2., 1., 0.],
        [0., 0., 0., 0., 0., 0., 1., -2., 1.],
        [0., 0., 0., 0., 0., 0., 0., 1., -2]]))
        actualMatrix = Dxx(3)
        assertSparseArrayEqual(actualMatrix, desiredMatrix)

    def testDyy(self):
        desiredMatrix = csr_matrix(np.array([
        [-2., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., -2., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., -2., 0., 0., 1., 0., 0., 0.],
        [1., 0., 0., -2., 0., 0., 1., 0., 0.],
        [0., 1., 0., 0., -2., 0., 0., 1., 0.],
        [0., 0., 1., 0., 0., -2., 0., 0., 1.],
        [0., 0., 0., 1., 0., 0., -2., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., -2., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., -2]]))
        actualMatrix = Dyy(3)
        assertSparseArrayEqual(actualMatrix, desiredMatrix)

    def testColumnToGrid(self):
        gridDimension = 3
        grid = np.array(
                [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
        desiredColumn = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
        actualColumn = gridToColumn(grid)
        assertArrayEqual(actualColumn, desiredColumn)

    def testGridToColumn(self):
        columnDimension = 9
        column = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        desiredGrid = np.array(
                [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
        actualGrid = columnToGrid(column)
        assertArrayEqual(actualGrid, desiredGrid)

    def testLaplacian(self):
        Nx = 3
        desiredMatrix = csr_matrix(np.array([
        [-4., 1., 0., 1., 0., 0., 0., 0., 0.],
        [1., -4., 1., 0., 1., 0., 0., 0., 0.],
        [0., 1., -4., 0., 0., 1., 0., 0., 0.],
        [1., 0., 0., -4., 1., 0., 1., 0., 0.],
        [0., 1., 0., 1., -4., 1., 0., 1., 0.],
        [0., 0., 1., 0., 1., -4., 0., 0., 1.],
        [0., 0., 0., 1., 0., 0., -4., 1., 0.],
        [0., 0., 0., 0., 1., 0., 1., -4., 1.],
        [0., 0., 0., 0., 0., 1., 0., 1., -4]]))
        actualMatrix = Laplacian(Nx)
        assertSparseArrayEqual(actualMatrix, desiredMatrix)

