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