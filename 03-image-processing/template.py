from PIL import Image

im = Image.open("bird.png") # load input image
output = Image.new(im.mode, im.size) # make blank output image with same dimension as input

for y in range(im.height):
  for x in range(im.width):
    (r, g, b) = im.getpixel((x, y))

    # your code here

    output.putpixel((x, y), (r, g, b))

output.save("output.png") # save output image
