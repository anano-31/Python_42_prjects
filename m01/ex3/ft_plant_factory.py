# === Plant Factory Output ===
# Created: Rose (25cm, 30 days)
# Created: Oak (200cm, 365 days)
# Created: Cactus (5cm, 90 days)
# Created: Sunflower (80cm, 45 days)
# Created: Fern (15cm, 120 days)
# Total plants created: 5

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def get_info(self):
        print(f"Created: {self.name} ({self.age}cm, {self.age} days)")
    
if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    print("=== Plant Factory Output ===")

    plants = [rose, oak, cactus, sunflower, fern]
    i = 0
    for p in plants:
            i =  i + 1
            p.get_info()
    
    print(f"Total plants created: {i}")