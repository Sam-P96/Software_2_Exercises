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


class Building:
    def __init__(self, bottom_f, top_f, no_ele):
        self.bottom_f = bottom_f
        self.top_f = top_f
        self.ele_list = []
        for i in range(no_ele):
            self.ele_list.append(Elevator(bottom_f, top_f))

    def run_elevator(self, ele_no, destination):
        true_ele = ele_no - 1
        self.ele_list[true_ele].go_to_floor(destination)

b = Building(0, 10, 3)
b.run_elevator(2, 8)

print(b.ele_list[0].position)
print(b.ele_list[1].position)
print(b.ele_list[2].position)





