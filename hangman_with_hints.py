# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    all_letters_are_in_word = True #boolean: turns false if a letter is guessed thats not in the word
    
    for letter in letters_guessed:
        if not letter in secret_word:
            all_letters_are_in_word = False
            break
        
    return all_letters_are_in_word



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    to_return = ""
    
    for letter in secret_word:
        if letter in letters_guessed:
            to_return += letter
        else:
            to_return += "_ "
    
    return to_return
    

        


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    alphabet = string.ascii_lowercase
    
    available_letters = ""
    
    for letter in alphabet:
        if not letter in letters_guessed:
            available_letters += letter
    
    return available_letters
    
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    #--------Initialize variables--------
    
    length_of_word = len(secret_word)
    num_guesses_left = 6
    #num_guesses = 6
    num_warnings_left = 3
    letters_guessed = ""
    current_state = get_guessed_word(secret_word,"")
    available_letters = get_available_letters("")
    vowels = ["a","e","i","o","u"]
    incorrect_vowel = False
    won_game = False
    
    #--------Opening--------
    
    print("Welcome to the Thunderdome!")
    #print("The word is:",secret_word) #TEMP
    print("I'm thinking of a word that's",length_of_word,"letters long.")
    print("You have",num_guesses_left,"guesses. Use them wisely!")
    
    for guess in range(1,num_guesses_left+1):
    
        if(incorrect_vowel == True): #skip this guess if the last guess was an incorrect vowel
            incorrect_vowel = False
            
        else:
            print("\n---- GUESS",guess,"----")    
            print("Available letters:",available_letters)
            #print("Current state:",current_state) #TEMP
               
            subtract_a_guess = False
    
        
            while subtract_a_guess == False and won_game == False:
            
                valid_guess = False    
                guessed_letter = input("Guess a letter: ") #get rid of /n
                #print("You guessed:",guessed_letter) #TEMP
                        
                #----Make sure it's a valid guess----
                        
                if str.isalpha(guessed_letter): #if it's a valid character
                    guessed_letter = str.lower(guessed_letter)
                
                    if guessed_letter in available_letters: #if they haven't already guessed this
                        valid_guess = True
            
                    else: #they already guessed this
                        print("You already guessed this letter!")
                        if num_warnings_left > 0:
                            num_warnings_left -= 1
                            print(num_warnings_left,"warning(s) left")
                        else:
                            print("Out of warnings, this counts as a guess")
                            #valid_guess = True
                            subtract_a_guess = True
                
                else: #it's an invalid character
                    print("That's not a letter!")
                    if num_warnings_left > 0:
                        num_warnings_left -= 1
                        print(num_warnings_left, "warning(s) left")
                    else:
                        print("Out of warnings, this counts as a guess")
                        #valid_guess = True
                        subtract_a_guess = True
                
                #----Actually check this guess----
                
                if valid_guess == True:          
                
                    letters_guessed += guessed_letter    
                    #print("letters guessed:",letters_guessed) #TEMP
            
                    new_state = get_guessed_word(secret_word, letters_guessed)
                    
                    if new_state == current_state: #incorrect guess
                        print("Oops! That letter is not in the word.")
                        subtract_a_guess = True
                        
                        if(guessed_letter in vowels):
                            incorrect_vowel = True
                            print("This counts as 2 guesses!")
                    
                    else: #correct guess
                        if(new_state == secret_word): #they won the game!
                            print("Congratulations! You won!")
                            
                            #----calculate score----
                            unique_letters = ""
                            for ltr in secret_word:
                                if not ltr in unique_letters:
                                    unique_letters += ltr
                            
                            num_unique_letters = len(unique_letters)
                            score = num_unique_letters * (num_guesses_left - guess)
                            
                            print("Your score is:",score)                           
                            
                            won_game = True
                            
                        else:                           
                            print("Good guess!")
                            subtract_a_guess = False                    
                   
                    current_state = new_state
                    available_letters = get_available_letters(letters_guessed)
                
                print(current_state)
                
        if(won_game == True):
            break
            
    if(won_game == False):
        print("You lost!")
        print("The word was:",secret_word)

                

    
    
    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def remove_spaces(my_word):
    
    unspaced_word = ""
    
    for letter in my_word:
        if(letter == " "):
            pass
        else:
            unspaced_word += letter
    
    return unspaced_word
        

