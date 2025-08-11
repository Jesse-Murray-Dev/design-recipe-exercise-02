# {{PROBLEM}} Function Design Recipe
## 1. Describe the Problem

_As a user_
_so that I can improve my grammar_
_I want to verify that a text starts with a capital letter and ends with a_ _suitable sentence-ending punctuation mark._

## 2. Design the Function Signature

```python
def check_grammar(text):
    # Parameters:
        # text: a string to represent human readble text
    
    # Returns:
        # Boolean: True if valid, false if otherwise

    # Side effects:
        # None
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._
```python
"""
Given a sentence which starts with 
a uppercase and ends in a fullstop 
Return True
"""
check_grammar("Hello, I am Jesse.") => True

"""
Given a sentence which starts with 
a uppercase and ends in a question mark 
Return True
"""
check_grammar("Hello, are you James?") => True

"""
Given a sentence which starts with 
a uppercase and ends in a exclamation mark 
Return True
"""
check_grammar("Meowth, that's right!") => True

"""
Given a sentence which starts with
a uppercase but does not have a fullstop
or other final punctuation
Return False
"""
check_grammar("Hello, I am Jesse") => False

"""
Given a sentence which starts with 
a uppercase and ends in a comma 
Return False
"""
check_grammar("Hello, I am Jesse,") => False

"""
Given a sentence which starts with 
a uppercase and ends in a colon 
Return False
"""
check_grammar("Hello, I am Jesse:") => False

"""
Given a sentence which starts with
a lowercase and ends in a fullstop
Return False
"""
check_grammar("hello, I am Jesse.") => False

"""
Given a sentence which starts with
a lowercase and does not have a fullstop
Return False
"""
check_grammar("hello, I am Jesse") => False
"""
Given an empty string
Raise an error
"""
check_grammar("") => "I have nothing to check"
```