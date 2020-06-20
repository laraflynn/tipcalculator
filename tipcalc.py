# Author: Lara Flynn
# Created: June 19 2020
# Last Updated: June 19 2020

import sys

def get_tip(total, percent):
    return total * (percent / 100)

if __name__ == "__main__":
    print("How much was the bill?")
    total = float(input())
    print("How much do you want to tip?")
    percent = float(input())
    tip = get_tip(total, percent)
    print("You should tip %4.2f bucks." % tip)
    print("Your total spending will be %4.2f bucks." % (total + tip))