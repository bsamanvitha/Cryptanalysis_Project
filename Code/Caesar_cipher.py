# Caesar cipher

def caesar(key_inp, hex_inp):
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

key_inp = 2203
hex_inp = '573IEJ169J65HJHI8H95412J0F434J93E7I4F9E9I9E9F545177142J'

print (caesar(key_inp, hex_inp))