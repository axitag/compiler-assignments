# Expression
# ((a+b)*(c+d)*) + ab*c*d

# Expected inputs
# (a+b)* -> all possible combinations of (a+b)* like a, b, aab, aba....
# (c+d)* => all possible combinations of (c+d)* like c, d, cd, dc,dcd ...
# ((a+b)*(c+d*) -> gives concatinated string.
# ab*c*d -> string should start with a includes combinations of b* and c* and ends with d.

# Final expected inputs
# 1. ((a+b)*(c+d*)) or
# 2. ab*c*d or


# steps
def checkAccepted(string: str) -> bool:

    isAccepted: bool = True

    # for empty strings
    if len(string) == 0:
        isAccepted = False

    for idx, char in enumerate(string):
        # ab*c*d
        if idx > 0 and idx < len(string) - 1:
            if char == "c" and string[idx + 1] == "b":
                isAccepted = False

            # ((a+b)*(c+d*))
            if char == "c":
                if string[idx + 1] == "a" or string[idx + 1] == "b":
                    isAccepted = False
            if char == "d":
                if string[idx + 1] == "a" or string[idx + 1] == "b":
                    isAccepted = False

    return isAccepted


while True:
    string: str = input("Enter a string >")
    print("Given String", string)

    isAccepted: bool = checkAccepted(string)

    if isAccepted:
        print("String Accepted!")
    else:
        print("String not Accepted!")
