#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        sor = sorted(self)
        for item in sor:
            print(item)
