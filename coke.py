mebleg = 50
while mebleg >= 0:
    try:
        a = int(input("meblegi girin: "))
        if a == 5 or a == 10 or a == 25:
            mebleg -= a
        else:
            if 0 < a <= 50:
                print("5,10,25 sentlik ve ya 50-den daha artiq mebleg daxil ede bilersiniz.")
            elif a <= 0:
                print("musbet eded daxil edin.")
            else:
                print(f"Amount Due: {a-50}")
                break
    except ValueError:
        print("duzgun deyer girmeyiniz xahis olunur.")
'''try ve except ValueError 
hissesini kecen defeki laborotoriya assignmentini isleyerken sorusmusdum aidan'''


