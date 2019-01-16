"""Generate Markov text from text files."""

from random import choice


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

    # chains[None] = None
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    ###########
    tuple_key = list(chains.keys())[0]
    
    while chains[tuple_key] != None:

        while len(words) == 0:

            #tuple_key = list(chains.keys())[0]
            value0 = tuple_key[0]
            value1 = tuple_key[1]

            words.append(value0)
            words.append(value1)

            value2 = choice(chains[tuple_key])

        else:
            words.append(value1)

        if value2 == None:
            break

        else:
            tuple_key = tuple([value1, value2])
            # print(value1, value2)





    ##############

    # # your code goes here
    # for key in chains:
    #     word1 = key[0]
    #     value1 = key[1]
    #     values_list = 
    #     value2 = choice(values_list)
        
    #     next_tuple = tuple([value1, value2])
    #     # print(next_tuple)

    #     if next_tuple in chains:

    #         random_item = choice(chains[next_tuple])
    #         #print(next_tuple, random_item)

    #         words.append(word1)
    #         words.append(value1)
    #         words.append(value2)
    #         words.append(random_item)


        
    return " ".join(words)


input_path = "green-eggs.txt"

# input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)





# ## SHH
# test_dict = {('a', 'fox?'): ['Would'],
#  ('Sam', 'I'): ['am?'],
#  ('could', 'you'): ['in', 'with', 'in', 'with'],
#  ('you', 'with'): ['a', 'a'],
#  ('box?', 'Would'): ['you'],
#  ('ham?', 'Would'): ['you'],
#  ('you', 'in'): ['a', 'a'],
#  ('a', 'house?'): ['Would'],
#  ('like', 'green'): ['eggs'],
#  ('like', 'them,'): ['Sam'],
#  ('and', 'ham?'): ['Would'],
#  ('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like'],
#  ('you', 'could'): ['you', 'you', 'you', 'you'],
#  ('a', 'mouse?'): ['Would'],
#  ('them,', 'Sam'): ['I'],
#  ('in', 'a'): ['house?', 'box?'],
#  ('with', 'a'): ['mouse?', 'fox?'],
#  ('house?', 'Would'): ['you'],
#  ('a', 'box?'): ['Would'],
#  ('green', 'eggs'): ['and'],
#  ('you', 'like'): ['green', 'them,'],
#  ('mouse?', 'Would'): ['you'],
#  ('fox?', 'Would'): ['you'],
#  ('eggs', 'and'): ['ham?']
# }

# print(len(test_dict))
# print(len(chains))
