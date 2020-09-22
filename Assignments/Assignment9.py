import turtle
from string import punctuation

stop_words = {"a","am","an", "and","are", "as", "at",
              "be","but", "by", "for", "i", "if", "in", "into",
              "is", "it", "its", "my", "nor", "not", "of", "on",
              "or", "so", "than", "that", "the", "then", "this",
              "to", "too", "will", "with"}

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

def print_word_count(dictionary, word):
    print("Count of \"" + word + "\" is:", dictionary[word])

'''
The animate function needs to take in an x and y as arguments
because of how we are calling it from the main function.
Since it is being called when the mouse is clicked, it is
required to take the x,y location of the mouse at the time
of the click. You do not need to use the x,y for anything, so
just leave them here as parameters but you do not need to use 
them inside your function.
'''
def animate(x, y):
    # your code goes here
    
    return

def count_words(f):
    file = open(f, "r")
    words = file.read()
    stripped_words = strip_punctuation(words)
    words_list = stripped_words.split()
    words_list2 = list()
    for word in words_list:
        words_list2.append(word.lower())
    word_dict = {}
    for word in words_list2:
        word_dict[word] = words_list2.count(word)
    for word in stop_words:
        word_dict.pop(word, None)
    return word_dict
    
def find_max(d):
    max_list = []
    max_val = max(d.values())
    for word in d:
        if d[word] == max_val:
            max_tuple = word, d[word]
            return max_tuple
        #max_list.append(word)
    
def animate(a,b):
    deg = 0

    while True:
        for i in range(5):
            turtle.lt(180 + deg)
            turtle.lt(36 - deg)
            turtle.forward(100)
            deg += 2
        turtle.circle(10,10)
        turtle.clear()  


def main():
    find_max(count_words("raven.txt"))

    print_word_count(count_words("raven.txt"), find_max(count_words("raven.txt"))[0])
    print_word_count(count_words("raven.txt"), "raven")
    print_word_count(count_words("raven.txt"), "nevermore")
    # Part 1 - your code goes here



    # Part 2 - when the mouse is clicked in the turtle window,
    # call the animate() function to display a spinning star
    # ***DO NOT CHANGE THIS CODE***
    turtle.speed(0)
    turtle.hideturtle()
    turtle.onscreenclick(animate)
    turtle.done()

if __name__ == '__main__':
    main()
