"""List Practice
Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.
    
    For example::
    
        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """
    for item in items:
        print(item)


def long_words(words):
    """Return words in input list that longer than 4 characters.
    
    For example::
    
        >>> long_words(["hello", "a", "b", "hi", "muffin", "muffin"])
        ['hello', 'muffin', 'muffin']
    
    (If there are duplicates, show both --- notice "muffin" appears
    twice in output)
    
    If no words are longer than 4 characters, return an empty list::
    
        >>> long_words(["all", "are", "tiny"])
        []
    """
    long_words_collection = []
    for word in words:
        if len(word) > 4:
            long_words_collection.append(word)

    return long_words_collection


def n_long_words(words, n):
    """Return words in list longer than `n` characters.
    
    For example::
    
        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "muffin", "muffin"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'muffin', 'muffin']
        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """
    words_of_a_certain_length = []
    for word in words:
        if len(word) > n:
            words_of_a_certain_length.append(word)

    return words_of_a_certain_length


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `min()`!
    
    For example::
    
        >>> smallest_int([-5, 2, -5, 7])
        -5
        >>> smallest_int([3, 7, 2, 8, 4])
        2
    
    If the input list is empty, return `None`::
    
        >>> smallest_int([]) is None
        True
    """

    if numbers == []:
        return None
    local_minimum = numbers[0]

    for number in numbers:
        if number < local_minimum:
            local_minimum = number
    return local_minimum


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `max()`!
    
    For example::
    
        >>> largest_int([-5, 2, -5, 7])
        7
        >>> largest_int([3, 7, 2, 8, 4])
        8
    
    If the input list is empty, return None::
    
        >>> largest_int([]) is None
        True
    """

    if numbers == []:
        return None
    local_maximum = numbers[0]

    for number in numbers:
        if number > local_maximum:
            local_maximum = number
    return local_maximum


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.
    
    For example::
    
        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]
   
    If any of the numbers are odd, make sure you don't round off
    the half::
   
        >>> halvesies([1, 5])
        [0.5, 2.5]
    """
    list_of_numbers_after_halving = []
    for number in numbers:
        number = int(number) / 2
        list_of_numbers_after_halving.append(number)

    return list_of_numbers_after_halving


def word_lengths(words):
    """Return the length of words in the input list.
    
    For example::
    
        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """
    word_lengths_list = []
    for word in words:
        length_of_the_word = len(word)
        word_lengths_list.append(length_of_the_word)
    return (word_lengths_list)


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.
    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.
    
    For example::
    
        >>> sum_numbers([1, 2, 3, 10])
        16
    
    Any empty list should return the sum of zero::
    
        >>> sum_numbers([])
        0
    """

    if numbers == []:
        return 0

    sum_so_far = 0
    for number in numbers:
        sum_so_far = sum_so_far + number

    return sum_so_far


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.
    
    For example::
    
        >>> mult_numbers([1, 2, 3])
        6
    
    Obviously, if there is a zero in input, the product is zero::
    
        >>> mult_numbers([10, 20, 0, 50])
        0
    
    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::
    
        >>> mult_numbers([])
        1
    """
    if 0 in numbers:
        return 0

    if numbers == []:
        return 1

    product = 1
    for number in numbers:
        product = product * number

    return product


def join_strings(words):
    """Return a string of all input strings joined together.
    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.
    
    For example::
    
        >>> join_strings(["spam", "spam", "muffin", "balloonicorn"])
        'spamspammuffinballoonicorn'
    
    For an empty list, you should return an empty string::
    
        >>> join_strings([])
        ''
    """

    if words == "":
        return ''

    all_the_strings = ""
    for word in words:
        all_the_strings = all_the_strings + word
    return all_the_strings


def average(numbers):
    """Return the average (mean) of the list of numbers given.
    
    For example::
    
        >>> average([2, 4])
        3.0
    
    This should handle cases where the result isn't an integer::
    
        >>> average([2, 12, 3])
        5.666666666666667
    
    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.
    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """

    if numbers == []:
        return None

    dividend = len(numbers)
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers = sum_of_numbers + number

    quotient = sum_of_numbers / dividend
    return quotient


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".
    
    For example::
     
        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'
    
    If there's only one thing in the list, it should return just that
    thing, of course::
   
        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """

    if len(words) == 1:
        return words[0]

    words_together_with_commas = ""
    for word in words:
        word = word + ", "
        words_together_with_commas = words_together_with_commas + word

    words_together_with_commas = words_together_with_commas[:-2]
    return words_together_with_commas


# def reverse_list_mimi(items):
#     """Return the input list, reversed.
#     **Do not use** the python function `reversed()` or the method
#     `list.reverse()`.

#     For example::

#         >>> reverse_list([1, 2, 3])
#         [3, 2, 1]
#         >>> reverse_list(["cookies", "love", "I"])
#         ['I', 'love', 'cookies']

#     You should do this without changing the original list::

#         >>> orig = ["apple", "berry", "cherry"]
#         >>> reverse_list(orig)
#         ['cherry', 'berry', 'apple']
#         >>> orig
#         ['apple', 'berry', 'cherry']
#     """

#     new_order_list = [None for item in items]
#     print(new_order_list)

#     for i, word in enumerate(items):
#         print(f"word #{-(i+1)} is {word}")
#         new_n = (-(i + 1))
#         new_order_list[new_n] = word

#     return (new_order_list)

# items = ["cookies", "love", "really", "I"]
# print(reverse_list_mimi(items))


