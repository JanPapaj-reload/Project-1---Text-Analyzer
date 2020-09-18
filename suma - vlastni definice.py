
#  suma datovych typu pomoci rekurze (line 8)
#  je potreba unpackovat vstupni hodnotu - funkce pozaduje jen jeden argument - a zadani *num defualtne vytvori
#  list pro vkladani vice hodnot.
def sum(*nums) -> int:
    result = 0
    for num in nums:
        if type(num) == type(list()):
            result += sum(*num)
        else:
            result += int(num)
    return result



assert 24 == sum(1,2,3,4,5, "3", [[[[1]]],2,3])
assert 3 == sum(1, "1", [1])
assert 1 == sum(-1, "1", [1])




