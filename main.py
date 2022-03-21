from fractions import Fraction

matrix = [
    [1, 1, 0, 2, 1, 0, 0, 0],
    [2, -1, 1, -1, 0, 1, 0, 0],
    [3, 3, 2, -2, 0, 0, 1, 0],
    [1, 2, 1, 0, 0, 0, 0, 1]
]

def format_value(s):
    s = str(Fraction(s).limit_denominator())
    l = 7 - len(s)
    return " " * l + s

def pprint_matrix():
    for row in matrix:
        for index, item in enumerate(row):
            if abs(item) < 0.0001:
                row[index] = 0
    for row in matrix:
        print('|', end="")
        for index, item in enumerate(row):
            print(format_value(item), end="")
            if index == 3:
                print(' |', end="")
        print('|')
    print()

def m_by_constant(constant, rownum):
    print("R" + str(rownum) + " = " + str(constant) + " * r" + str(rownum))
    rownum -= 1
    for index, item in enumerate(matrix[rownum]):
        matrix[rownum][index] = item * constant
    pprint_matrix()

def m_and_add(constant, baserow, addrow):
    print("R" + str(baserow) + " = r" + str(baserow) + " + (" + str(Fraction(constant).limit_denominator()) + ")r" + str(addrow))
    baserow -= 1
    addrow -= 1
    for index, item in enumerate(matrix[addrow]):
        item = item * constant
        matrix[baserow][index] += item
    pprint_matrix()



pprint_matrix()
m_and_add(-3, 3, 1) #R3 = r3 - 3r1
m_and_add(-1, 2, 4) #R2 = r2 - r4
m_and_add(-1, 1, 2)
m_and_add(1/3, 2, 1)
m_and_add(-1, 4, 2) #R4 = r4 - r2
m_and_add(-11/12, 4, 1)
m_and_add(-2, 3, 4)
m_by_constant(-2/5, 3)
m_and_add(-3, 1, 3)
m_by_constant(1/4, 1)
m_and_add(5/3, 2, 1)
m_and_add(11/4, 4, 3)
