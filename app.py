import os
from PIL import Image

inputFolder = './input'

for filename in os.listdir(inputFolder):
    if filename.endswith('.jpg'):
        print(filename)
        inputImage = Image.open(f'./input/{filename}')
        inputImage.save(f'./output/{filename}.webp')


# inputImage = Image.open('./input/')

# print(inputImage)

# inputImage.save('./output/test.webp')
