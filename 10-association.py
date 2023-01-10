"""
Jatka edellisen tehtävän ohjelmaa siten,
että Talo-luokassa on parametriton metodi palohälytys, 
joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, 
että talossasi tulee palohälytys.
"""

class Hissi:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def __str__(self):
        return f'Hissi joka on kerroksessa {self.current_floor}'

    def move_to_floor(self, move_to):
        if move_to < self.bottom_floor or move_to > self.top_floor:
            print("Kerrosta ei ole olemassa.")
            return
        if move_to == self.current_floor:
            print("Olet jo tällä kerroksella.")
            return

        subtraction = abs(move_to - self.current_floor)
        if move_to > self.current_floor:
            self.move_floor_up(subtraction)
        else:
            self.move_floor_down(subtraction)

    def move_floor_down(self, move_to):
        for i in range(move_to):
            self.current_floor -= 1
            print(f"Nyt ollaan kerroksella {self.current_floor}.")
    
    def move_floor_up(self, move_to):
        for i in range(move_to):
            self.current_floor += 1
            print(f"Nyt ollaan kerroksella {self.current_floor}.")

class Talo:
    def __init__(self, bottom_floor, top_floor, num_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(num_of_elevators):
            self.elevators.append(Hissi(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, target_floor):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print("Virheellinen hissin numero.")
            return
        self.elevators[elevator_number].move_to_floor(target_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.move_to_floor(self.bottom_floor)
            print(f"{elevator} on pohjakerroksessa.")
    
def main():
    new_house = Talo(1, 10, 2)
    print(f"Talon hissien määrä {(len(new_house.elevators))}")
    print(f"Talon hissien pohja kerros {new_house.bottom_floor}")
    print(f"Talon korkein kerros {(new_house.top_floor)}")
    new_house.run_elevator(0, 5)
    new_house.run_elevator(1, 3)
    new_house.fire_alarm()

if __name__ == "__main__":
    main()
