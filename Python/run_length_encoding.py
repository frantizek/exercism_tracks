def decode(string):
    if len(string) == 0:
        return ""
    else:
        # At this point we know that the string at least contains one value
        if all(c.isalnum() or c.isspace() for c in string):
            # All valid characters
            decoding = ""
            current_counter = "0"

            # Initialize the values
            if string[0].isdigit():
                current_counter = string[0]
            else:
                decoding += string[0]
            string = string[1:]

            while len(string) > 0:

                if string[0].isdigit():
                    current_counter += string[0]
                else:
                    if int(current_counter) >= 2:
                        decoding += string[0] * int(current_counter) 
                    else:
                        decoding += string[0]
                    # We can reset the values
                    current_counter = "0"
                string = string[1:]
        
        return decoding


def encode(string):
    if len(string) == 0:
        return ""
    else:
        # At this point we know that the string at least contains one value
        if all(c.isalpha() or c.isspace() for c in string):
            # All valid characters
            encoding = ""

            # Initialize the values
            current_letter = string[0]
            current_counter = 1
            string = string[1:]


            while len(string) > 0:

                if string[0] == current_letter:
                    current_counter += 1
                else:
                    # If there is a change, first save the data in the encoding string
                    if str(current_counter) == "1":
                        encoding += current_letter
                    else:
                        encoding += str(current_counter) + current_letter
                    # We can reset the values
                    current_counter, current_letter = 1, ""
                    current_letter = string[0]
                string = string[1:]

            if str(current_counter) == "1":
                encoding += current_letter
            else:
                encoding += str(current_counter) + current_letter


        return encoding
