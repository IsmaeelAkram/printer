# Printer
Printing functions for my Python projects.

## Installation & Usage
```sh
pip install git+https://github.com/ismaeelakram/printer
```
With emojis:
```python
>>> from printer import *
>>> good("Hey!")
[👍][20:33:57] Hey!
```
Without emojis:
```python
>>> from printer import *
>>> useEmojis(False)
>>> good("Hey!")
GOOD 20:35:05 Host scanned
```