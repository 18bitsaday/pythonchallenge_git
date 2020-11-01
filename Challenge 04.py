import urllib.request
import string

count = 1
nothing = '12345'

count = 84
nothing = '3875'

count = 139
nothing = '82682'

# count = 249
# nothing = 'peak.html'
while count <= 400:
    with urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing) as response:
        html = response.read()
    text = html.decode("utf-8")
    cleanStr = text[:]
    print(cleanStr)
    onlyNumbers = ""
    for character in cleanStr:
        # print(character)
        if character.isdigit():
            onlyNumbers += character
    if (nothing) == '16044':
        onlyNumbers = '8022'
    if nothing == '82682':
        onlyNumbers = '63579'

    print(count, ":", onlyNumbers)
    count += 1
    nothing = str(onlyNumbers)
    # print(string)
    # nothing = string[-5:]
    # print(nothing)
