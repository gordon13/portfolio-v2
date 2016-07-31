from PIL import Image, ImageOps
import os
path = os.path.dirname(os.path.realpath(__file__))
images_path = "%s\\src\\assets\\images"%path
out_path = "%s\\src\\assets\\images\\thumbs"%path
thumbnail_size = 300, 500

import os
for file in os.listdir(images_path):
	if file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".jpg"):
		print(file)
		im = Image.open("%s\\%s"%(images_path, file))
		thumb = ImageOps.fit(im, thumbnail_size, Image.ANTIALIAS)
		namext = file.split(".")
		thumb.save("%s\\%s_thumb.%s" % (out_path, namext[0], namext[1]))