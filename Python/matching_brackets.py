# Given a string containing brackets [], braces {}, parentheses (),
# or any combination thereof, verify that any and all pairs are matched and nested correctly.
# The string may also contain other characters, which for the purposes of this exercise should be ignored.

def is_paired(input_string: str) -> bool:
    if len(input_string) == 0:
        return True
    else:
        complement = ""
        for element in input_string.upper():
            match element:

                # If they are opening brackets, add to the variable so we can compare

                case "[":
                    complement += "["
                case "{":
                    complement += "{"
                case "(":
                    complement += "("

                case "]":
                    if len(complement) == 0:
                        # the first element is a closing bracket, therefore
                        return False
                    elif complement[-1] == "[":
                        # the last saved element is a match, so we can delete
                        # and proceed in case there are more elements to evaluate
                        complement = complement[:-1]
                    else:
                        # the last element being evaluated does not match
                        return False
                case "}":
                    if len(complement) == 0:
                        # the first element is a closing bracket, therefore
                        return False
                    elif complement[-1] == "{":
                        # the last saved element is a match, so we can delete
                        # and proceed in case there are more elements to evaluate
                        complement = complement[:-1]
                    else:
                        # the last element being evaluated does not match
                        return False
                case ")":
                    if len(complement) == 0:
                        # the first element is a closing bracket, therefore
                        return False
                    elif complement[-1] == "(":
                        # the last saved element is a match, so we can delete
                        # and proceed in case there are more elements to evaluate
                        complement = complement[:-1]
                    else:
                        # the last element being evaluated does not match
                        return False

                case _:
                    complement += ""

        if len(complement) == 0:
            return True
        return False