import math

def score(x:float, y:float) -> int:
    CENTER_X = 0
    CENTER_Y = 0

    points = 0

    distance_to_center = math.sqrt(math.pow((CENTER_X-x),2)+math.pow((CENTER_Y-y),2))

    print(distance_to_center)

    if distance_to_center > 10.0:
        points = 0
    elif 10.0 >= distance_to_center > 5.0:
        points = 1
    elif 5.0 >= distance_to_center > 1.0:
        points = 5
    elif 1.0 >= distance_to_center >= 0.0:
        points = 10

    return points
