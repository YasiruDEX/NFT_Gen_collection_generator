# import PIL module
from PIL import Image

# import os module
import os

import random

#Getting the folder list
dirs = [f for f in os.listdir('.') if os.path.isfile(f) == False]

NeededNFTs = 100

Layers = []
for  i in dirs:
    if "#" in i:
        Layers.append(i)
      
Layers.sort()

#Getting assets to a list
Assets = []
for index,i in enumerate(Layers):
    path =  i + "/" 
    Assets.append([f for f in os.listdir(path)])

#calculate total NFTs
total = 1
for i in range(len(Assets)):
    total *= len(Assets[i])

def place(x):
    final = []
    #x -= 1
    for i in range(len(Layers)):
        #calculate the special value for a binary digit
        special = 1
        for j in range(len(Layers) - i - 1):
            k = -(j+1)
            special *= len(Assets[k])
        final.append(x//special)
        x -= special * (x//special)
    return(final)
       
Gotvalues = []
for i in range(NeededNFTs):
    if total < NeededNFTs:
        print("Erorr")
        break

    while True:
        ran = random.randint(0, total - 1)
        if ran in Gotvalues:
            continue
        else:
            Gotvalues.append(ran)
            break
    
    Place = place(ran)

    # BackImage
    filenamebackground = Layers[0] +  "/" + Assets [0][Place[0]]

    # Open Front Image
    background = Image.open(filenamebackground)

    # Convert image to RGBA
    background = background.convert("RGBA")

    for j in range(len(Layers) - 1):

        # Front Image
        filenamefrontImage = Layers[1+j] +  "/" + Assets [1+j][Place[1+j]]

        # Open Background Image
        frontImage = Image.open(filenamefrontImage)

        # Convert image to RGBA
        frontImage = frontImage.convert("RGBA")

        # Paste the frontImage
        #background.paste(frontImage, (0, 0), frontImage)
        background = Image.alpha_composite(background,frontImage)

    # Save this image
    filename = "Generated/" + str(i+1) + ".png" 
    background.save(filename)
    print("Saving " + str(i +1) + " th file")
    #Image.alpha_composite(background,frontImage).save(filename)

    


        
    
