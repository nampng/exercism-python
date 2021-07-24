class Matrix:
    def __init__(self, matrix_string):
        self.num_row = []
        self.num_column = []

        split = matrix_string.split('\n')

        print(f"Split: {split}")

        for i in range(len(split[0].split(' '))):
            self.num_column.append(list())

        for row in split:
            row = row.split(' ')
            row = list(map(int, row))
            self.num_row.append(row)
            for i in range(len(row)):
                self.num_column[i].append(row[i])

        print(f"Row: {self.num_row}")
        print(f"Column: {self.num_column}")
                


    def row(self, index):
        return self.num_row[index - 1]

    def column(self, index):
        return self.num_column[index - 1]
