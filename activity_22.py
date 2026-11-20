anime = ["Doraemon", "Mr. Bean", "Upin and Ipin"]
print(anime[0])
anime_k = {"Doraemon": "A robot cat", "Mr. Bean": "A comedy character", "Upin and Ipin": "Two brothers"}

print(anime_k["Doraemon"])

#2d dimensional list
Doraemon = ["Doraemon", "Nobita", "Shizuka", "Gian", "Suneo"]
Mr_Bean = {"Mr. Bean", "Teddy", "Irma"}
Upin_and_Ipin = ["Upin", "Ipin", "Kk Ros", "Opah", "Ehsan", "Mail", "Fizi"]

doraemon = ["helpful", "kind", "intelligent", "caring"]
nobita = ["lazy", "kind-hearted", "emotional", "irresponsible"]
shizuka = ["gentle", "smart", "friendly", "helpful"]
gian = ["strong", "brave", "bully"]
suneo = ["rich", "boastful", "clever", "selfish"]
mr_bean = ["funny", "childish", "creative", "clumsy", "selfish"]
teddy = ["stuff toy"]
irma = ["caring", "patient", "understanding"]
upin = ["responsible", "friendly", "cheerful", "caring"]
ipin = ["playful", "funny", "energetic", "lovable"]
kak_ros = ["strict", "protective"]
opah = ["wise", "patient", "kind", "caring"]
ehsan = ["confident", "funny", "boastful"]
mail = ["hardworking", "practical", "business minded"]
fizi = ["talkative", "playful", "teasing"]

robot = [doraemon, nobita, shizuka, gian, suneo]
comedy = [mr_bean, teddy, irma]
brother = [upin, ipin, kak_ros, opah, ehsan, mail, fizi]

anime = {"robot cat":robot, "comedy character":comedy, "two brother":brother}

print(anime["robot cat"])
print(anime["robot cat"][0][-1])

# ============================================================
# CLUE: HOW TO ADD A NEW ENTRY TO A DICTIONARY
# Pattern: dictionary[new_key] = new_value
# If the key is new, Python ADDS it.
# If the key already exists, Python REPLACES its value.
# Remove the # to try each one.
#
# Add your entries HERE, before the loops, so the loops print them.
# ============================================================


# --- Add a new CHARACTER to a cartoon (Level 3) ---
# doraemon = ["Robot cat from the future", "Gadget inventor"]
# robot_cat["Doraemon"] = doraemon


# --- Add a new CARTOON to a category (Level 2) ---
# mr_bean = {"Mr. Bean": ["Funny and clumsy man", "Creative problem solver"]}
# comedy["Mr. Bean"] = mr_bean


# --- Add a new CATEGORY (Level 1) ---
# new_category = {"New Cartoon": {"Character": ["Description", "Ability"]}}
# anime["New Category"] = new_category


# --- Change (update) an existing value ---
# anime["Robot Cat"]["Doraemon"]["Doraemon"][1] = "New Gadget"


# ============================================================
# LEVEL 4: Each character is a list [description, traits]
# ============================================================

doraemon = ["Robot cat from the future", "Helpful, kind, intelligent, caring"]
nobita = ["Doraemon's human friend", "Lazy, kind-hearted, emotional, irresponsible"]
shizuka = ["Nobita's friend", "Gentle, smart, friendly, helpful"]
gian = ["Nobita's classmate", "Strong, brave, sometimes a bully"]
suneo = ["Nobita's rich friend", "Rich, boastful, clever, selfish"]

mr_bean = ["Comedy character", "Funny, childish, creative, clumsy, selfish"]
teddy = ["Mr. Bean's stuffed toy", "Loyal companion"]
irma = ["Mr. Bean's friend", "Caring, patient, understanding"]

upin = ["Elder twin brother", "Responsible, friendly, cheerful, caring"]
ipin = ["Younger twin brother", "Playful, funny, energetic, lovable"]
kak_ros = ["Older sister of Upin and Ipin", "Strict, protective"]
opah = ["Grandmother of Upin and Ipin", "Wise, patient, kind, caring"]
ehsan = ["Upin and Ipin's friend", "Confident, funny, boastful"]
mail = ["Upin and Ipin's friend", "Hardworking, practical, business-minded"]
fizi = ["Upin and Ipin's friend", "Talkative, playful, teasing"]


# ============================================================
# LEVEL 3: Each cartoon is a dictionary of characters
# ============================================================

robot_cat = {"Doraemon": doraemon,"Nobita": nobita,"Shizuka": shizuka,"Gian": gian,"Suneo": suneo}

comedy = {"Mr. Bean": mr_bean,"Teddy": teddy,"Irma": irma}

two_brothers = {"Upin": upin,"Ipin": ipin,"Kak Ros": kak_ros,"Opah": opah,"Ehsan": ehsan,"Mail": mail,"Fizi": fizi}


# ============================================================
# LEVEL 2: Each category is a dictionary of cartoons
# ============================================================

animation = {"Doraemon": robot_cat}
comedy_category = {"Mr. Bean": comedy}
family = {"Upin and Ipin": two_brothers}


# ============================================================
# LEVEL 1: The main dictionary
# ============================================================

anime = {"Robot Cat": animation,"Comedy Character": comedy_category,"Two Brothers": family}


# ============================================================
# 1. Going down one level at a time
# ============================================================

print("=== 1. Going down one level at a time ===")
print(anime["Robot Cat"]["Doraemon"]["Doraemon"][1])

print()

# ============================================================
# 2. Loop level 1: categories
# ============================================================

print("=== 2. Loop level 1: categories ===")

for category in anime:
    print(category)
print()

# ============================================================
# 3. Loop levels 1-2: categories and titles
# ============================================================

print("=== 3. Loop levels 1-2: categories and titles ===")

for category, titles in anime.items():
    print(category)
    for title in titles:
        print(" -", title)
print()

# ============================================================
# 4. Loop ALL levels
# ============================================================

print("=== 4. Loop ALL levels ===")

for category, titles in anime.items():
    print(category)

    for title, characters in titles.items():
        print(" ", title)

        for name, info in characters.items():
            print("   " + name)
            print("      Description:", info[0])
            print("      Traits:", info[1])

print()

# ============================================================
# 5. Count every character
# ============================================================

print("=== 5. Count every character ===")

count = 0

for titles in anime.values():
    for characters in titles.values():
        for name in characters:
            count = count + 1

print("Total characters:", count)

print()

# ============================================================
# 6. Search for a character
# ============================================================

print("=== 6. Search for a character ===")

search = "Ipin"
found = False

for category, titles in anime.items():
    for title, characters in titles.items():
        if search in characters:
            print(search, "is from", title, "(" + category + ")")
            print("Description:", characters[search][0])
            print("Traits:", characters[search][1])
            found = True

if found == False:
    print(search, "not found.")
