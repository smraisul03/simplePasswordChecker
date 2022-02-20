import string

# Take input from keyboard to check for password
password = input("Please enter password: ")

# Iterate through all characters, digits & special characters in password
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
punctuation = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

# Re-orienting characters to a variable
characters = [upper_case, lower_case, punctuation, digits]

# Determine the length of the password
length = len(password)

# Initializing the score
score = 0

# Open the file with the common passwords used
with open('common.txt', 'r') as f:
    common = f.read().splitlines()

# If password is found in the list, disregard
if password in common:
    print("Password was found in a common list. Score 0 / 7")
    exit(0)

# Counting the length
if length > 8:
    score += 1
if length > 16:
    score += 1
if length > 32:
    score += 1
print(f"Password length is {str(length)}, adding {str(score)} points!")

# Counting the number of characters
if sum(characters) > 2:
    score += 1
if sum(characters) > 4:
    score += 1
if sum(characters) > 8:
    score += 1
print(f"Password has {str(sum(characters))} character types, adding {str(sum(characters) - 1)} points!")

# Adding up scores & responding back prompts
if score < 2:
    print(f"Password is weak! Score: {str(score)} / 7 ")
elif score > 2 or score < 4:
    print(f"Password is ok! Score: {str(score)} / 7 ")
elif score > 5 or score < 6:
    print(f"Password is good! Score: {str(score)} / 7 ")
elif score > 6:
    print(f"Password is excellent! Score: {str(score)} / 6 ")
