# What? Why?

This is a rating system in Python based on the [Elo rating system](https://en.wikipedia.org/wiki/Elo_rating_system) created by Arpad Elo. You can use it on lists and do all kinds of fun stuff, like finding out what your favourite vegetable is.

_But why use the Elo system? Surely you can rank vegetables in O(n log(n)) time instead?_

The Elo system is designed to work over longer periods of time. Let's say cabbage is your favourite vegetable but one day you wake up and feel a sudden urge to eat some lettuce. In that moment you may rank lettuce higher than cabbage but in the grand scheme of things cabbage is still your favourite vegetable. Simple ranking-based rating systems do not take this into account.

# Usage

## Filename
You can either enter the filename when prompted or hard-code it in the source. You can enter the filename without the `.txt` suffix. If you're feeling particularly cool you can pass the filename as a commandline argument:
`python3 elo.py test_list`

If you want to reset your list you can add `init` as an argument when running the command: `python3 elo.py test_list init`

## File Format
You can use this script on any text list in the following format:

    Apple, 0, 1000,
    Orange, 8, 1200,
    Pear, 3, 998,
    Peach, 4, 982,
    Melon, 3, 899,
    Lemon, 1, 1002,

The first number (counter) is the amount of times this item has been questioned against another item and the second number (elo) is the Elo rank

The script will also recognize lists in this format:

    Grapes
    Apricot
    Watermelon
    Pineapple
    Papaya
    Strawberry

If the list solely consists of names, the script will initialise it with a counter of 0 and an Elo rank of 1000.

Mixed lists are also permitted and the comma at the end of the line is not necessary - a newline however is necessary in any case. If there are too many newlines, the program will delete all empty lines.

Another legal example:

    Cabbage, 0, 1000,
    Ginger
    Tomato, 0, 1002
    Carrot
    Beans

    Potato, 3, 990

## Actual Rating
You'll be presented with two options. Enter `1` or `2` to decide which is better. If you're undecided enter `3` and when you get bored press `Ctrl+C`.
