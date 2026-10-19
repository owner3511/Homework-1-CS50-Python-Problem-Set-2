saitler = ["a", "ı", "o", "u", "e", "ə", "i", "ö", "ü", "A", "I", "O", "U", "E", "Ə", "İ", "Ö", "Ü"]
a = input("")
lst = []
for i in a:
    if i not in saitler:
        lst.append(i)
print("".join(lst))
'''saitler = ["a", "ı", "o", "u", "e", "ə", "i", "ö", "ü", "A", "I", "O", "U", "E", "Ə", "İ", "Ö", "Ü"]
a = input("")
lst = list(a)
for i in lst:
    if i in saitler:
        lst.remove(i)
print("".join(lst))
kodumun ilkin formasi bele idi. 
amma aiden sorusduqda kodumda remove ederken 
bezi simvollarin indexi surusduyu ucun yanlis calisa bileceyini dedi. 
kiçik deyişiklik etdim ona gore'''