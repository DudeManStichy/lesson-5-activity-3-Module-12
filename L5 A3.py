input("XOR sign detection - n ^ m < 0 means n and m have different signs. Press Enter to continue...")
print(" 4 ^ 2 =", 4 ^ 2, "same sign, result is positive")
print(" 4 ^ -2 =", 4 ^ -2, "different signs, result is negative")

n = int(input("Enter a number ( try 5 or -3): "))
guess = input("Will " + str(n) + " ^ -8 be positive or negative? ")
input("XOR is negative when signs are different. Press Enter to continue...")
print(" ", n, "^ -8 =", n ^ -8, " you guessed:", guess)