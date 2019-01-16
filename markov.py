"""Generate Markov text from text files."""

from random import choice, sample

import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text_file = open(file_path)
    text = text_file.read()
    # print(type(text))
    # print(text)

    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words = text_string.split()

    words.append(None)

    for index in range(len(words) - 2):
        word_tuple = tuple(words[index:index + 2])

        third_word = words[index + 2]

        if word_tuple in chains:
            # Get a list
            values_list = chains[word_tuple]
            values_list.append(third_word)

        else:
            # Make a new list
            new_list = [third_word]
            chains[word_tuple] = new_list

    return chains

def make_chains2(text_string1, text_string2):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words1 = text_string1.split()
    words2 = text_string2.split()

    words1.append(None)
    words2.append(None)

    for index in range(len(words1) - 2):
        word_tuple = tuple(words1[index:index + 2])

        third_word = words1[index + 2]

        if word_tuple in chains:
            # Get a list
            values_list = chains[word_tuple]
            values_list.append(third_word)

        else:
            # Make a new list
            new_list = [third_word]
            chains[word_tuple] = new_list

    for index in range(len(words2) - 2):
        word_tuple = tuple(words2[index:index + 2])

        third_word = words2[index + 2]

        if word_tuple in chains:
            # Get a list
            values_list = chains[word_tuple]
            values_list.append(third_word)

        else:
            # Make a new list
            new_list = [third_word]
            chains[word_tuple] = new_list

    #  print("chains", chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    # punctuation = "!.,?()"  # Punctuation checker feature

    tuple_key = list(chains.keys())[0]
    value0 = tuple_key[0]
    words.append(value0)
    
    while chains[tuple_key] != None:

        value1 = tuple_key[1]
        words.append(value1)

        value2 = choice(chains[tuple_key])

        # if value2[-1] in punctuation: # Punctuation checker feature
        if value2 == None:
            # words.append(value2) # Punctuation checker feature
            break

        else:
            tuple_key = tuple([value1, value2])

        
    return " ".join(words)


def make_text_ngrams(chains, n):
    """Return text from chains.
    https://docs.python.org/3/library/random.html

    chains is dictionary of (tuple) : [list...] key value pairs
    n is the number of items in the tuple.

    random.sample https://docs.python.org/3/library/random.html
    """

    words = []

    tuple_key = list(chains.keys())[0]
    

    value0 = tuple_key[0]
    # if value0[0].isupper(): # Further Study feature 3
    
    words.append(value0)
    
    while chains[tuple_key] != None:

        value1 = tuple_key[1]
        words.append(value1)

        # value2 = choice(chains[tuple_key])
        m = max(n - 1, len(chains[tuple_key]))
        random_list = sample(chains[tuple_key], m)

        print("N: ", n)
        print("Random list: ", random_list)
        print("Random list type: ", type(random_list))

        if None in random_list:
            break

        else:
            # tuple_key = tuple([value1, value2]) # New tuple
            tuple_key = tuple(random_list)

        
    return " ".join(words)



# input_path = "green-eggs.txt"
# input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1])
# input_text1 = open_and_read_file(sys.argv[1]) ##F4
# input_text2 = open_and_read_file(sys.argv[2]) ##F4

# Get a Markov chain
chains = make_chains(input_text)
# chains2 = make_chains2(input_text1, input_text2) ##F4

# Produce random text
random_text = make_text(chains)
# random_text2 = make_text(chains2) ##F4

random_text_n = make_text_ngrams(chains, 4)##F3
# print(random_text2)

# print(random_text)
# print(random_text2) ##F4
print(random_text_n) ##F3




