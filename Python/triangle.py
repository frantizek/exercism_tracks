
def is_triangle(sides: list):
    if sum(sides) > 0 and (sides[0] + sides[1] >= sides[2] and
                           sides[1] + sides[2] >= sides[0] and
                           sides[0] + sides[2] >= sides[1]):
        return True
    return False


def equilateral(sides: list):
    if is_triangle(sides):
        if sides.count(sides[0]) == 3:
            return True
    return False


def isosceles(sides: list):
    if is_triangle(sides):
        if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
            return True
    return False


def scalene(sides: list):
    if is_triangle(sides):
        if sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
            return True
    return False
