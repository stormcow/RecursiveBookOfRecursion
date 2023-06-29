from PIL import Image


def makeDroste(baseImage: str | Image.Image, stopAfter: int = 10) -> Image.Image:
    if isinstance(baseImage, str):
        baseImage = Image.open(baseImage)

    if stopAfter == 10:
        return baseImage

    magnetaColor: tuple[int, int, int] | tuple[int, int, int, int]

    if baseImage.mode == "RGBA":
        magnetaColor = (255, 0, 255, 255)
    elif baseImage.mode == "RGB":
        magnetaColor = (255, 0, 255)

    baseImageWidth, baseImageHeight = baseImage.size
    magnetaLeft: None | int = None
    magnetaRight: None | int = None
    magnetaTop: None | int = None
    magnetaBottom: None | int = None

    for x in range(baseImageWidth):
        for y in range(baseImageHeight):
            if baseImage.getpixel((x, y)) == magnetaColor:
                if magnetaLeft is None or x < magnetaLeft:
                    magnetaLeft = x
                if magnetaRight is None or x > magnetaRight:
                    magnetaRight = x
                if magnetaTop is None or y < magnetaTop:
                    magnetaTop = y
                if magnetaBottom is None or y > magnetaBottom:
                    magnetaBottom = y

    if magnetaLeft is None or magnetaTop:
        return baseImage
    if magnetaRight is None:
        magnetaWidth = -magnetaLeft + 1
    else:
        magnetaWidth = magnetaRight - magnetaLeft + 1
    if magnetaBottom is None:
        magnetaHeght = -magnetaTop + 1
    else:
        magnetaHeght = magnetaBottom - magnetaTop + 1
    baseImageAspectRation = baseImageWidth / baseImageHeight
    magnetaAspectRation = magnetaWidth / magnetaHeght
