def english_ruler(n=3, repeats=10):
    limit = repeats * (2 ** n - 2)
    counter = 0
    while counter <= limit:
        dashes = 1
        sub_counter = counter
        while sub_counter & 1:
            dashes += 1
            sub_counter = sub_counter >> 1
        dashes = min(dashes, n)
        print('-' * dashes)
        counter += 1


english_ruler(4, 3)