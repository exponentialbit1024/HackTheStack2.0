from PIL import Image
message = "the key is 40382b41412b479b"

img = Image.open("left.jpg").convert("RGBA")

w,h = img.size
m = 0
for i in range(w):
	for j in range(h):
		c = ord(message[m % len(message)])
		#load original
		R, G, B, A = img.load()[i, j]
		#pack in data
		R = ((192 & c) >> 6) + (R & (~3))
		G = ((48 & c) >> 4) + (G & (~3))
		B = ((12 & c) >> 2) + (B & (~3))
		A = ((3 & c)) + (A & ~(3))
		#write to image
		img.load()[i, j] = (R, G, B, A)

img.save("right.jpg")
