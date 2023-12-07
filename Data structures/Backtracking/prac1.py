def issafe(Mat, R, C):
    for i in range(R):  # check the columns
        if Mat[i][C] == 1:
            return False

    (i, j) = (R, C)  # check the '\' diagonal
    while i >= 0 and j >= 0:
        if Mat[i][j] == 1:
            return False
        i = i - 1
        j = j - 1

    (i, j) = (R, C)  # check the '/' diagonal
    while i >= 0 and j < len(Mat):
        if Mat[i][j] == 1:
            return False
        i = i - 1
        j = j + 1

    return True


def print_solution(mat):
    print(mat)
    print('\n')


def NQueen(Mat, R):
    if R == len(Mat):
        print_solution(Mat)


    for i in range(len(Mat)):
        if issafe(Mat, R, i):
            Mat[R][i] = 1
            NQueen(Mat, R + 1)
            Mat[R][i] = '-'  # backtrack and remove the inserted value


if __name__ == "__main__":
    n = 8
    mat = [['-' for i in range(n)] for j in range(n)]
    # print(mat)
    NQueen(mat, 0)
