import winsound
import time

# dictionary to ranslate letters to morse
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', ' ':' '} 

# Splits a string into a list
def split(word): 
    return [char for char in word]

# plays the dot sound effect (eh)
def dot():
    winsound.PlaySound('dot.wav', winsound.SND_FILENAME)

# plays the dash sound effect (ehhhhh)
def dash():
    winsound.PlaySound('dash.wav', winsound.SND_FILENAME)

# Plays the corresponding sound effect when a character morse is suppied e.g. "..-"
def GetMorse(morse):
    for ch in morse:
        if ch == '.':
            dot()
        elif ch == '-':
            dash()
        else: # if a dash or dot isn't found e.g. a space (' '), the code will pause for 1 second
            time.sleep(1)
    # Pause between each charater
    time.sleep(0.15)

def main():
    # Get string to convert as user input and convert to uppercase
    text = input("Enter text to be converted...").upper()

    # Convert the string to a list
    textToList = split(text)

    # Loop through list of characters
    for ch in textToList:
        # Get morse equiv. of character
        morseChar = MORSE_CODE_DICT.get(ch)

        # test if the character was found in the morse code dictionary
        if morseChar != None:
            # play audio equivelent of morse code character
            print(morseChar)
            GetMorse(morseChar)
        else:
            # notify the user the code will be exited and why
            print("Unsupported character given...quiting script...")
            quit
    
    print("")
    print("")
    print("")
    print("")
    
    main()

main()