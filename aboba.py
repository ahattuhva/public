from PIL import Image, ImageDraw, ImageFont

def f(t, i):

    im = Image.new('RGB', (1920,1080), color=('#59a946'))
    font = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', size=(100))
    for i in range (10):
        im.save('C:/Users/student/Documents/142/хайп/bebra'+str(i)+'.jpg')
    
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (100,100),
        t,
        font=font,
        fill=('#ffffff')
        )
    im.show()
    im.save('C:/Users/student/Documents/142/хайп/bebra'+str(i)+'.jpg')
t='яяяяяяяя'
t=['ВСЁ РЕШЕНО', 
   'Я ЛИЦЕИСТ',
   'Я ПОВЗРОСЛЕЛ',
   'МОЖЕТЕ ПРОСТО ПРОМОЛЧАТЬ',
   'МОЖЕТЕ ЗЛИТЬСЯ',
   'ИЛИ БЕСИТЬСЯ',
   'НУ, А Я ПОШЁЛ УЧИТЬ',
   'АЛГЕБРУ',
   'ОБЩЕСТВО',
   'ГЕОМЕТРИЮ']
for i in range(10):
    f(t[i],i)
f(t)


