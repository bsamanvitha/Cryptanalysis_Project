# Caesar cipher

key_inp = 2203
YY = str(key_inp)[-2:]
XX = str(key_inp)[0:2]
hex_inp = '573IEJ169J65HJHI8H95412J0F434J93E7I4F9E9I9E9F545177142J'
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

print ('Given:  ' + hex_inp)
print ('Result: ' + output_str)
print ('Actual: ' + '240EAF836F32DFDE5D62189F7B101F60A4E1B6A6E6A6B212844819F')

