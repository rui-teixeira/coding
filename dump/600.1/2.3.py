# Paste your code into this box
floor = 0
ceil = 100
guess = 50
valid = ['h', 'c', 'l']

print("Please think of a number between 0 and 100!")
print("Is your secret number {}?".format(guess))
print("Enter 'h' to indicate the guess is too high.", end=' ')
print("Enter 'l' to indicate the guess is too low.", end=' ')
print("Enter 'c' to indicate I guessed correctly.")
user = input()
while True:
    if user not in valid:
        print("Sorry, I did not understand your input.")
        continue
    if user == 'c':
        break
    elif user == 'h':
        ceil = guess - 1
        guess = (ceil - floor) // 2 + floor
    elif user == 'l':
        floor = guess + 1
        guess = (ceil - floor) // 2 + floor
    print("Is your secret number {}?".format(guess))
    user = input()
print("Game over. Your secret number was: {}".format(guess))        
