s = ""
with open('charabia.txt', 'r') as file:
    while True:
        char = file.read(1)
        if not char:
            break
        s += char

s = s.replace("л", " ")
s = s.replace("ц", "_")

s = s.replace("[$", "c")
s = s.replace("λ", "t")
s = s.replace("Σ", "f")

s = s.replace("^", "e")

# ét#╩6Ξe -> étrange:
s = s.replace("#", "r")
s = s.replace("╩", "a")
s = s.replace("6", "n")
s = s.replace("Ξ", "g")

# !annea&E -> panneaux:
s = s.replace("!", "p")
s = s.replace(" p ", "! ")
s = s.replace("&", "u")
s = s.replace("E", "x")

# /ஏrapeau -> drapeau
s = s.replace("/ஏ", "d")

# c▙erc▙eΩ -> cherchez
s = s.replace("▙", "h")
s = s.replace("Ω", "z")

# dan[ -> dans
s = s.replace("[", "s")

# c|ntre -> contre
s = s.replace("|", "o")

# p⃝aît -> plaît
s = s.replace(chr(8413), "l") # weird character

# :ous -> vous
s = s.replace(":", "v")
s = s.replace(" v ", " : ") # there is a ':' before the flag

# su𝚑s -> suis
s = s.replace("𝚑","i")

#Ψlessé -> blessé
s = s.replace("Ψ", "b")

#per༽is -> permis
s = s.replace("༽", "m")

#g?mnasti%ue -> gymnastique
s = s.replace("?", "y")
s = s.replace(" y", "?") # last character pf the plaintext is a question mark
s = s.replace("%", "q")

#quяavant -> qu'avant
s = s.replace("я", "'")

# ⃥e -> je
s = s.replace(" ⃥", " j")
s = s.replace("-⃥", "-j")

#ConTreж -> contre,
s = s.replace("ж", ",")

#ChuTeв -> chute.
s = s.replace("в", ".")

print(s, end = '')
