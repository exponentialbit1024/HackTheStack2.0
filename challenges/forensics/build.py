from PIL import Image
from random import random
old = Image.open("original.png")
width = old.size[0]
left = old.crop((0, 0, width, width)).resize((200, 200), Image.ANTIALIAS)
left.save("left.png")
code = Image.open("qrcode.png")
right = Image.new("RGB", (200, 200))
for i in range(200):
	for j in range(200):
		r,g,b, = left.load()[i,j]
		d,_,_ = code.load()[i,j]
		if d:
			rn = random()
			if rn < 1.0/3:
				right.load()[i,j] = ((r+g)//2, g, b)
			elif rn < 2.0/3:
				right.load()[i,j] = (r, (g+b//2), b)
			else:
				right.load()[i,j] = (r, g, (r+b)//2)
		else:
			right.load()[i,j] = (r,g,b)

right.save("right.png")
