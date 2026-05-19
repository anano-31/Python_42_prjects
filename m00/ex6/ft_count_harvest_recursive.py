#  ft_count_harvest_recursive()
# Days until harvest: 5
# Day 1
# Day 2
# Day 3
# Day 4
# Day 5
# Harvest time!


def ft_count_harvest_recursive():
    x = int(input("Days until harvest:"))

    def recursive(current_day):
        if current_day < x:
            print(f"Day {current_day}")
            recursive(current_day + 1)
        elif current_day == x:
            print(f"Day {x}")
            print("Harvest time!")
    recursive(1)

ft_count_harvest_recursive()