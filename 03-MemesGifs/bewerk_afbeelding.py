from PIL import Image

afbeelding = Image.open("kermit.png")
afbeelding.show()

breedte = str(afbeelding.width)
hoogte = str(afbeelding.height)

helft_breedte = afbeelding.width // 2

helft_hoogte = afbeelding.height // 2

nieuwe_afmeting = (helft_breedte, helft_hoogte)

kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)

kleinere_afbeelding.save('kermit_klein.png')
