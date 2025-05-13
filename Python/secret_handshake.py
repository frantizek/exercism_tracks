"""
00001 = wink
00010 = double blink
00100 = close your eyes
01000 = jump
10000 = Reverse the order of the operations in the secret handshake.
"""

def commands(binary_str: str) -> list[str]:
    commands_list = []
    if binary_str[4] == "1":
        commands_list.append("wink")
    if binary_str[3] == "1":
        commands_list.append("double blink")
    if binary_str[2] == "1":
        commands_list.append("close your eyes")
    if binary_str[1] == "1":
        commands_list.append("jump")
    if binary_str[0] == "1":
        commands_list.reverse()
    return commands_list
