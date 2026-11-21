def even_number_counter (x):
    counter= {"parzyste": 0, "nieparzyste": 0}
    for element in x:
        if element%2==0:
            counter["parzyste"] += 1
        else:
            counter["nieparzyste"] += 1

    return counter

