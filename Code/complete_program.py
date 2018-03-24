# File name:    Cryptanalysis_Project, complete_program
# Date created: 3/23/18
# Python v:     2.7

#!/usr/bin/python
'''
Book Cipher
'''

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
    if decodedText1[j] == "XXX":
        decodedText1[j] = xxx1
    if decodedText1[j] == "YYY":
        decodedText1[j] = yyy1
#print "\n1: "
#print decodedText1

xxx2 = "9"
yyy2 = "7"
for k in range(0, len(decodedText2)):
    # print "IN FOR 2\n"
    if decodedText2[k] == "XXX":
        decodedText2[k] = xxx2
    if decodedText2[k] == "YYY":
        decodedText2[k] = yyy2

#print "\n2: "
#print decodedText2

# form the key to encrypt the final number with both the possibilities
finalText1 = []
for elements in decodedText1:
    if len(elements) > 1:
        elements = elements[0]
        finalText1.append(elements)
        # print elements
        continue
    if len(elements) == 1:
        finalText1.append(elements)

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

###########################################
# forming encrypted number
print "\n################# Outputs of Book Cipher #################\n"

finalNum1 = []
for elements in num:
    elements = finalText1[int(elements) - 1]
    finalNum1.append(elements)
print "Final encrypt Num1: "
print ''.join(finalNum1) + '\n'
finalNum2 = []
for elements in num:
    elements = finalText2[int(elements) - 1]
    finalNum2.append(elements)
print "Final encrypt Num2: "
print ''.join(finalNum2)
print ''

'''
Caesar Cipher
'''
def caesarEncrypt(key_inp, hex_inp):
    YY = str(key_inp)[-2:]
    XX = str(key_inp)[0:2]
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = str(key_inp)
    hex_string = str(hex_inp)
    output_str = ""
    for eachChar in hex_string:
        try:
            digit = int(eachChar)
            output_str += str((digit - int(YY)) % 10)
        except:
            output_str += letters[(letters.index(eachChar) + int(XX)) % 26]
    return output_str

def caesarDecrypt(key_inp, hex_inp):
    YY = str(key_inp)[-2:]
    XX = str(key_inp)[0:2]
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = str(key_inp)
    hex_string = str(hex_inp)
    output_str = ""
    for eachChar in hex_string:
        try:
            digit = int(eachChar)
            output_str += str((digit + int(YY)) % 10)
        except:
            output_str += letters[(letters.index(eachChar) - int(XX)) % 26]
    return output_str

input1 = ''.join(finalNum1)
input2 = ''.join(finalNum2)

#print 'Input 1 for Caesar: ' + input1
#print 'Input 2 for Caesar: ' + input2 + '\n'

print "\n################# Outputs of Caesar Cipher #################\n"
print 'Outputs from input 1: '
print 'Output 1' + ": " + caesarDecrypt(1503, input1)  # 3 left = 7 right
rsa_input1 = caesarDecrypt(1503, input1)
print 'Output 2' + ": " + caesarDecrypt(1507, input1) + '\n' # 7 left
rsa_input2 = caesarDecrypt(1507, input1)
print 'Outputs from input 2: '
print 'Output 1' + ": " + caesarDecrypt(1503, input2)  # 3 left = 7 right
rsa_input3 = caesarDecrypt(1503, input2)
print 'Output 2' + ": " + caesarDecrypt(1507, input2)  # 7 left
rsa_input4 = caesarDecrypt(1507, input2)

rsa_input1 = int(rsa_input1,16)
#print rsa_input1
rsa_input2 = int(rsa_input2,16)
#print rsa_input2
rsa_input3 = int(rsa_input3,16)
#print rsa_input3
rsa_input4 = int(rsa_input4,16)
#print rsa_input4
'''
RSA Cipher
'''

'''
rsa_input1(First output of Caesar Cipher) contains a standard value of e=65537. we split the key as
n=501281908486219621910086584233925309600136539640088201223414043112175611
e=65537
c=455254144570149659309053721142936464401700360179699485409768697057718862
We use a online tool to factorise n
source: https://factordb.com/index.php
n= 501281908486219621910086584233925309600136539640088201223414043112175611
After Factorisation, we get:
p= "578455732137135466812346681323546443"
q= "866586465716584657165746753876546577"
'''

p = int('578455732137135466812346681323546443')
q = int('866586465716584657165746753876546577')
phi_n = 0
n= 501281908486219621910086584233925309600136539640088201223414043112175611
e= 65537
c= 455254144570149659309053721142936464401700360179699485409768697057718862
#get the values of p and q

def modularInverse(a, m):
    g, x, y = modInv_part2(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x % m

def modInv_part2(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = modInv_part2(b % a, a)
    return (g, x - (b // a) * y, y)

def get_n_phin(p,q):
    phi_n = (p-1)*(q-1)
    #print "Value of phi n: %d" % phi_n
    return phi_n
    #elif p == q:
    if p == q:
        print('p and q cannot be equal')
    else:
        print('Not a prime number')

phi_n = get_n_phin(p,q)

M = ""
'''
def gcd(x, y):
    print "Finding if E is co-prime to PHI(n)"
    while y !=0:
        (x, y) = (y, x % y)
    return x

g = gcd(e, phi_n)
if g != 1:
    g = gcd(e, phi_n)
    print "E is co-prime to PHI(n)"
'''
d = modularInverse(e,phi_n)


def decrypt():
    #print "Decrypting...\n"
    '''
    We solve this by using Big Integer library of Java and get the value of M
    M = 70082079077068071079078079082084072051055087069083084050051068073071053
    '''
    M = "70082079077068071079078079082084072051055087069083084050051068073071053"
    return M
M = decrypt()

def split_str(seq, chunk, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(split_str(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst
temp_str = split_str(M, 3)

print "\n################# Outputs of RSA Cipher #################\n"

print"The plaintext Message encrypted was:"
for msg in temp_str:
        print str(chr(int(msg[0:2]))),
print "\nThe treasure is found :)"
#print msg
