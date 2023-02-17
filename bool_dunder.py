class PotentialChungus:
    def __init__(self, weight):
        self.weight = weight

    def __bool__(self):
        return self.weight > 100


if __name__ == "__main__":
    if PotentialChungus(85):
        print("That's one Big Chungus!!")
    if PotentialChungus(120):
        print("That's one Big Chungus!!")
