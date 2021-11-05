from PIL import Image, ImageFont, ImageDraw
afbeelding = Image.open("meme_background.jpg")

breedte = afbeelding.width
hoogte = afbeelding.height

lettertype = ImageFont.truetype("impact", 35)

tekengebied = ImageDraw.Draw(afbeelding)

tekst = "Dani waneer zijn code \n niet werkt"
tekengebied.multiline_text((300,150), tekst, font=lettertype, fill=(255,250,250))

afbeelding.show()

afbeelding.save("meme_met_tekst.png")
