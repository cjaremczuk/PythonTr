import random
from words import words
import string

def get_valid_word(words):
        word = random.choice(words)  #randomly chooses something from the list
        while '-' in word or ' ' in word:
            word = random.choice (words)
            
        return word.upper()          #convert word into uppercase
        
        
def hangman():             
        word= get_valid_word (words)
        word_letters = set(word)     #get letters in the word
        alphabet = set(string.ascii_uppercase)
        used_letters = set()         #what user has guessed
        lives = 10                   #initialize number of chances
        
        #getting user input
        while len(word_letters)> 0 and lives> 0:
            #letters used
            print ('You have', lives, 'lives left and have used these letters:   ', ' '.join(used_letters))
        
            #status of current word guessing--what current word is
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print ('Current word:    ', '  '.join(word_list))
        
            user_letter = input('Guess a letter:  ').upper()
            if user_letter in alphabet-used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    
                else:
                    lives-=1 #takes away a life if wrong
                    print ('Letter is not in word')
                 
            elif user_letter in used_letters:
                print ('You already selected that letter. Please try again.')
                
            else:
                print('Invalid character.  Please try again')
        
        # gets here when word_letters= 0 or lives=0
        if lives==0:
                print ('Sorry, you died')
                
        else:
                print ('You guessed the right word',word ,'!!!')

if __name__ == '__main__':
    hangman()        
        