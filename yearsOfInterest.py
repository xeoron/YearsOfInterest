#!/usr/bin/env python
# Name: yearsOfInterest.py
# License: Released under GPL v3 or higher. Details here http://www.gnu.org/licenses/gpl.html
# Author: Jason Campisi
# Version 0.1.0
# Date: 6/13/23
# About: This program solves if you have X amount of money that grows in interest rate Y each year, how much do you have after Y years?
# Usage: yoi amount-of-money interest-rate [years]
#  Where interest rate is in decimal form
#  if you do not define years, it will assume 30

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
    
    for y in range (years):
        money = money + (money*interest)

    print ( "$%s" % addFormatting(float(sys.argv[1])), "growing at",percentage(interest), "for", years, "years yields", addFormatting(money), "dollars!")

except SyntaxError:
    print ("Failure: %s" % SyntaxError)    
    exit()