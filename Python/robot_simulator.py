# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates: tuple[int, int] = x_pos, y_pos

    def move(self, movements: str):
        if movements is not None and len(movements) > 0:
            for action in movements.upper():
                match action:
                    case "R":
                        match self.direction:
                            case "NORTH":
                                self.direction = EAST
                            case "EAST":
                                self.direction = SOUTH
                            case "SOUTH":
                                self.direction = WEST
                            case "WEST":
                                self.direction = NORTH
                    case "L":
                        match self.direction:
                            case "NORTH":
                                self.direction = WEST
                            case "EAST":
                                self.direction = NORTH
                            case "SOUTH":
                                self.direction = EAST
                            case "WEST":
                                self.direction = SOUTH
                    case "A":
                        match self.direction:
                            case "NORTH":
                                coordinates_as_a_list = list(self.coordinates)
                                coordinates_as_a_list[1] += 1
                                self.coordinates = tuple(coordinates_as_a_list)
                            case "EAST":
                                coordinates_as_a_list = list(self.coordinates)
                                coordinates_as_a_list[0] += 1
                                self.coordinates = tuple(coordinates_as_a_list)
                            case "SOUTH":
                                coordinates_as_a_list = list(self.coordinates)
                                coordinates_as_a_list[1] -= 1
                                self.coordinates = tuple(coordinates_as_a_list)
                            case "WEST":
                                coordinates_as_a_list = list(self.coordinates)
                                coordinates_as_a_list[0] -= 1
                                self.coordinates = tuple(coordinates_as_a_list)