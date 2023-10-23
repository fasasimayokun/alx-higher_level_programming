#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """a func that divides elem by elem 2 lists."""
    newList = []

    for nm in range(list_length):
        try:
            newList.append(my_list_1[nm] / my_list_2[nm])
        except ZeroDivisionError:
            newList.append(0)
            print("division by 0")
            continue
        except IndexError:
            newList.append(0)
            print("out of range")
            continue
        except TypeError:
            newList.append(0)
            print("wrong type")
            continue
        finally:
            pass
    return newList
