class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def age_(self):
        self.age += 1
    def growth(self):
        self.height +=1
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    plants = [rose]
    print("=== Day 1 ===")
    plants[0].get_info()

    for p in plants:
        for day in range(1, 7):
            p.growth()
            p.age_()
    
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{day}cm")
