##########################################################
# Cheese-it Grooves
# Collin Sanford, Matthew Reed, Madison Gay
# 02/10/19
# Using PIL to manipulate images
##########################################################
from PIL import Image

def replace(sourcename, destname, offset):
	
	# opens images
	source = Image.open(sourcename)
	dest = Image.open(destname)
	
	# loads pixels value
	sourcepix = source.load()
	destpix = dest.load()
	
	# gets image size
	size = source.size
	LENGTH = size[1]
	WIDTH = size[0]
	
	# maps pixels of source to pixels of destination 
	# (you might want to specify the correct length offset)
	for i in range(WIDTH):
		for j in range(LENGTH):
			destpix[i,j+offset] = sourcepix[i,j]

	dest.save(destname)


replace("fragment1.bmp","key.bmp",0)
