# Algorithm Exercises


## Overview

This repo is dedicated to practicing algorithm solutions. It is broken into sections based on the nature of the problem, but all problems are supplemented with additional metadata, so a docstring would look like this:

```python
# binary_trees.py
def some_function(var: int) -> int:
    """
    Title: XXX
    Origin: link-to-website/book
    Difficulty: EASY|MEDIUM|HARD
    Topics: BINARY-TREE,RECURSION
    Description: XXX
    Notes: my notes...
    Supplements:
        - tests/test_binary_trees.test_some_function
        - notebooks/binary_trees.some_function
    Args:
         var (int): XXX
    Returns:
        (int) XXX
    """
    ...
```

Each function has a corresponding test associated with it. Some concepts have supplementary material covered in the notebooks.

## Setup

This project requires Python 3.9.11 to run. Set up your environment with the following:

```shell
brew install pyenv
brew install pyenv-virtualenv
pyenv install 3.9.11
pyenv virtualenv 3.9.11 algo
pytest local algo
exec "$SHELL"
pip install --upgrade pip
pip install -r requirements.txt
pre-commit install
tox  # this will run the tests
```
