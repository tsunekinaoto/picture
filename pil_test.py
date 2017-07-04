from PIL import Image

img = Image.open( 'mauntain_huji.jpg' )

gray_img = img.convert('L')

gray_img.save( 'gray.jpg' )