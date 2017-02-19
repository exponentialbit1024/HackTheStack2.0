text = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""
text = text.replace("\n", " ")
f = lambda c: ord(c) == 32 or 0<=(ord(c)-65)<26 or 0<=(ord(c)-97)<26

cleaned = "".join(list(filter(f, text))).lower()

key = [3, 8, 25, 16, 19, 15]

cleaned += " the password is seven hundred twenty seven d eight b four d four hundred fifteen c four e eight c"

encrypted = list()
i = 0
for c in cleaned:
	if c == " ":
		encrypted += " "
	else:
		encrypted += chr(((ord(c)-97+key[i % len(key)])%26)+97)

print("".join(encrypted))


text = open("ciphered").read().strip()

key = [-3, -8, -25, -16, -19, -15]

encrypted = list()
i = 0
for c in text:
	if c == " ":
		encrypted += " "
	else:
		encrypted += chr(((ord(c)-97+key[i % len(key)])%26)+97)

print("".join(encrypted))

