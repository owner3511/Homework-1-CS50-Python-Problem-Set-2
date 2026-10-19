nickname = str(input("birlesik yazilmis nickname daxil edin.(duzgun formada duzelis edeceyik): "))
modified_nickname = ""
for i in nickname:
    if i.isupper():
        if modified_nickname == "":
            modified_nickname += i.lower()
        else:
            modified_nickname += "_" + i.lower()
    else:
        modified_nickname += i
print(modified_nickname)
'''ai-dan isupper funkisyasinin nece islediyini maraqlandim. 
ozum evvelceden isdigit ve isalpha-in proqramlarda qarsilasdigimiz formalarini bilirdim. 
amma duzgun halinin yazilis seklini unutmusdum'''