# Question : Write a Python program to convert an integer to a Roman numeral.

num = int(input("Enter a number : "))

values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

roman = ""

for i in range(len(values)):
    
    while num >= values[i]:
        roman = roman + symbols[i]
        num = num - values[i]

print("Roman numeral : ", roman)