# === Day 1 ===
# Rose: 25cm, 30 days old
# === Day 7 ===
# Rose: 31cm, 36 days old
# Growth this week: +6cm

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def age(self):
        self.age += 1
    def height(self):
        self.height +=1
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()

    for day in range(1, 7):
        rose.height
        rose.age
    
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{day}cm")
