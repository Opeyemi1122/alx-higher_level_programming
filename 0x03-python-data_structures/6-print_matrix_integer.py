#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()


if __name__ == "__main__":
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
