def spiral_matrix(size: int):
    if size < 0 or size > 10:
        return []
    else:
        matrix = [["_" for _ in range(size)] for _ in range(size)]
        i = 1
        while i < pow(size, 2)+1:
            for j in range(size):
                for k in range(size):
                    matrix[j][k] = i
                    i += 1

        return matrix


print(spiral_matrix(4))