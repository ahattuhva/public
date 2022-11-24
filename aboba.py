from PIL import Image, ImageDraw, ImageFont

def f(t):




    im = Image.new('RGB', (200,200), color=('#FAACAC'))
    font = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', size=20)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (100,100),
        ' яяяяяяяя ',
        font=font,
        fill=('#1C0606')
        )
    im.show()
t='яяяяяяяя'
f(t)


