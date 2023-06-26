#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divList = []
    for i in range(list_length):
        try:
            result = 0
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            i += 1
            print('wrong type')
        except IndexError:
            i += 1
            print('out of range')
        finally:
            divList.append(result)
    return divList
