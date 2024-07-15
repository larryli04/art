from PIL import Image
import sys
from pathlib import Path

def luminosity(r: int, g: int, b:int) -> int:
    return (int) (0.2126*r + 0.7152*g + 0.0722*b)

n = len(sys.argv)
if(n == 2):
    filename = Path(sys.argv[1])
elif(n > 2):
    print("Too many arguments. Please only provide the filepath")
    exit(1)
else:
    print("Please provide a filepath")
    exit(1)
 

# from an image, generate a dotmap

im = Image.open(filename)
width, height = im.size
print(width, height)

# print(f"Opened file {filename.name} with width {width} and height {height}")

grad = "$@B%8WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,^`'."
grad_len = len(grad)

im = im.convert('RGBA')
out = [[0 for _ in range(width)] for _ in range(height)]

f = open("out.svg", "a")

# start writing svg format
f.write(f"<svg height=\"{height*3}\" width=\"{width*3}\" xmlns=\"http://www.w3.org/2000/svg\">")
f.write("<style>.small {font: bolder 5px monospace} </style>\n")
f.write("<rect width=\"100%\" height=\"100%\" fill=\"#1e295b\"/>")
for y in range(height):
    for x in range(width):
        r, g, b, _ = im.getpixel((x, y));
        lindex = int(grad_len *(luminosity(r, g, b)/255))
        f.write(f"<text x=\"{x*3}\" y=\"{y*3}\" fill=\"rgb({r}, {g}, {b})\" class=\"small\">{grad[lindex]}</text>\n")

f.write("</svg>")
