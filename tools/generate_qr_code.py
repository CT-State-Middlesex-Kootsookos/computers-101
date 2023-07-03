import qrcode
img = qrcode.make('https://middlesex-community-college-kootsookos.github.io/computers-101')
type(img)  # qrcode.image.pil.PilImage
img.save("../logo.png")





