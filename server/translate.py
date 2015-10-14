'''Helper functions for morse code translation.'''
__author__ = 'Sebastian Boyd'
import re

def text_to_morse(text):
    '''Translate a list of words into morse code.
    @param words: A list of Alphanumeric strings.
    @returns: A list of lists of strings containing . and -
    '''
    text = format(text)
    words = text.split()
    morse_word_list = []
    for word in words:
        word = word.lower()
        morse_letter_list = []
        letters = list(word)
        for letter in letters:
            morse_letter_list.append(morse_alphabet[letter])
        morse_word_list.append(morse_letter_list)

    return morse_word_list

def format(text):
	if text == None:
		text = ''
	pattern = re.compile('[\W_]+', re.UNICODE)
	text = pattern.sub('', text)
	text = text.lower()
	return text


'''Morse code dictionary definitions'''
morse_alphabet = {}
morse_alphabet['a'] = '.-'
morse_alphabet['b'] = '-...'
morse_alphabet['c'] = '-.-.'
morse_alphabet['d'] = '-..'
morse_alphabet['e'] = '.'
morse_alphabet['f'] = '..-.'
morse_alphabet['g'] = '--.'
morse_alphabet['h'] = '....'
morse_alphabet['i'] = '..'
morse_alphabet['j'] = '.---'
morse_alphabet['k'] = '-.-'
morse_alphabet['l'] = '.-..'
morse_alphabet['m'] = '--'
morse_alphabet['n'] = '-.'
morse_alphabet['o'] = '---'
morse_alphabet['p'] = '.--.'
morse_alphabet['q'] = '--.-'
morse_alphabet['r'] = '.-.'
morse_alphabet['s'] = '...'
morse_alphabet['t'] = '-'
morse_alphabet['u'] = '..-'
morse_alphabet['v'] = '...-'
morse_alphabet['w'] = '.--'
morse_alphabet['x'] = '-..-'
morse_alphabet['y'] = '-.--'
morse_alphabet['z'] = '--..'
morse_alphabet['1'] = '.----'
morse_alphabet['2'] = '..---'
morse_alphabet['3'] = '...--'
morse_alphabet['4'] = '....-'
morse_alphabet['5'] = '.....'
morse_alphabet['6'] = '-....'
morse_alphabet['7'] = '--...'
morse_alphabet['8'] = '---..'
morse_alphabet['9'] = '----.'
morse_alphabet['0'] = '-----'
