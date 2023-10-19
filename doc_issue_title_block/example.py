from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.graphics import renderPM

d = Drawing(400, 200)
d.add(Rect(0, 0, 400, 200, fillColor=colors.yellow))
d.add(String(150,100, 'Hello World', fontSize=18, fillColor=colors.red))

renderPM.drawToFile(d, 'example1.png', 'PNG')
