'''Small python script to build an ASCII art representation of a supplied
image using the PIL module. Open an image file as an Image object and supply it as arg to the 
convert function.'''

from PIL import Image

ASCII_CHARS = [' ', '.', '*', ':', 'o', '&', '8', '#', '@']
ASCII_CHARS_LEN = len(ASCII_CHARS)

def convert_image_to_ascii(image, columns=80):
    image = image.resize((columns, columns), Image.ANTIALIAS)
    pixels = image.load()
    ascii_art = []
    for i in range(image.size[1]):
        row = []
        for j in range(image.size[0]):
            intensity = sum(pixels[j, i]) / 3
            char = ASCII_CHARS[int(intensity / 256 * ASCII_CHARS_LEN)]
            row.append(char)
        ascii_art.append(''.join(row))
    return '\n'.join(ascii_art)

test = Image.open('testimage.webp')
print(convert_image_to_ascii(test))