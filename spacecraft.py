class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        if self.direction == "North":
            self.y += 1
        elif self.direction == "South":
            self.y -= 1
        elif self.direction == "East":
            self.x += 1
        elif self.direction == "West":
            self.x -= 1
        elif self.direction == "Up":
            self.z += 1
        elif self.direction == "Down":
            self.z -= 1

    def move_backward(self):
        if self.direction == "North":
            self.y -= 1
        elif self.direction == "South":
            self.y += 1
        elif self.direction == "East":
            self.x -= 1
        elif self.direction == "West":
            self.x += 1
        elif self.direction == "Up":
            self.z -= 1
        elif self.direction == "Down":
            self.z += 1

    def turn_left(self):
        if self.direction == "North":
            self.direction = "West"
        elif self.direction == "South":
            self.direction = "East"
        elif self.direction == "East":
            self.direction = "North"
        elif self.direction == "West":
            self.direction = "South"

    def turn_right(self):
        if self.direction == "North":
            self.direction = "East"
        elif self.direction == "South":
            self.direction = "West"
        elif self.direction == "East":
            self.direction = "South"
        elif self.direction == "West":
            self.direction = "North"

    def turn_up(self):
        if self.direction in ["North", "South", "East", "West"]:
            self.direction = "Up"

    def turn_down(self):
        if self.direction in ["North", "South", "East", "West"]:
            self.direction = "Down"

    def execute_commands(self, commands):
        for command in commands:
            if command == "f":
                self.move_forward()
            elif command == "b":
                self.move_backward()
            elif command == "l":
                self.turn_left()
            elif command == "r":
                self.turn_right()
            elif command == "u":
                self.turn_up()
            elif command == "d":
                self.turn_down()
