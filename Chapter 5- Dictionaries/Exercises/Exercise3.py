# a glossary dictionary
glossary = {
    'loop': 'A control flow statement that allows code to be executed repeatedly based on a condition.',
    'function': 'A block of organized, reusable code that performs a specific task.',
    'variable': 'A named storage location in computer memory where data can be stored and accessed.',
    'list': 'A data structure that holds an ordered collection of items, which can be of different types.',
    'if statement': 'A statement that performs different actions depending on whether a condition is true or false.',
    # added more examples
    'dictionary': 'A data structure that stores key-value pairs, allowing efficient lookup, insertion, and deletion of elements.',
    'module': 'A file containing Python code that can be executed and imported into other Python files.',
    'class': 'A blueprint for creating objects, providing initial values for state (attributes) and implementations of behavior (methods).',
    'inheritance': 'The mechanism of basing an object or class upon another object (prototypal inheritance) or class (class-based inheritance), retaining similar implementation.',
    'exception': 'An event that occurs during the execution of a program that disrupts the normal flow of instructions. It is handled by exception handling mechanisms.'
}


for key, value in glossary.items(): # goes through the glossery and takes the key and values 
    print(key + ": " + value) #prints the key and value
    print()  # Insert a blank line between each word-meaning pair like \n