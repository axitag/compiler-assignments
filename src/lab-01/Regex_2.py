# Expression
# (ab*c) + (def) + ab*c*d

# Expected inputs
# (ab*c) -> the string should start with a , contain all possible combinations of b and end with c.
# def -> should contain string def
# ab*c*d -> the string should start with a , conatin all possible combinations of b and c and end with d.

# final expected inputs
# 1. (ab*c) or
# 2. (def) or
# 3. (ab*c*d) or


# Expression -> (ab*c) + (def) + ab*c*d
def checkAcceptence(string: str) -> bool:

    isAccepted: bool = True

    # Incase the string is empty
    if len(string) == 0:
        isAccepted = False

    # for (ab*c)
    elif string[0] == "a" and string[len(string) - 1] == "c":
        for idx, char in enumerate(string):
            # checking in the middle
            if idx > 0 and idx < len(string) - 1 and char != "b":
                isAccepted = False
                break

    # for def
    elif string == "def":
        return isAccepted

    # for (ab*c*d)
    elif string[0] == "a" and string[len(string) - 1] == "d":
        for idx, char in enumerate(string):
            if idx > 0 and idx < len(string) - 1:
                if char == "b" or char == "c":
                    if char == "c" and string[idx + 1] == "b":
                        isAccepted = False
                        break

                else:
                    isAccepted = False
                    break
    else:
        isAccepted = False

    return isAccepted


while True:
    string: str = input("Enter a string > ")
    print("Given string: ", string)

    isAccepted: bool = checkAcceptence(string)

    if isAccepted:
        print("String Accepted!")
    else:
        print("String not Accepted!")
