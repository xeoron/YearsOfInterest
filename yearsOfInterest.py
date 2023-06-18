#!/usr/bin/env python
# Name: yearsOfInterest.py
# License: Released under GPL v3 or higher. Details here http://www.gnu.org/licenses/gpl.html
# Author: Jason Campisi
# Version 0.2.1
# Date: 6/18/23
# About: This program solves if you have X amount of money that grows in interest rate Y each year, how much do you have after Y years?
# Usage: yearsOfInterest [amount-of-money] [interest-rate] [years] [tax rate]
#  Where interest and tax rate is in decimal form
#  if you do not define years, it will assume 30
#  Tax rate is optional... idea what if you are paid x for y years each year you are taxed, thus account for take home after taxes
# Example: 
#   yoi 100 0.08 5 0.35   --> $100.00 growing at 8% for 5 years yields 95.51 dollars!

from ast import Return
import sys

def addFormatting(number):  # add comas to large nunbers and round to 2 digital before the decimal point
    return ("{:,.2F}".format(number))
def percentage(number):     # convert digit percentage to number thus 0.05 percent is converted to 5%
    return "{0:.0f}%".format(number * 100)   

try:
    if len(sys.argv) < 3: #is sys.argv[1] && sys.argv[2] empty?
        print ("Error: Please provide the money value and interest rate in decimal form!")
        exit(1)
    else:
        money = float(sys.argv[1])
        interest = float(sys.argv[2])
        
    if len(sys.argv) < 4:   #no years of interest?
        years = 30
    else:
        years = int(sys.argv[3])
    if len(sys.argv) < 5:   #no tax rate given?
        tax = 1
    else: # account for taxes if percentage was given
        tax = float(sys.argv[4])
        money = money - (money * tax)
        #print ("Amount after taxes is this", money)

    for y in range (years):
        money = money + ((money * interest) * tax)

    print ( "$%s" % addFormatting(float(sys.argv[1])), "growing at",percentage(interest), "for", years, "years yields", addFormatting(money), "dollars!")

except SyntaxError:
    print ("Failure: %s" % SyntaxError)    
    exit()