def reverse_list(items):
    """Return the input list, reversed.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> reverse_list([1, 2, 3])
        [3, 2, 1]
        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']
    
    You should do this without changing the original list::
    
        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """
    reversed_list = []
    n = len(items)

    for index in range(n - 1, -1, -1):
        # print(number)
        reversed_list.append(items[index])
        # print(reversed_list)
    return reversed_list


def reverse_list_in_place(items):
    """Reverse the input list `in place`.
    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]
        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """
    n = len(items)
    for index in range(0, (n // 2)):
        temp = items[index]
        items[index] = items[n - index - 1]
        items[n - index - 1] = temp


def duplicates(items):
    """Return list of words from input list which were duplicates.
    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.
   
    For example::
   
        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']
        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]
   
    You should do this without changing the original list::
   
        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']
        >>> orig
        ['apple', 'apple', 'berry']
    """
    items_seen_already = []
    seen_a_second_time = []
    for item in items:
        if item in items_seen_already:
            seen_a_second_time.append(item)
        elif item not in items_seen_already:
            items_seen_already.append(item)
    finalized_list = []
    for item in seen_a_second_time:
        if item not in finalized_list:
            finalized_list.append(item)
    return finalized_list


"""use ordered = sorted(finalized_list)"""


def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.
    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.
    **DO NOT** use the `list.index()` method.
    
    For example::
    
        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]
    
    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")
    
    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::
    
        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]
    
    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """
    index_of_letter = 0
    indices_of_letter = []
    for word in words:
        if letter in word:
            index_of_letter = word.index(letter)
            indices_of_letter.append(index_of_letter)
        elif letter not in word:
            indices_of_letter.append(None)
    return indices_of_letter


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")

#         What is an algorithm? Provide some examples, both in the context in of computer science and beyond.
# >>>I'm not super sure this is something we learned yet, but my understanding is that it is a method by which to approach a problem.
# An example would be FIFO, first in first out, where you process something in the order in which it arrives
# Another example would be Dijkstra's algorithm which searches for the shortest path between two points, kind of like Uber.

# What is a heuristic? How do they relate to algorithms?

#we didn't learn this but according to the internet a heuristic algorithm is a procedure that determines near optimal solutions to an optimization problem.
# however, this is achieved by trading optimality for completeness, accuracy or prevision for speed.

# What is the brute force method? What are some problems with it?

#we also didn't learn this in class, but I understand it to be kind of approaching a problem by means of an inelegant solution at first just to get it solved.
#looked it up and I was wrong. it is actually looking at every possible solution, rather than trying to solve for the optimal solution
#an example would be if you ahve a lock and you don't know the combo, trying every combo one by one.
#the problem is that it relies on sheer computing power rather than efficiency.

# What is version control? How is it different than simply saving a file?

#version control is the means by which developers can coordinate with one another on the same piece of code.  (or a single developer can coordinate with themself over different computers/times)
#saving a file simply means that the progress has locally been saved in the current folder.
#however, with version control, you can make changes to a piece of code locally and then decide whether or not to push the code to the main branch.
#that way, multiple people can be working on the same piece of code, and if they work on the same section within the code they can have a conversation about which version to use
#it also helps back up code so that even if your computer in stolen on the BART, you have not lost all of your progress.

# What’s the difference between Git and Github?
#Github uses Git to function; Github is a company, Git is an open source repository sharing & storing system

# Git commands to know:

# git log
#tells you all the changes that were made to the repository, by whom, when.

# git init
#this creates an empty git repository.

# git status
#this tells you what the status of the code that you're currently working on is, relative to other versions it may be connected to.
#for example, if you have not pushed your changes, or not committed your changes, it will tell you so. if the main branch is ahead of the lcoal branch, it will tell you that too.

# git add
#this will add one or more files (you can specify) to the queue so that you don't have to add all of them at once, only the ones you specify.

# git commit with -a and -m
#the a just means "all" and the m just means "memo"(??) -- after m you should write your comment that describes the code in the present tense in an active verb descriptively.

# git remote add
#I had to refresh my mind on this one, but "Git remote add" will create a new connection record to a remote repository.

# git remote -v
#I also had to refresh my mind on this one; "To check what the git thinks the remote(s) is/are; the v stands for verbose, which asks for a bit more information"

# git push

# What does the file .gitignore do? What is the content of the .gitignore file?

# What are some files that git should generally ignore?

# How can you tell whether a file is being ignored by git or not?

# If you git add a secret file, is it possible to remove that file from the history of git?

# Why is using the command line important?

# What is the prompt in the context of the command line?

# Shell commands to know:

# ls - list (lists the contents of the directory)

# pwd - (print working directory - prints where you currently are)

# cp -

# mv

# cd

# mkdir

# rm

# man

# any command with --help

# CTRL-D and CTRL-C

# What’s the difference between relative and absolute paths?

# What’s the difference between parameters and arguments?

# What’s the difference between return, break, and print?

# What does a function return if it doesn’t have a return statement?

# What is a default parameter?

# What is scope? What is function scope?

# What are some important Python style considerations for writing functions?

# Python list methods/functions to know:

# sorted()

# .sort()

# .append()

# .extend()

# How to index a list

# How to slice a list

# How to loop over a list

# Using range(len(some_list))

# Using a counter and indexing the list

# Without using either of the above (just a for-loop)

# What is mutability?

# How is Python memory different than C memory? How are Python variables different than “classic” variables?

# What is garbage collection?

# What is the id function? What does the comparator is do in Python?

# What are sets good for?

# Set methods to know:

# .add()

# len()

# .remove()

# How to create a set

# How to check if something is in a set

# What are tuples good for?

# How do you create a tuple?

# How to index a tuple
