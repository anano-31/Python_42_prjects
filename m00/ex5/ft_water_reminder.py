# >>> ft_water_reminder()
# Days since last watering: 4
# Water the plants!
# >>> ft_water_reminder()
# Days since last watering: 1
# Plants are fine


def ft_water_reminder():
    x = int(input("Days since last watering:"))
    if x > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")