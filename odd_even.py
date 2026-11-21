def odd_even_check(x):
    count={"even":0,"odd":0}
    for n in x:
        if n%2==0:
            count["even"]+=1
        else:
            count["odd"]+=1

    return count