def match_with_gaps(my_word, other_word, available_letters):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    same = True  
    counter = 0
    
    for letter in my_word:
        if letter == "_":
            if other_word[counter] in available_letters:
                counter +=1
            else:
                same = False
                break
        elif letter == other_word[counter]:
            counter +=1
        else:
            same = False
            break        
    
    return same
                
        


def show_possible_matches(my_word, available_letters):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    my_word = remove_spaces(my_word)
    my_word_length = len(my_word)
    
    list_of_words = ""
    
    
    #matchcounter = 0 #TEMP
    #lengthcounter = 0 #temp
    
    for word in wordlist:
        if len(word) == my_word_length:
            
            if match_with_gaps(my_word, word, available_letters):
                list_of_words += " "
                list_of_words += word
                
    
    #print("listofwords:",list_of_words)

    list_of_words = list_of_words.strip()
    
    return list_of_words
        
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    #--------Initialize variables--------
    
    length_of_word = len(secret_word)
    num_guesses_left = 6
    #num_guesses = 6
    num_warnings_left = 3
    letters_guessed = ""
    current_state = get_guessed_word(secret_word,"")
    available_letters = get_available_letters("")
    vowels = ["a","e","i","o","u"]
    incorrect_vowel = False
    won_game = False
    
    #--------Opening--------
    

    print("Welcome to the Hint Thunderdome!")
    #print("The word is:",secret_word) #TEMP
    print("I'm thinking of a word that's",length_of_word,"letters long.")
    print("You have",num_guesses_left,"guesses. Use them wisely!")
    
    for guess in range(1,num_guesses_left+1):
    
        if(incorrect_vowel == True): #skip this guess if the last guess was an incorrect vowel
            incorrect_vowel = False
            
        else:
            print("\n---- GUESS",guess,"----")    
            print("Available letters:",available_letters)
            #print("Current state:",current_state) #TEMP
               
            subtract_a_guess = False
    
        
            while subtract_a_guess == False and won_game == False:
            
                valid_guess = False    
                guessed_letter = input("Guess a letter: ") #get rid of /n
                #print("You guessed:",guessed_letter) #TEMP
                        
                #----Make sure it's a valid guess----
                        
                if str.isalpha(guessed_letter): #if it's a valid character
                    guessed_letter = str.lower(guessed_letter)
                
                    if guessed_letter in available_letters: #if they haven't already guessed this
                        valid_guess = True
            
                    else: #they already guessed this
                        print("You already guessed this letter!")
                        if num_warnings_left > 0:
                            num_warnings_left -= 1
                            print(num_warnings_left,"warning(s) left")
                        else:
                            print("Out of warnings, this counts as a guess")
                            #valid_guess = True
                            subtract_a_guess = True
                
                elif guessed_letter == "*": #if they want a hint
                    print("Possible words:")
                    possible_words = show_possible_matches(current_state, available_letters)
                    print(possible_words)
                
                else: #it's an invalid character
                    print("That's not a letter!")
                    if num_warnings_left > 0:
                        num_warnings_left -= 1
                        print(num_warnings_left, "warning(s) left")
                    else:
                        print("Out of warnings, this counts as a guess")
                        #valid_guess = True
                        subtract_a_guess = True
                
                #----Actually check this guess----
                
                if valid_guess == True:          
                
                    letters_guessed += guessed_letter    
                    #print("letters guessed:",letters_guessed) #TEMP
            
                    new_state = get_guessed_word(secret_word, letters_guessed)
                    
                    if new_state == current_state: #incorrect guess
                        print("Oops! That letter is not in the word.")
                        subtract_a_guess = True
                        
                        if(guessed_letter in vowels):
                            incorrect_vowel = True
                            print("This counts as 2 guesses!")
                    
                    else: #correct guess
                        if(new_state == secret_word): #they won the game!
                            print("Congratulations! You won!")
                            
                            #----calculate score----
                            unique_letters = ""
                            for ltr in secret_word:
                                if not ltr in unique_letters:
                                    unique_letters += ltr
                            
                            num_unique_letters = len(unique_letters)
                            score = num_unique_letters * (num_guesses_left - guess)
                            
                            print("Your score is:",score)                           
                            
                            won_game = True
                            
                        else:                           
                            print("Good guess!")
                            subtract_a_guess = False                    
                   
                    current_state = new_state
                    available_letters = get_available_letters(letters_guessed)
                
                print(current_state)
                
        if(won_game == True):
            break
            
    if(won_game == False):
        print("You lost!")
        print("The word was:",secret_word)




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
