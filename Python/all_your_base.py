def rebase(input_base, digits, output_base):
    if int(input_base) < 2 :
        raise ValueError("input base must be >= 2")

    for digit in digits:
        if not(0 <= digit < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")

    if int(output_base) < 2 :
        raise ValueError("output base must be >= 2")

    base_ten = 0
    position = len(digits)-1
    if position > 0:
        for digit in digits:
            base_ten += digit * pow(input_base, position)
            position -= 1

    list_converted = []
    for number in str(base_ten):
        list_converted.append(int(number))

    return list_converted






'''
print(rebase(10, [4,2], 3)) #1120



print(rebase(2, [1,0,1,0,1,0], 10)) # 42
print(rebase(3, [1,1,2,0], 10)) #42
'''

print(rebase(10, [4,2], 2)) #101010