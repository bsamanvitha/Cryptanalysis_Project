#!/usr/bin/python
text = "SIERRA-ZERO-JULIET-SIX-YANKEE-ONE-ROMEO-PAPPA-EIGHT-KILO-FIVE-UNIFORM-XRAY-XXX-BRAVO-VICTOR-TWO-FOUR-TANGO-MIKE-OSCAR-HOTEL-DELTA-QUEBECK-FOXTROT-ALPHA-YYY-LIMA-INDIA-THREE-WISKEY-NOVEMBER-ECHO-CHARLIE-GOLF-ZULU"
XXX = ""
YYY = ""
num = "02192404240811270719140602241104010404040830181419040718071412122419071917091206240627010706270414300408091817060212081914040614080908171814042718180830060408090714170617271709243024090912081917091427012404113007060419062409011109180619111802270619"
decodedText = []
decodedText1 = []
decodedText2 = []

numbers = {
    'ZERO': '0',
    'ONE': '1',
    'TWO': '2',
    'THREE': '3',
    'FOUR': '4',
    'FIVE': '5',
    'SIX': '6',
    'SEVEN': '7',
    'EIGHT': '8',
    'NINE': '9'
}


# print text
################################################
def split_str(seq, chunk, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(split_str(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst


num = split_str(num, 2)
# print num
################################################

#####read the numbers and replace with numbers with reference to hash map
decodedText = text.strip().split('-')
# print decodedText
for i in range(0, len(decodedText)):
    # print "IN FOR\n"
    for key, value in numbers.items():
        if decodedText[i] == key:
            decodedText[i] = value
    # else:
    # print "Not Found\n"
# print decodedText
decodedText1 = list(decodedText)
decodedText2 = list(decodedText)

'''
print "\n1: "
print decodedText1
print "\n2: "
print decodedText2
'''

######get the 2 strings with respect to 2 values of XXX and YYY
xxx1 = "7"
yyy1 = "9"
for j in range(0, len(decodedText1)):
    # print "IN FOR 1\n"
    if decodedText1[i] == "XXX":
        decodedText1[i] = xxx1
    if decodedText1[i] == "YYY":
        decodedText1[i] = yyy1
# print "\n1: "
# print decodedText1

xxx2 = "9"
yyy2 = "7"
for k in range(0, len(decodedText2)):
    # print "IN FOR 2\n"
    if decodedText2[i] == XXX:
        decodedText2[i] = xxx2
    if decodedText2[i] == YYY:
        decodedText2[i] = yyy2

# print "\n2: "
# print decodedText2


# form the key to encrypt the final number with both the possibilities
finalText1 = []
for elements in decodedText1:
    # print len(decodedText1[j])
    # print len(elements)
    if len(elements) > 1:
        elements = elements[0]
        finalText1.append(elements)
        # print elements
        continue
    if len(elements) == 1:
        finalText1.append(elements)
# else:
# print "Its probably a num"
# print "\nFinal 1: "
# print finalText1
finalText2 = []
for elements in decodedText2:
    # print len(decodedText1[j])
    # print len(elements)
    if len(elements) > 1:
        elements = elements[0]
        finalText2.append(elements)
        # print elements
        continue
    if len(elements) == 1:
        finalText2.append(elements)
# else:
# print "Its probably a num"
# print "\nFinal 2: "
# print finalText1

###########################################
# forming encrypted number
finalNum1 = []
for elements in num:
    elements = finalText1[int(elements) - 1]
    finalNum1.append(elements)
print "\nFinal encrypt Num1: "
print finalNum1
finalNum2 = []
for elements in num:
    elements = finalText2[int(elements) - 1]
    finalNum2.append(elements)
print "\nFinal encrypt Num2: "
print finalNum2
