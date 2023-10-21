import qrcode
img = qrcode.make('https://ct-state-middlesex-kootsookos.github.io/computers-101/intro.html')
type(img)  # qrcode.image.pil.PilImage
img.save("../logo.png")





