yearsOfInterest
=====
Sometimes we just want to do simple math fast and easy.

Problem: how much money will you have after investing X amount with a rate of return being R percent after Y years?
This program tells you.

Usage Example

    sudo ./install_yoi.sh  <-- to install it on MacOS
     yearsOfInterest [amount-of-money] [interest-rate] [years] [tax rate]
        Note: 
         Interest and tax rate are in decimal form. 
         Tax rate is optional.
         If years is left out, it assumes 30 years by default
     
     yearsOfInterest 100 0.05 2  --> $100.00 growing at 5% for 2 years yields 110.25 dollars!
     yearsOfInterest 100 0.08 5  --> $100.00 growing at 8% for 5 years yields 146.93 dollars!
     yearsOfInterest 100 0.08 5 0.35   --> $100.00 growing at 8% for 5 years yields 74.62 dollars!
     