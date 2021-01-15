letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25::-1]
print(backwards)

# create a slice that produces the characters qpo
print(letters[17:14:-1])

# slice the string to produce edcba
print(letters[4::-1])

# slice the string to produce the last 8 characters, in reverse order
print(letters[26:17:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])
