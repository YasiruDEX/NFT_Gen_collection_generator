# import PIL module
from PIL import Image

# import os module
import os

import random

#Getting the folder list
dirs = [f for f in os.listdir('.') if os.path.isfile(f) == False]

NeededNFTs = 500

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

rarities = []
#Check and piling up rarities
for i in range(len(Layers)):
    if "%" in Assets[i][0]:
        rarities.append([])
        for j in range(len(Assets[i])):
            Temp = Assets[i][j].split("%")
            rarities[i].append(int(Temp[0]))
    else:
        rarities.append(0)

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
Rarityhold = [None] * len(Layers)
for i in range(NeededNFTs):
    if total < NeededNFTs:
        print("Erorr")
        break
    while True:
        while True:
            ran = random.randint(0, total - 1)
            if ran in Gotvalues:
                continue
            else:
                Gotvalues.append(ran)
                break
        
        Place = place(ran)
        
        #checking the rarity
        exceeded = False
        for k in range(len(Place)):
                if rarities[k] != 0:
                    if Rarityhold[k] == None:
                        Rarityhold[k] = [0] * len(Assets[k])
                    if Rarityhold[k][Place[k]] >= NeededNFTs/100 * rarities[k][Place[k]]:
                        exceeded = True
                    #else:
                        #Rarityhold[k][Place[k]] += 1
        
        if exceeded == False:
            break
                
    print ("breaked")

    for k in range(len(Place)):
                if rarities[k] != 0:
                    Rarityhold[k][Place[k]] += 1
    print(Rarityhold)
                        
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

    


        
    
