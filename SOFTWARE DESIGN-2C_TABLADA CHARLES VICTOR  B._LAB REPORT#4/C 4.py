def reverse(string):
    if len(string) > 0:
        reverse(string[1:])
        print(string[0], end='')
    reverse('pots&pans')