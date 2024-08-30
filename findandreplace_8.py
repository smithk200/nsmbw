def replace_characters(input_string, replacements):
    """
    Function to replace characters in the input string based on a replacements dictionary.

    :param input_string: The input string to process.
    :param replacements: Dictionary where keys are characters to find, and values are replacement strings.
    :return: A new string with characters replaced according to the replacements dictionary.
    """
    replaced_parts = []

    # Iterate through each character in the input string
    for char in input_string:
        if char in replacements:
            replaced_parts.append(replacements[char])

    # Join the replaced parts into a single string
    result_string = "|".join(replaced_parts) + "|%"

    return result_string

# Example replacements dictionary
replacements = replacements = {
    "a" : "108",
    "b" : "109",
    "c" : "110",
    "d" : "111",
    "e" : "112",
    "f" : "113",
    "g" : "114",
    "h" : "115",
    "i" : "116",
    "j" : "117",
    "k" : "118",
    "l" : "119",
    "m" : "120",
    "n" : "121",
    "o" : "122",
    "p" : "123",
    "q" : "124",
    "r" : "125",
    "s" : "126",
    "t" : "127",
    "u" : "128",
    "v" : "129",
    "w" : "130",
    "x" : "131",
    "y" : "132",
    "z" : "133",
    "A" : "134",
    "B" : "135",
    "C" : "136",
    "D" : "137",
    "E" : "138",
    "F" : "139",
    "G" : "140",
    "H" : "141",
    "I" : "142",
    "J" : "143",
    "K" : "144",
    "L" : "145",
    "M" : "146",
    "N" : "147",
    "O" : "148",
    "P" : "149",
    "Q" : "150",
    "R" : "151",
    "S" : "152",
    "T" : "153",
    "U" : "154",
    "V" : "155",
    "W" : "156",
    "X" : "157",
    "Y" : "158",
    "Z" : "159",
    "1" : "160",
    "2" : "161",
    "3" : "162",
    "4" : "163",
    "5" : "164",
    "6" : "165",
    "7" : "166",
    "8" : "167",
    "9" : "168",
    "0" : "169",
    "!" : "170",
    "?" : "171",
    "." : "172",
    "," : "173",
    "'" : "174",
    '"' : "175",
    "(" : "176",
    ")" : "177",
    ":" : "178",
    ";" : "179",
    "@" : "180",
    "&" : "181",
    "_" : "182",
    "-" : "183",
    "+" : "184",
    "=" : "185",
    "#" : "186",
    " " : "103",
}

# Input string
input_str = "Mario"

# Replace characters and construct final string
result = "ReggieClip|0:0:{}:1:35:17:1:1|%".format(replace_characters(input_str, replacements))

# Print the result
print(result)
