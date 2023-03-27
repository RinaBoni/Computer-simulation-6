class Simplex:
    def __init__(self, source):
        # source - симплекс таблица без базисных переменных
        self.m = len(source)
        self.n = len(source[0])
        # симплекс таблица
        self.table = [[0 for i in range(self.n + self.m - 1)] for j in range(self.m)]
        # список базисных переменных
        self.basis = []

        for i in range(self.m):
            for j in range(len(self.table[0])):
                if j < self.n:
                    self.table[i][j] = source[i][j]
                else:
                    self.table[i][j] = 0
            # выставляем коэффициент 1 перед базисной переменной в строке
            if (self.n + i) < len(self.table[0]):
                self.table[i][self.n + i] = 1
                self.basis.append(self.n + i)

        self.n = len(self.table[0])

    def is_it_end(self):
        flag = True
        for j in range(1, self.n):
            if self.table[self.m - 1][j] < 0:
                flag = False
                break
        return flag

    def find_main_col(self):
        main_col = 1
        for j in range(2, self.n):
            if self.table[self.m - 1][j] < self.table[self.m - 1][main_col]:
                main_col = j
        return main_col

    def find_main_row(self, main_col):
        main_row = 0
        for i in range(self.m - 1):
            if self.table[i][main_col] > 0:
                main_row = i
                break
        for i in range(main_row + 1, self.m - 1):
            if self.table[i][main_col] > 0 and self.table[i][0] / self.table[i][main_col] < self.table[main_row][0] / self.table[main_row][main_col]:
                main_row = i
        return main_row

    def calculate(self, result):
        while self.is_it_end() is False:
            main_col = self.find_main_col()
            main_row = self.find_main_row(main_col)
            self.basis[main_row] = main_col

            new_table = [[0 for i in range(self.n)] for j in range(self.m)]

            for j in range(self.n):
                new_table[main_row][j] = self.table[main_row][j] / self.table[main_row][main_col]

            for i in range(self.m):
                if i == main_row:
                    continue
                for j in range(self.n):
                    new_table[i][j] = self.table[i][j] - self.table[i][main_col] * new_table[main_row][j]

            self.table = new_table

        for i in range(len(result)):
            try:
                k = self.basis.index(i + 1)
            except:
                k = -1

            if k != -1:
                result[i] = self.table[k][0]
            else:
                result[i] = 0

        return self.table, result


