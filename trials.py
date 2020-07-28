"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
# print each item in the array

    for i in items:
        print(i)

# in console type output_all_items(argument in form of list you want to unpack_)
# test case provided with is outputAllItems([1, 'hello', true]) for JavaScript
# test case provided in Python requires quotes around true
# or true to be capitalized
# outputAllItems([1, 'hello', 'true']) 
# outputAllItems([1, 'hello', True]) 

# Commenting changed to Python's hash tag
# // Given an array of numbers, return an array of all even numbers.
# //
# // Ex.:
# //   > getAllEvens([7, 8, 10, 1, 2, 2]);
# //   [8, 2, 2]
def get_all_evens(nums):
    evenNums = []
    # removed const and semi-colon at end of list
    for num in nums:
    # removed parentheses, const and curly brace and added colon, and chenged of into in
        if num % 2==0:
    # changed spaces from 2 to 4 for indent; removed parentheses, removed one of 
    # the equal signs as no truthy in python; removed curly brace and added colon
            evenNums.append(num)
    # continued using 4 space indents, replaced push with append; removed semi-colon
    # removed additional curly braces
    return evenNums
    #returned without semi-colon or even curly braces.

# Changed comments to Python hash
# // Given a list, return all elements at odd numbered indices.
# Changed array to list
def get_odd_indices(items):
    i=0
    # set i to 0
    result = []
    # removed const and semi-colon from list declaration
    # added While True
    while True:
        if i < len(items):

        # changed idx to i; added statement to iterate over length of list 

                if i % 2 != 0:

        # removed all curly braces            
                    result.append(items[i])

        # changed push to append     

                i += 1

        # increment count

    return result

    #outdent return result

# // Ex.:
# //   > getOddIndices([1, 'hello', true, 500]);
# //   ['hello', 500]        
# call get_odd_Indices([1, 'hello', true, 500])


# This is where we stopped  for lunch.
# We agreed to save to github and add examples; re-comment;
# remove the above removed elements (function(def), const, ;, curly braces; push(append); === to ==); save test cases
# pre-re-pairing.
# new items that come up are:
# let
# console.log
#` $ f'
# // Given an array, output a numbered list.
# camelcase versus _
# length
# no step for range in JavaScript vs Python
# toUpperCase versus upper()
# toString versus str()

def print_as_numbered_list(items):

  let i = 1

  for item in items:

      console.log(`${i}. ${item}`)

      i += 1

# // Ex.:
# // > printAsNumberedList([1, 'hello', true]);
# // 1. 1
# // 2. hello
# // 3. true

# // Return an array of numbers in a certain range.


def get_range(start, stop):
# // Ex.:
# // > getRange(0, 5);
# // [0, 1, 2, 3, 4]
# 
# // > getRange(1, 3);
# // [1, 2]
  nums = []

  for (let num = start; num < stop; num += 1):

      nums.append(num)
  
# // Given a string, return a string where vowels are replaced with '*'.
# 

def censor_vowels(word):

  chars = []

  for letter of word:

      if ('aeiou'.includes(letter)):
          chars.append('*')

      chars.append(letter)

  return chars.join('')
# // Ex.:
# //   > censorVowels('hello world');
# //   'h*ll* w*rld'

# // Given a string in snake case, return a string in upper camel case.


def snake_to_camel(string):

  camelCase = []

  for word of string.split('_'):
    
    camelCase.append(`${word[0].toUpperCase()}${word.slice(1)}`)

  return camelCase.join('')

# // Ex.:
# //   > snakeToCamel('hello_world');
# //   'HelloWorld'

# // Return the length of the longest word in the given array of words.


def longest_word_length(words):

    let longest = words[0].length

    for word of words:
      if longest < word.length:
        longest = word.length

    return longest

# // Ex.:
# //   > longestWordLength(['hello', 'world']);
# //   5
# 
# //   > longestWordLength(['jellyfish', 'zebra']);
# //   9

# // Truncate repeating characters into one character.


def truncate(string):

    result = []

    for char in string:

        if result.length == 0 || char != result[result.length - 1]:

            result.append(char)

    return result.join('')

# // Ex.:
# //   > truncate('aaaabbbbcccca');
# //   'abca'
#
# //   > truncate('hi***!!!! wooow');
# //   'hi*! wow'


# // Return true if all parentheses in a given string are balanced.



def has_balanced_parens(string):

  let parens = 0

  for char of string:

    if char == '('):

        parens += 1
        
    else if:

        char == ')'

        parens -= 1

    if parens < 0:

        return false

    return parens < 0

# // Ex.:
# // > hasBalancedParens('()');
# // true
# 
# // > hasBalancedParens('((This) (is) (good))');
# // true
# 
# // > hasBalancedParens('(Oh no!)(');
# // false


# // Return a compressed version of the given string.


def compress(string):

  compressed = []

  let currChar = ''

  let charCount = 0

  for char in string:

      if char != currChar:

          compressed.append(currChar)

      if charCount > 1:

          compressed.append(charCount.toString())

      currChar = char

      charCount = 0

    charCount += 1

  compressed.append(currChar)

      if charCount > 1:
          compressed.append(charCount.toString())

  return compressed.join('')

    # // Ex.:
# //   > compress('aabbaabb');
# //   'a2b2a2b2'
# 
# // If a character appears once, it shouldn't be followed by a number:
# //   > compress('abc');
# //   'abc'
# 
# // The function should handle all types of characters:
# //   > compress('Hello, world! Cows go moooo...');
# //   'Hel2o, world! Cows go mo4.3'