# Expression
# (0* + 1*) + 0*1*

# Expected inputs
# 0* -> all possible combinations of string 0 including epsilon
# 1* -> all possible combinations of string 1 including epsilon
# (0* + 1*) -> all possible combinations  of  0 or 1 including epsilon
# 0*1* ->the expression should start with combinations of 0 followed by combinations of 1 no mixing

# final expected inputs
# 1. 0* or
# 2. 1* or
# 3. 0*1*

# Steps


# Expression -> (0* + 1*) + 0*1*
def checkAcceptence(string: str) -> bool:

    isAccepted: bool = True

    # if the string is of length 0 : epsilon
    if len(string) == 0:
        return isAccepted

    # only when string contains 0 after 1 will it get rejected
    for idx, char in enumerate(string):
        if char == "1" and idx != len(string) - 1 and string[idx + 1] == "0":
            isAccepted = False
    return isAccepted


while True:
    string: str = input("Enter a string >")
    print("Given string")

    isAccepted: bool = checkAcceptence(string)

    if isAccepted:
        print("String Accepted!")
    else:
        print("String not Accepted!")
