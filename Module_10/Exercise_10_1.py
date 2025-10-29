class Elevator:
    def __init__(self, bottom_f, top_f):
        self.bottom_f = bottom_f
        self.top_f = top_f
        self.position = bottom_f

    def floor_up(self):
        print(f"Going up. Current Position: {self.position}")
        self.position += 1

    def floor_down(self):
        print(f"Going down. Current Position: {self.position}")
        self.position -= 1

    def go_to_floor(self, goal):
        if self.bottom_f <= goal <= self.top_f:
            while self.position != goal:
                if self.position > goal:
                    self.floor_down()
                elif self.position < goal:
                    self.floor_up()
                else:
                    #Just for a quick debug
                    print("This shouldn't be happening, check the code")
                    break
            print(f"Floor reached. Current Position: {self.position}")
        else:
            print(f"Invalid floor, the elevator cannot reach floor {goal}")


h = Elevator(3, 7)
h.go_to_floor(6)
h.go_to_floor(4)
h.go_to_floor(7)
h.go_to_floor(1)
h.go_to_floor(3)




