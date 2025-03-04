# Shot game Tutorial 1 STOR-i 609
def shoot_game(n,m):
    targets = list(range(n))
    pos = 0
    while len(targets)>1:
        # remove
        remove_element = targets.pop(pos)
        print(remove_element)
        # find next alive
        pos = (pos + (m-1)) % len(targets)

shoot_game(6,2)