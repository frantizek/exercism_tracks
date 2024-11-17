def egg_count(display_value):
    result = 0
    display_number_to_binary = str(bin(display_value))[2::]
    for char in display_number_to_binary:
        if char == "1":
            result += 1
    return result