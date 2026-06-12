def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def helper(d):
        if d > n:
            print("Harvest time!")
            return
        print(f"Day {d}")
        helper(d + 1)
    helper(1)
