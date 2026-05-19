# >>> ft_plant_age()
# Enter plant age in days: 75
# Plant is ready to harvest!
# >>> ft_plant_age()
# Enter plant age in days: 45
# Plant needs more time to grow.

def ft_plant_age():
    x = int(input("Enter plant age in days:"))
    if x > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
