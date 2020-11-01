import string

alfabet = string.ascii_lowercase

alfabet += alfabet

print(alfabet)
keyValue = 2
solution = ''
encrypted = 'map g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb\
             rfyr q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

for letter in encrypted:
    if letter in alfabet:
        solution += alfabet[alfabet.find(letter)+keyValue]
    else:
        solution += ' '


print(encrypted)
print(solution)