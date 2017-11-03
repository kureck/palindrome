# Palindrome minimum base number - How to use

## Requirements

1. Python 3.5
2. git
3. virtualenv
4. Linux ou Mac

### Installation

Go to a directory of your choice to create a virtual environment using virtualenv for Python 3.5

```
virtualenv palindrome
```

### How to run the code

```
cd palindrome
source bin/activate
git clone https://github.com/kureck/palindrome
cd palindrome
pip install -r requirements.txt
pytest -vv # to run tests
python main.py # to run code
```
---

## Description
A Python program which determines the smallest base (greater than or equal to 2) in which the first 1000 positive decimal integers are palindromes.
