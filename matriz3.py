def determinante3x3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def inversa3x3(m):
    det = determinante3x3(m)
    if det == 0:
        return None
    cof = [[0] * 3 for _ in range(3)]
    cof[0][0] = (m[1][1] * m[2][2] - m[1][2] * m[2][1])
    cof[0][1] = -(m[1][0] * m[2][2] - m[1][2] * m[2][0])
    cof[0][2] = (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    cof[1][0] = -(m[0][1] * m[2][2] - m[0][2] * m[2][1])
    cof[1][1] = (m[0][0] * m[2][2] - m[0][2] * m[2][0])
    cof[1][2] = -(m[0][0] * m[2][1] - m[0][1] * m[2][0])
    cof[2][0] = (m[0][1] * m[1][2] - m[0][2] * m[1][1])
    cof[2][1] = -(m[0][0] * m[1][2] - m[0][2] * m[1][0])
    cof[2][2] = (m[0][0] * m[1][1] - m[0][1] * m[1][0])
    adj = [[cof[j][i] for j in range(3)] for i in range(3)]
    inv = [[adj[i][j] / det for j in range(3)] for i in range(3)]
    return inv


class Matriz3x3:
    def __init__(self):
        pass

