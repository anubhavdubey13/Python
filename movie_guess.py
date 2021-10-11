# Guess the movie may be
# Idea credit Kanika Tayal ft. some MIT OCW

movie = input('Enter the movie name: ').lower()

vowels = ['a','e','i','o','u']

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 
                'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

# outputs the vowels with dashes
guess = []
for m in movie:
    if m in vowels:
        guess.append(' ' + m + ' ')
    else:
        guess.append(' _ ')
        
print(guess)

# Take the letter guess input
letter = input('Enter letter: ').lower()
# insert a conditional here
for i in range(0, len(movie),1):
    if movie[i] == letter:
        guess[i] = letter

print(guess)

# At the moment, I can think of the following things:
# 1. A counter to check the guesses left
# 2. If user inputs complete movie name, a way to compare it
# 3. A way to remove the used up alphabets

# Iter 1
# Some major errors here:
    # 1. taking repeated letters & not exiting 

movie = 'Dhishoom'

guess = []
for m in movie:
    if m in vowels:
        guess.append(' ' + m + ' ')
    else:
        guess.append(' _ ')
        
print(guess)
counter = 9
while (counter > 0) and (' _ ' in guess):
    letter = input('Enter letter: ').lower()
    
    if letter in movie:
        for i in range(0, len(movie),1):
            if movie[i] == letter:
                guess[i] = letter
        if ' _ ' in guess == False:
            print('You guessed right!')
    else:
        counter -= 1
        print(counter)
        if counter == 0:
            print('Game Over. You lost. The movie is ', movie)
