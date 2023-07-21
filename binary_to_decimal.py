# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 18:09:59 2023

@author: Julius
"""


"""
main() takes input from the user and checks if it is a postitiv integer, if so it calls dec2bin() and passes 
the input as an argument. We are assuming that the user is not entering strings or any other kind of numbers.
"""
def main():
    
    nummer = input("vargåd ange ett heltal: ")
    if int(nummer) < 0:
        print("kan enbart hantera positiva heltal")
    else:
        dec2bin(nummer)
    
"""
dec2bin() takes one argument and assumes it is an interger. it then checks the size of the interger to determine 
how many bits it might need to represent the number in binary form. it works by calculating the remainder
of the input divided by two. Because it is divided by two, the remainder is always 1 or 0. If we then save 
this remainder and then divide the quotiet by two and then save this remainder in an array and keep doing this
we end up with the binary representaion backwards in the array. So dec2bin() also
reverses the array, then joins it to a string to print out the correct formation.
"""
def dec2bin(nummer):
    ref = nummer
    nummer = int(nummer)
    bin_array = []
    
    if nummer > 65635:
        while nummer >= 1:
            räst = nummer%2
            nummer = nummer//2
            bin_array.append(str(räst))
            
        added_zeros = 32-len(bin_array)
        
        for i in range(added_zeros):
            bin_array.append("0")
            

    elif nummer > 255:
        while nummer >= 1:
            räst = nummer%2
            nummer = nummer//2
            bin_array.append(str(räst))
            
        added_zeros = 16-len(bin_array)
        
        for i in range(added_zeros):
            bin_array.append("0")
                     
            
        
    else:
        while nummer >= 1:
            räst = nummer%2
            nummer = nummer//2
            bin_array.append(str(räst))
            
        added_zeros = 8-len(bin_array)
        
        for i in range(added_zeros):
            bin_array.append("0")
            
    bin_array.reverse()
    print(f"Det binära talet av {ref} är :")
    print("".join(bin_array))
                
    
if __name__ == "__main__":
    main()