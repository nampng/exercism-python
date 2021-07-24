class Garden:

    plants_dict = {
        'V' : 'Violets',
        'R' : 'Radishes',
        'C' : 'Clover',
        'G' : 'Grass'
    }

    students = {
        'Alice' : 0,
        'Bob': 1,
        'Charlie' : 2,
        'David' : 3,
        'Eve' : 4,
        'Fred' : 5,
        'Ginny' : 6,
        'Harriet' : 7,
        'Ileana' : 8,
        'Joseph' : 9,
        'Kincaid' : 10,
        'Larry' : 11
    }

    def __init__(self, diagram, students=None):
        diagram = diagram.split()

        if students:
            self.FillStudentsDict(students)

        plant_rows = [ [char for char in diagram[0]], [char for char in diagram[1]] ]
        print(plant_rows)

        i  = 0
        for student in self.students:
            self.students[student] = [plant_rows[0][i], plant_rows[0][i + 1], plant_rows[1][i], plant_rows[1][i + 1]]
            self.students[student] = list(map(self.plants_dict.get, self.students[student]))
            i += 2
            if i > len(plant_rows[0]) - 1:
                print("i is too large, breaking...")
                break

    def plants(self, name):
        return self.students[name]

    def FillStudentsDict(self, students):
        students.sort()
        self.students = {students[i] : i for i in range(len(students)) }

        

