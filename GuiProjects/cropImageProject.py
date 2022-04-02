from PIL import Image,ImageFilter


image = Image.open("ulucamii.jpg")


image.save("ulucamii2.jpg")

image.rotate(180).save("ulucamii_rotate180.jpg")

image.convert(mode = "L").save("ulucamii_blackWhite.jpg")

change_dimension = (100,80)
image.thumbnail(change_dimension)
image.save("ulucamii_newDimension.jpg")

image.filter(ImageFilter.GaussianBlur(2)).save("ulucamii_blur.jpg")

crop_area = (133,25,190,135)
image2 = Image.open("pythonPngImage.png")
image2.crop(crop_area).save("pythonImage_crop.png")
#image.show()