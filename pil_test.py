from PIL import Image
from PIL import ImageFilter

img = Image.open( 'mauntain_huji.jpg' )

gimg = img.filter(ImageFilter.EMBOSS)

gimg.save( 'moza.jpg' )