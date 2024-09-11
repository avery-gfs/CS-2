## Concepts

- What are colors?
- Pixels https://en.wikipedia.org/wiki/Pixel#/media/File:Pixel_geometry_01_Pengo.jpg
- Image coordinate system
- RGB color model https://colorpicker.me/
- Pillow library: https://pillow.readthedocs.io/en/stable/reference/Image.html
- How many colors are there?
- Grayscale and luminance https://en.wikipedia.org/wiki/Grayscale
- Color distance
- HSL color model / conversion
- Dithering https://tannerhelland.com/2012/12/28/dithering-eleven-algorithms-source-code.html
- Kernels and convolution https://setosa.io/ev/image-kernels/

- Setup

  ```py
  from PIL import Image

  im = Image.open("bird.png") # load input image
  output = Image.new(im.mode, im.size) # make blank output image with same dimension as input

  # your code here

  output.save("output.png") # save output image
  ```

- Dimensions

  ```py
  im.height # image height in pixels
  im.width # image height in pixels
  ```

- Grayscale

  ```py
  im = Image.open("bird.png") # load input image in grayscale
  ```

- Get pixel value:

  ```py
  (r, g, b) = im.getpixel((x, y)) # (color image) get rgb values at position x, y

  l = im.getpixel((x, y)) # (grayscale image) get lightness value at position x, y
  ```

- Set pixel value:

  ```py
  im.putpixel((x, y), (r, g, b)) # (color image) set rgb values at position x, y

  im.putpixel((x, y), l) # (grayscale image) set lightness value at position x, y
  ```

- Basic convolution:

  ```py
  from PIL import Image

  im = Image.open("bird.png")
  output = Image.new(im.mode, im.size)

  # Identity kernel, doesn't to anything
  # Tweak numbers for different effects
  # Kernel numbers should sum to 1 (why?)

  kernel = [
    [ 0,  0,  0],
    [ 0,  1,  0],
    [ 0,  0,  0],
  ]

  for y in range(1, im.height - 1):
    for x in range(1, im.width - 1):
      newR = 0
      newG = 0
      newB = 0

      for ky in [-1, 0, 1]:
        for kx in [-1, 0, 1]:
          factor = kernel[ky][kx]
          (r, g, b) = im.getpixel((x + kx, y + ky))

          newR += r * factor
          newG += g * factor
          newB += b * factor

      output.putpixel((x, y), (round(newR), round(newG), round(newB)))

  output.save("output.png")
  ```

## Problems

Write a program to convert an image to black-and-white.

Write a program to rotate an image `n` degrees about its center (without using the PIL rotation functionality).

Write a program that sharpens an image with the sharpen kernel. https://en.wikipedia.org/wiki/Kernel_(image_processing)#External_links

Choose a color palette of 8 colors. Write a program that converts an image to use this color palette by finding the closest color in the palette to each color in the input image.

Write a program that increases an image's saturation to the maximum amount.

Write a program that performs random dithering.

Write a program that generates a color palette for an image automatically using k-means clustering.

Write a program that performs Floyd-Steinberg dithering.

Write a program to find the edges in an image using the Sobel operator. https://en.wikipedia.org/wiki/Sobel_operator
