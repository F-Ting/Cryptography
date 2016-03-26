# Functions for running an encryption or decryption algorithm

ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions after this comment.  Do not change the statements above
# this comment.  Do not use import, open, input or print statements in the 
# code that you submit.  Do not use break or continue statements.

def clean_message(message):
    """(str) -> str
    
    Return only the alphabetical characters in message that has been converted
    to uppercase
    
    >>>clean_message("abc123def")
    ABCDEF
    >>>clean_message("I AM spaaaaaaaaarta123   ")
    IAMSPAAAAAAAAARTA
    """
    
    message_holder = ""
    for i in message:
        if i.isalpha():
            message_holder += i
    return message_holder.upper()

def encrypt_letter(letter, value):
    """(str, int) -> str
    
    return the encripted letter using value to encrypt the letter
    
    >>>encrypt_letter("A", 1)
    B
    >>>encrypt_letter("Z", 10)
    J
    """
    
    key_value = (ord(letter) - ord("A") + value)%26
    return chr(key_value + ord('A'))

def decrypt_letter(letter, value):
    """(str, int) -> str
    
    return the decripted letter using value to decrypt the letter
    
    >>>decrypt_letter("J", 10)
    Z
    >>>decrypt_letter("B", 1)
    A
    """
    
    key_value = (ord(letter)- ord("A") - value)%26
    return chr(key_value + ord('A'))

def swap_cards(deck, index):
    """(list of int, int) -> NoneType
    
    swap card at index with the card that is 1 index higher
     
    >>>deck = [1,2,3,4,5]
    >>>swap_cards(deck, 2)
    >>>deck
    [1,2,4,3,5]
    
    >>>deck = [6,12,2,7,4,3]
    >>>swap_cards(deck,5]
    >>>deck
    [3,12,2,7,4,3,6]
    """
    a = deck[index]
    if index == len(deck) - 1:
        deck[index] = deck[0]
        deck[0] = a
    else:
        deck[index] = deck[index + 1]
        deck[index + 1] = a
    
def get_small_joker_value(deck):
    """(list of int) -> int
    
    return the value of the second highest card
    
    >>>get_small_joker_value([1,2,3,4,5])
    4
    >>>get_small_joker_value([12,2,43,24,56])
    43
    """
    
    new_deck = deck + []
    new_deck.remove(get_big_joker_value(deck))
    return max(new_deck)

def get_big_joker_value(deck):
    """(list of int) -> int
    
    return the value of the highest card
    
    >>>get_big_joker_value([1,2,3,4,5])
    5
    >>>get_big_joker_value([551,212,3,424,5])
    551
    """
    
    return max(deck)

def move_small_joker(deck):
    """(list of int) -> NoneTypa

    swap the small joker with the value under it
    
    >>>deck = [551,212,3,424,5]
    >>>move_small_joker([551,212,3,424,5])
    >>>deck
    [551,212,3,424,5]
    
    
    """
    
    swap_cards(deck,deck.index(get_small_joker_value(deck)))

def move_big_joker(deck):
    """(list of int) -> NoneType

    swap the big joker with the value under it, then swaps with the next value
    under it
    
    >>>deck = [3,4,5,1,2]
    >>>move_big_joker(deck)
    >>>deck
    [3,4,1,2,5]
    
    """
    
    swap_cards(deck,deck.index(get_big_joker_value(deck)))
    swap_cards(deck,deck.index(get_big_joker_value(deck)))

def triple_cut(deck):
    """(list of int) -> NoneType
        
        swap the numbers before the first joker with the numbers after the second
        joker in a list
        
    >>>deck = [1,2,3,4,20,5,6,7,8,9,30,10,11,12,13,14]
    >>>triple_cut(deck)
    >>>deck
    [10, 11, 12, 13, 14, 20, 5, 6, 7, 8, 9, 30, 1, 2, 3, 4]
    
    
    """    
    
    top_stack = []
    bottom_stack = []
    
    small_joker_index = deck.index(get_small_joker_value(deck))
    big_joker_index = deck.index(get_big_joker_value(deck))

    if small_joker_index < big_joker_index:
        top_joker_index = small_joker_index
        bottom_joker_index = big_joker_index
    elif small_joker_index > big_joker_index:
        top_joker_index = big_joker_index 
        bottom_joker_index = small_joker_index
        
# make a copy of the top and bottom stack
    for i in deck:
        if deck.index(i) < top_joker_index:
            top_stack.append(i)
        if deck.index(i) > bottom_joker_index:
            bottom_stack.append(i)
# take the top stack and bottom stack out of the original deck
    for i in top_stack:
        deck.remove(i)
    for i in bottom_stack:
        deck.remove(i)     
