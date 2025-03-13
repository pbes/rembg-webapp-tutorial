from rembg import remove
from PIL import Image


input = Image.open('/home/pbes/Downloads/BP_avatar_uj.jpg')

output = remove(input)

background_image = Image.open('digitaler-showroom-fahrzeugpraesentation-001-1920w.png')
transparent_image = Image.new('RGBA', background_image.size, (0, 0, 0, 0))

x = (transparent_image.width - output.width) // 2
y = (transparent_image.height - output.height) // 2

transparent_image.paste(output, (x, y), output)
transparent_image = transparent_image.resize(background_image.size)

merged_image = Image.alpha_composite(background_image.convert('RGBA'), transparent_image)

merged_image.save('merged_output.png')