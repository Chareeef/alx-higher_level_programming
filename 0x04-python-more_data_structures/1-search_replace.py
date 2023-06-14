#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def rep(x):
        if x != search:
            return x
        else:
            return replace
    return [list(map(rep, my_list))]
