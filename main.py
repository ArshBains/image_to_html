from PIL import Image

image_loc = r'D:\path\to\pic.jpeg'     # image path
html_loc = r'D:\location\to\save\image.html'    # location to store the .html file with its name

im = Image.open(image_loc)
w, h = im.size

top = '<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"><title>Picture</title><link ' \
      'rel="stylesheet" href="styles.css"><style>*{margin:0;padding:0;}.main{margin:auto;width:'+str(w)+'px;height:' \
      +str(h)+';background-color: green;}.px{width:1px;height:1px;float:left;}</style></head><body><div class="main"> '
foot = '</div></body></html>'

with open(html_loc, 'w') as html:
    html.write(top)
    for i in range(0, h):
        for j in range(0, w):
            col = str(im.getpixel((j,i)))
            html.write('<div class="px r'+ str(i) +'c'+ str(j) +'" style="background-color:rgb'+col+';" ></div>')
    html.write(foot)
