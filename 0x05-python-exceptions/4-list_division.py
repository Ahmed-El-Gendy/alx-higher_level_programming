#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []

    for i in range(0, list_length):
        try:
            t = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            t = 0
            print("division by 0")
        except TypeError:
            t = 0
            print("wrong type")
        except IndexError:
            t = 0
            print("out of range")
        finally:
            new.append(t)
    return new
