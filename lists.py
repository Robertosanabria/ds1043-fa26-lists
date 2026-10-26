"""lists

Exercises for exploring lists
"""

from pathlib import Path


def clamp(a: list[int], low: int = 0, high: int = 10) -> None:
    """Modify the values of a to be low or high when outside the range."""
    for i in range(len(a)):
        if a[i] < low:
            a[i] = low
        elif a[i] > high:
            a[i] = high


def reverse(a: list) -> None:
    """Reverses the list a in place."""
    for i in range(len(a) // 2):
        j = len(a) - 1 - i
        a[i], a[j] = a[j], a[i]

# Read the following function and write out your prediction of what it will do
# in the following situations:
# - create a list named `susan`. Call `hop_in` multiple times, passing `susan`
#   as the `pouch` argument
# - simply call `hop_in` multiple times without specifying a `pouch`
#
# Now run this in the console. Was your prediction correct?
def hop_in(name: str, pouch: list[str] = []) -> None:
    if len(pouch) > 0:
        siblings = f' with their siblings: {", ".join(pouch)}'
    else:
        siblings = ''
    print(f"{name} hops into their mother's pouch{siblings}")
    pouch.append(name)


# You can point this function a folder on your computer and it will list
# all the files in it and any subfolders. Experiment with how `items` is
# built (Stack vs Queue) and see how the ordering changes.
def list_files(folder: str) -> list[str]:
    """Create a list of all files under `root`"""
    root = Path(folder)
    filenames: list[str] = []
    items: list[Path] = []
    while len(items) > 0:
        item = items.pop()
        if item.is_dir():  # if the item is a folder...
            # add the contents of item.iterdir() to items
            items.extend(item.iterdir())
        else:
            # add item.name to filenames
            filenames.append(item.name)
    return filenames


# Implement this function using a list as a stack to find matching parentheses
# if a match is not found, raise a ValueError with a helpful message (like the
# index of the unmatched parenthesis)
def match_parentheses(line: str) -> list[str]:
    """Given a string containing an expression, return a list of subexpressions delineated by parenthesis"""
    stack = []
    expressions = []

    for i in range(len(line)):
        if line[i] == "(":
            stack.append(i)

        elif line[i] == ")":
            if len(stack) == 0:
                raise ValueError(
                    f"Unmatched closing parenthesis at index {i}"
                )

            start = stack.pop()
            expressions.append(line[start + 1:i])

    if len(stack) > 0:
        raise ValueError(
            f"Unmatched opening parenthesis at index {stack[-1]}"
        )

    return expressions

