# Guess the movie may be
# Idea credit Kanika Tayal ft. some MIT OCW

# What I would want to see this as: Multi-player game like scribble

# Final Function. Version 2
# Issue: 1. I have to hide the input but can't figure a way rn
# Update: Been able to clear console so kinda works for now
# Baaki to fulfill objective, might have to learn frontend

def guess_the_movie(movie):
    
    vowels = ['a','e','i','o','u']
    
    movie = movie.lower()

    guess = []
    for m in movie:
        if m in vowels:
            guess.append(m)
        elif m == ' ':
            guess.append('/')
        else:
            guess.append(' _ ')
    print("\033[H\033[J")         
    print(''.join(guess))

    counter = 9
    list_guessed_letters = vowels.copy()
    while (counter > 0) and (' _ ' in guess):
        letter = input('Enter letter: ').lower()
        
        if letter in list_guessed_letters:
            print('Letter already guessed or it is vowel. Try again')
        else: 
            if letter in movie:
                for i in range(0, len(movie),1):
                    if movie[i] == letter:
                        guess[i] = letter
            else:
                counter -= 1
                if counter == 0:
                    print('Game Over. You lost. The movie is', movie)
        
        if ' _ ' not in guess:
            print('You guessed right! The movie is', movie)
        else:
            print(''.join(guess))
            print('Guesses left:', counter)
        
        list_guessed_letters.append(letter)
    
guess_the_movie('Kal Ho Na Ho')

#==============================================================================

# import getpass
# m = getpass.getpass('Enter movie:')
# print(m)
    
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
    # 1. taking repeated letters & not exiting - sorted

movie = 'Shershah'
movie = movie.lower()

guess = []
for m in movie:
    if m in vowels:
        guess.append(m)
    else:
        guess.append(' _ ')
        
print(guess)

counter = 9
list_guessed_letters = vowels.copy()
while (counter > 0) and (' _ ' in guess):
    letter = input('Enter letter: ').lower()
    
    if letter in list_guessed_letters:
        print('Letter already guessed or it is vowel. Try again')
    else: 
        if letter in movie:
            for i in range(0, len(movie),1):
                if movie[i] == letter:
                    guess[i] = letter
        else:
            counter -= 1
            if counter == 0:
                print('Game Over. You lost. The movie is ', movie)
    
    if ' _ ' not in guess:
        print('You guessed right! The movie is ', movie)
    else:
        print(guess)
        print('Guesses left:', counter)
    
    list_guessed_letters.append(letter)
    
