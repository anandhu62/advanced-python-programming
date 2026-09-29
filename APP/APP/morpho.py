matrix = [
    [1, 0, 1, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 0, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1, 0, 1]
]

kernel = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]

for i in range(7):
    for j in range(7):

        match = True

        for x in range(3):
            for y in range(3):

                if matrix[i + x][j + y] != kernel[x][y]:
                    match = False
                    break

            if not match:
                break

        if match:
            print("Kernel matched at:", i, j)