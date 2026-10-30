decimal_num = int(input("Enter a decimal number:"))
if decimal_num == (0):
    binary_num = (0)
else:
    binary_num = ""
    temp = decimal_num
    while temp > 0:
        remainder = temp % 2
        binary_num = str(remainder) + binary_num 
        temp = temp//2

        print(f"The binary equivalent of {decimal_num} is:{binary_num}")
