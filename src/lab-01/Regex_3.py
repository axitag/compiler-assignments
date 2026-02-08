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


# Expression -> ((a+b)*(c+d)*) + ab*c*d
def checkAccepted(string: str) -> bool:

    isAccepted: bool = True

    # for empty strings
    if len(string) == 0:
        isAccepted = True

        # for ab*c*d
    elif (
        string[0] == "a"
        and string[len(string) - 1] == "d"
        and string.count("a") == 1
        and string.count("d") == 1
    ):
        for idx, char in enumerate(string):
            if idx > 0 and idx < len(string) - 1:
                if char == "b" or char == "c":
                    if char == "c" and string[idx + 1] == "b":
                        isAccepted = False
                        break

                else:
                    isAccepted = False
                    break

    # for ((a+b)*(c+d)*)
    elif string[0] == "a" or string[0] == "b" or string[0] == "c" or string[0] == "d":
        for idx, char in enumerate(string):
            if char == "a" or char == "b" or char == "c" or char == "d":
                if idx < len(string) - 1:
                    if char == "c" and (
                        string[idx + 1] == "a" or string[idx + 1] == "b"
                    ):
                        isAccepted = False
                        break
                    if char == "d" and (
                        string[idx + 1] == "a" or string[idx + 1] == "b"
                    ):
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
    print("Given String", string)

    isAccepted: bool = checkAccepted(string)

    if isAccepted:
        print("String Accepted!")
    else:
        print("String not Accepted!")
