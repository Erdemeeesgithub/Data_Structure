class Matrix:
    # TODO: Please write your code here
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self.data = [[0] * cols] * rows

    def _check_same_type(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Operand must be a Matrix")

    def _check_same_shape(self, other):
        self._check_same_type(other)
        if self._rows != other._rows or self._cols != other._cols:
            raise ValueError("Incompatible dimensions")

    def __add__(self, other):
        self._check_same_shape(other)
        out = Matrix(self._rows, self._cols)
        out.data = [
            [self.data[i][j] + other.data[i][j] for j in range(self._cols)]
            for i in range(self._rows)
        ]
        return out

    def __sub__(self, other):
        self._check_same_shape(other)
        out = Matrix(self._rows, self._cols)
        out.data = [
            [self.data[i][j] - other.data[i][j] for j in range(self._cols)]
            for i in range(self._rows)
        ]
        return out

    def __mul__(self, other):
        self._check_same_type(other)
        if self._cols != other._rows:
            raise ValueError("Incompatible dimensions")

        out = Matrix(self._rows, other._cols)
        res = [[0 for _ in range(other._cols)] for _ in range(self._rows)]

        for i in range(self._rows):
            for k in range(self._cols):
                aik = self.data[i][k]
                for j in range(other._cols):
                    res[i][j] += aik * other.data[k][j]

        out.data = res
        return out

    def __truediv__(self, other):
        # Element-wise division (as your tests show) [file:7]
        self._check_same_shape(other)
        out = Matrix(self._rows, self._cols)
        res = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                if other.data[i][j] == 0:
                    raise ValueError("Division by zero")
                row.append(round(self.data[i][j] / other.data[i][j], 1))
            res.append(row)
        out.data = res
        return out

    def __eq__(self, other):
        # Restrict equality to same type [file:10]
        if not isinstance(other, Matrix):
            return False
        return (self._rows == other._rows and
                self._cols == other._cols and
                self.data == other.data)

    def __str__(self):
        return "\n".join(" ".join(str(v) for v in row) for row in self.data)

    def transpose(self):
        # In-place: update data + swap _rows/_cols [file:10]
        transposed = [[self.data[r][c] for r in range(self._rows)]
                    for c in range(self._cols)]
        self.data = transposed
        self._rows, self._cols = self._cols, self._rows

    def scale(self, scalar):
        self.data = [[v * scalar for v in row] for row in self.data]

    def removeRow(self, row_index):
        if row_index < 0 or row_index >= self._rows:
            raise ValueError("Invalid row index")
        self.data.pop(row_index)
        self._rows -= 1

    def removeCol(self, col_index):
        if col_index < 0 or col_index >= self._cols:
            raise ValueError("Invalid col index")
        for r in range(self._rows):
            self.data[r].pop(col_index)
        self._cols -= 1

    def determinant(self):
        if self._rows != self._cols:
            raise ValueError("Determinant only for square matrices")  # [file:10]
        n = self._rows

        a = [list(map(float, row)) for row in self.data]
        det = 1.0
        sign = 1.0

        for i in range(n):
            pivot = i
            for r in range(i, n):
                if abs(a[r][i]) > abs(a[pivot][i]):
                    pivot = r
            if abs(a[pivot][i]) < 1e-12:
                return 0

            if pivot != i:
                a[i], a[pivot] = a[pivot], a[i]
                sign *= -1

            piv = a[i][i]
            det *= piv

            for r in range(i + 1, n):
                factor = a[r][i] / piv
                for c in range(i, n):
                    a[r][c] -= factor * a[i][c]

        det *= sign
        if abs(det - round(det)) < 1e-9:
            return int(round(det))
        return round(det, 1)

    def rank(self):
        a = [list(map(float, row)) for row in self.data]
        m, n = self._rows, self._cols
        rank = 0
        row = 0

        for col in range(n):
            pivot = None
            for r in range(row, m):
                if abs(a[r][col]) > 1e-10:
                    pivot = r
                    break
            if pivot is None:
                continue

            a[row], a[pivot] = a[pivot], a[row]
            piv = a[row][col]

            for c in range(col, n):
                a[row][c] /= piv

            for r in range(m):
                if r != row and abs(a[r][col]) > 1e-10:
                    factor = a[r][col]
                    for c in range(col, n):
                        a[r][c] -= factor * a[row][c]

            rank += 1
            row += 1
            if row == m:
                break

        return rank


def main():
    #
    # Student tests for addition of square matrices(+)
    #
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 1], [1, 1]]

    matrix2 = Matrix(2, 2)
    matrix2.data = [[1, 1], [1, 1]]

    print((matrix1 + matrix2).data == [[2, 2], [2, 2]])  # should print the boolean "True"

    matrix3 = Matrix(2, 2)
    matrix3.data = [[2, 2], [2, 2]]

    matrix4 = Matrix(2, 2)
    matrix4.data = [[-1, -1], [-1, -1]]

    print((matrix3 + matrix4).data == [[1, 1], [1, 1]])  # should print the boolean "True"

    #
    # Student tests for addition of non-square matrices(+)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 1, 1], [1, 1, 1]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[1, 1, 1], [1, 1, 1]]

    print((matrix1 + matrix2).data == [[2, 2, 2], [2, 2, 2]])  # should print the boolean "True"

    matrix3 = Matrix(2, 3)
    matrix3.data = [[2, 2, 2], [2, 2, 2]]

    matrix4 = Matrix(2, 3)
    matrix4.data = [[-1, -1, -1], [-1, -1, -1]]

    print((matrix3 + matrix4).data == [[1, 1, 1], [1, 1, 1]])  # should print the boolean "True"

    #
    # Student tests for subtraction of square matrices(-)
    #
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 1], [1, 1]]

    print((matrix1 - matrix1).data == [[0, 0], [0, 0]])  # should print the boolean "True"

    matrix2 = Matrix(2, 2)
    matrix2.data = [[0, 0], [0, 0]]

    matrix3 = Matrix(2, 2)
    matrix3.data = [[-1, -1], [-1, -1]]

    print((matrix2 - matrix3).data == [[1, 1], [1, 1]])  # should print the boolean "True"

    #
    # Student tests for subtraction of non-square matrices(-)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 1, 1], [1, 1, 1]]

    print((matrix1 - matrix1).data == [[0, 0, 0], [0, 0, 0]])  # should print the boolean "True"

    matrix2 = Matrix(2, 3)
    matrix2.data = [[0, 0, 0], [0, 0, 0]]

    matrix3 = Matrix(2, 3)
    matrix3.data = [[-1, -1, -1], [-1, -1, -1]]

    print((matrix2 - matrix3).data == [[1, 1, 1], [1, 1, 1]])  # should print the boolean "True"

    #
    # Student tests for multiplication (*)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(3, 2)
    matrix2.data = [[1, 2], [3, 4], [5, 6]]

    print((matrix1 * matrix2).data == [[22, 28], [49, 64]])  # should print the boolean "True"

    #
    # Student tests for division (/)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    print((matrix1 / matrix1).data == [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])  # should print the boolean "True"

    #
    # Student tests for equality (==)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 1, 1], [1, 1, 1]]

    print(matrix1 == matrix1)  # should print the boolean "True"

    matrix2 = Matrix(2, 3)
    matrix2.data = [[2, 2, 2], [2, 2, 2]]

    print(matrix1 != matrix2)  # should print the boolean "True"

    #
    # Student tests for stringification (print)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 1, 1], [1, 1, 1]]
    print(matrix1.__str__() == "1 1 1\n1 1 1")  # should print the boolean "True"

    matrix2 = Matrix(2, 3)
    matrix2.data = [[-2, -2, -2], [-2, -2, -2]]
    print(matrix2.__str__() == "-2 -2 -2\n-2 -2 -2")  # should print the boolean "True"

    #
    # Student tests for transpose (m^T)
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix1.transpose()
    print(matrix1.data == [[1, 4], [2, 5], [3, 6]])  # should print the boolean "True"

    matrix2 = Matrix(2, 2)
    matrix2.data = [[-1, -2], [-3, -4]]

    matrix2.transpose()
    print(matrix2.data == [[-1, -3], [-2, -4]])  # should print the boolean "True"

    #
    # Student tests for determinant
    #
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 2], [3, 4]]

    print(matrix1.determinant() == -2)  # should print the boolean "True"

    #
    # Student tests for rank
    #
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 1], [1, 1]]
    print(matrix1.rank() == 1)  # should print the boolean "True"

    matrix2 = Matrix(4, 4)
    matrix2.data = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    print(matrix2.rank() == 4)  # should print the boolean "True"

    #
    # Student tests for scale
    #
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 1], [1, 1]]

    matrix1.scale(2)
    print(matrix1.data == [[2, 2], [2, 2]])  # should print the boolean "True"

    matrix2 = Matrix(2, 3)
    matrix2.data = [[-1, -1, -1], [-1, -1, -1]]

    matrix2.scale(2)
    print(matrix2.data == [[-2, -2, -2], [-2, -2, -2]])  # should print the boolean "True"

    #
    # Student tests for removeRow
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix1.removeRow(1)
    print(matrix1.data == [[1, 2, 3]])  # should print the boolean "True"

    #
    # Student tests for removeCol
    #
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix1.removeCol(2)
    print(matrix1.data == [[1, 2], [4, 5]])  # should print the boolean "True"


if __name__ == '__main__':
    main()