# insert the bottom stack on the top of deck and insert top stack on bottom of
# deck
    for i in range(len(bottom_stack)):
        deck.insert(i,bottom_stack[i])
    for i in range(len(top_stack)):
        deck.insert(len(deck)+i,top_stack[i])

def insert_top_to_bottom(deck):
    """(list of int) -> NoneType
    
    read thhe value of the bottom and take that many amount of cards from the top
    of the deck and insert them on top of the bottom card of the deck in the 
    right order
    
    >>>deck = [10,11,12,13,14,15,1,2,7,8,9,3,4,5,6]
    >>>insert_top_to_bottom(deck)
    >>>deck
    [11, 13, 15, 2, 8, 3, 4, 5, 10, 12, 14, 1, 7, 9, 6]
    
    """
    
    top_stack = []
    bottom_card = deck[len(deck)-1]
    if bottom_card == get_big_joker_value(deck):
        bottom_card -= 1
        
# copy the cards to be moved into top stack and remove them from deck
    for i in deck:
        if deck.index(i) < bottom_card:
            top_stack.append(i)
    for i in top_stack:
        deck.remove(i)
# insert the top stack just above the last card
    for i in range(len(top_stack)):
        deck.insert(len(deck)-1,top_stack[i])
        
def get_card_at_top_index(deck):
    """(list of int) -> int
    
    reads the value of the card on the top of the deck find the next value by using
    the value of top card as the index and return that value
    
    >>>get_card_at_top_index([10,11,12,13,14,15,1,2,7,8,9,3,4,5,6])
    9
    
    """
    top_card = deck[0]
    if top_card == get_big_joker_value(deck):
        top_card -= 1
    return deck[top_card]

def get_next_keystream_value(deck):
    """(list of int) -> int

    run through the encryption algoritm and return the value that we get from
    the algorithm
    
    >>>get_next_keystream_value([1,4,7,10,13,16,19,22,25,28,3,6,9,12,
    15,18,21,24,27,2,5,8,11,14,17,20,23,26])
    11
    """
    
    value = get_small_joker_value(deck)
    # a while loop to ensure the 
    while value == get_small_joker_value(deck) or value == get_big_joker_value(deck):
            move_small_joker(deck)
            move_big_joker(deck)
            triple_cut(deck)
            insert_top_to_bottom(deck)
            value = get_card_at_top_index(deck)   
    return value
def process_messages(deck,message,process):
    """(list of int, list of str, str) -> list of str
    
    return a list of processed message depending on the input for the process
    parameter
    
    >>>process_messages([1,2,3,4,5,6],["my name" , "is" , "Jeff"],'e')
    ['PBOEOH', 'JV', 'MIIH']
    >>>process_messages([1,2,3,4,5,6],['PBOEOH', 'JV', 'MIIH'],'d')
    ['MYNAME', 'IS', 'JEFF']
    
    """
    unprocessed_message = []
    processed_message = []

    for i in message:
        j = clean_message(i)
        unprocessed_message.append(j)
        
    if process == ENCRYPT:      
        for i in unprocessed_message:
            message_holder = ''   
            for j in range(len(i)):
                #encript each letter in j
                message_holder += encrypt_letter(i[j],
                                                 get_next_keystream_value(deck))
            processed_message.append(message_holder)
    elif process == DECRYPT:
        for i in unprocessed_message:
            message_holder = ''   
            for j in range(len(i)):
                #decripts each letter i
                message_holder += decrypt_letter(i[j],
                                                 get_next_keystream_value(deck))
            processed_message.append(message_holder)
    return processed_message

def read_messages(file):
    """(file open for reading) -> list of str
    """
    message = []
    a = file.readline()
    while a != '':
        message.append(a.strip())   
        a = file.readline()
     
    return message
    
def is_valid_deck(deck):
    """(list of int) -> bool
    
    return true if the deck is a list of interger from 1 to the length of the 
    deck without repeating
    
    >>>is_valid_deck([1,1,3,4,5])
    False
    >>>is_valid_deck([5,2,4,3,1])
    True
    """
    i = 1
    valid_deck = []
    while i <= len(deck):
        valid_deck.append(i)
        i += 1
    sort_deck = deck + []
    sort_deck.sort()
    return valid_deck == sort_deck
    
def read_deck(file):
    """(file open for reading) -> list of int
    """
    deck = []
    
    line_of_numbers = file.readline()
    while line_of_numbers != '':
        numbers = line_of_numbers.split()
        for i in numbers:
            deck.append(int(i))
        line_of_numbers = file.readline()
    
    return deck