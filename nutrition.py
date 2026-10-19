calori_cedveli = {
    "apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60,
    "grapes": 90, "honeydew melon": 50, "kiwi": 90, "lemon": 15, "orange": 80}
item = input("item daxil edin: ").lower()
if item in calori_cedveli:
    print(f"Calories: {calori_cedveli[item]}")
else:
    pass
#mene aid koddur