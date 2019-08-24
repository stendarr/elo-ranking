# Usage
## Filename
You can either enter the filename when prompted or hard-code it in the source.

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

## Actual Ranking
You'll be presented with two options. Enter `1` or `2` to decide which is better. If you get bored press `Ctrl+C`.
