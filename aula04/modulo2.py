import modulo

tv = "Baby, we're the new romantics"
print(tv)
enc = modulo.caesar(tv, 18)
print(enc)
print(modulo.caesar(enc, 18, decode = True))