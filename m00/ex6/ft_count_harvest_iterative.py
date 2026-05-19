def ft_count_harvest_iterative():
    x = int(input("Days until harvest:"))
    for i in range(1, x):
        print("Day", i)
    print(f"Day {x}")
    print("Harvest time!")

ft_count_harvest_iterative()