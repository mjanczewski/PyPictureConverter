import os
from PIL import Image

inputFolder = './input'

for filename in os.listdir(inputFolder):
    if filename.endswith('.jpg'):
        filenameMod = filename.split('.')
        filenameMod = str(filenameMod[0])
        print(filename)
        inputImage = Image.open(f'./input/{filename}')
        inputImage.save(f'./output/opis/{filenameMod}.webp')
        inputImage.save(f'./output/{filenameMod}.jpg')


# inputImage = Image.open('./input/')

# print(inputImage)

# inputImage.save('./output/test.webp')
