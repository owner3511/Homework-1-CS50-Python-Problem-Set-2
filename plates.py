while True:
    try:
        plate_name = input("Duzgun plakati yazin: ")
        if 2 <= len(plate_name) <= 6 and plate_name[:2].isalpha() and plate_name.isalnum():
            print("Correct Valid")
            break
    except ValueError:
        pass
'''camel tapsirigini isleyerken diger is... metodlarini sorusmusdum. 
qarsima elave olaraq bilmediyim islower, isalnum, isspace, isstitle, isnumeric, 
isdecimal, isidentifier, isascii, isprintable metodlari cixmisdi. arasinda evvelden birce bildiyim
isalpha ve isdigit var idi. isalnum da bu tapsiriqda isime yaradi.'''


