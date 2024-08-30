import re

def find_and_replace_numbers_standalone(input_string, replacements):
    """
    Function to find and replace all numbers in the input string according to the replacements dictionary,
    only if they are standalone (bound by colons).

    :param input_string: The input string to process.
    :param replacements: Dictionary where keys are the numbers to find, and values are the numbers to replace with.
    :return: A new string with all numbers replaced according to the replacements dictionary.
    """
    # Create a pattern from the keys of the replacements dictionary
    # This pattern matches any number that is standalone (bound by colons)
    pattern = '|'.join(r'(?<=:){}(?=:|$)'.format(re.escape(key)) for key in replacements)
    
    # Define the replacement function for re.sub
    def replace_match(match):
        # Extract the matched value (number)
        matched_value = match.group(0)
        # Replace it with the corresponding value from the replacements dictionary
        return replacements[matched_value]

    # Perform the replacements using re.sub
    modified_string = re.sub(pattern, replace_match, input_string)
    
    # Return the modified string
    return modified_string

def find_and_replace_string(input_string, replacements):
    """
    Function to find and replace substrings in an input string based on the replacements dictionary.

    :param input_string: The input string to process.
    :param replacements: Dictionary where keys are the substrings to find, and values are the substrings to replace with.
    :return: A new string with substrings replaced according to the replacements dictionary.
    """
    # Iterate through the replacements dictionary
    for old_value, new_value in replacements.items():
        # Replace each occurrence of the old value with the new value
        input_string = input_string.replace(old_value, new_value)
    
    # Return the modified string
    return input_string

# Define the replacements dictionary
replacements = {
    "A" : "108",
    "B" : "109",
    "C" : "110",
    "D" : "111",
    "E" : "112",
    "F" : "113",
    "G" : "114",
    "H" : "115",
    "I" : "116",
    "J" : "117",
    "K" : "118",
    "L" : "119",
    "M" : "120",
    "N" : "121",
    "O" : "122",
    "P" : "123",
    "Q" : "124",
    "R" : "125",
    "S" : "126",
    "T" : "127",
    "U" : "128",
    "V" : "129",
    "W" : "130",
    "X" : "131",
    "Y" : "132",
    "Z" : "133",
    "a" : "134",
    "b" : "135",
    "c" : "136",
    "d" : "137",
    "e" : "138",
    "f" : "139",
    "g" : "140",
    "h" : "141",
    "i" : "142",
    "j" : "143",
    "k" : "144",
    "l" : "145",
    "m" : "146",
    "n" : "147",
    "o" : "148",
    "p" : "149",
    "q" : "150",
    "r" : "151",
    "s" : "152",
    "t" : "153",
    "u" : "154",
    "v" : "155",
    "w" : "156",
    "x" : "157",
    "y" : "158",
    "z" : "159",
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

def replace(self):
    test = self
    string = ""
    numberlist = []
    stringlist = []
    xpos = 16
    ypos = 45
    reggieclip = "ReggieClip"
    percent = "%"
    for i in test:
        j = find_and_replace_string(i, replacements)
        if j == '1165116516167116516167116511651':
            j = '103'
        if j == '11651165161671165165116516167': #odd edge cases that don't resond to the normal replacements dictionary, for whatever reason. Test the string with "test" to see which symbols
            #should be replaced!
            j = '170'
        if j == '1165116516167116516511651':
            j = '172'
        if j == '11651165161671165165116511651':
            j = '173'
        if j == '1165116516167116516511653':
            j = '174'
        if j == '11651165161671165165116511653':
            j = '175'
        if j == '11651165161671165165165':
            j = '176'
        if j == '116511651616711651651165165':
            j = '177'
        if j == '11651165161671671165116516167':
            j = '181'
        if j == '1165116516167167116511651':
            j = '183'
        if j == '116511651616716711653':
            j = '184'
        if j == '1165116516167167165':
            j = '186'
        numberlist.append(j)
        #print j #still need to test things, maybe. Should be good for now.

    for i in range(len(numberlist)):
        xpos += 1
        if xpos >= 42:
            xpos = 17
            ypos += 1
        string = "|0:0:"+numberlist[i]+":1:"+str(xpos)+":"+str(ypos)+":1:1"
        stringlist.append(string)

    reggiestring = ''.join(stringlist) #''.join is a magic method! Very useful!
    return "ReggieClip" + reggiestring + "|%" #The finished product! Heck yeah!

# Perform the find and replace operation
# result = find_and_replace_string(input_string, replacements)
# Print the modified string
#print result
"""Mario, I'm fifty years old. It's that time where I have to check for colon cancer.
Mario, there's no good doctors for a hundred miles because of the inflation problem in the Mushroom Kingdom. I know you have some medical expertise, when you were
Doctor Mario. So, Mario, I have one favor to ask of you. Will you please check me for colon cancer?
"""
input_string = "Uh-oh..."
print replace(input_string)
print
print "ReggieClip|0:0:99:1:32:23:1:1|0:0:100:1:33:23:24:1|0:0:101:1:57:23:1:1|0:0:105:1:32:27:1:1|0:0:107:1:57:27:1:1|0:0:104:1:57:24:1:3|0:0:102:1:32:24:1:3|0:0:106:1:33:27:24:1|%"

