from reportlab.pdfgen.canvas import Canvas

from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from datetime import datetime

today = datetime.today().strftime('%F')

outfile = "print_template.pdf"
template = PdfReader("parseMet/ceilo_template.pdf", decompress=False)
canvas = Canvas(outfile, pagesize='A4')

col_star_padding = 140
week1_pad = 190
week2_pad = week1_pad + col_star_padding # 310
week3_pad = week2_pad + col_star_padding #450

# create page objects
pages = template.pages[0: 4]
pages = [pagexobj(page) for page in pages]

for page in pages:
    #canvas.setPageSize((page.BBox[2], page.BBox[3]))
    canvas.doForm(makerl(canvas, page))
    canvas.setFont("Helvetica", 9)
    #data = parse()

    """ canvas.drawString(week1_pad, 680, "ER,EE")
    canvas.drawString(week1_pad, 667, today)
    canvas.drawString(week1_pad, 597, data[0])
    canvas.drawString(week1_pad, 583, data[1])
    """

    canvas.showPage()

"""template = PdfReader("rvr_template.pdf", decompress=False).pages[0]
template_obj = pagexobj(template)

canvas = Canvas(outfile, pagesize='A4')
canvas.setFont("Helvetica", 10)

xobj_name = makerl(canvas, template_obj)
canvas.doForm(xobj_name)

ystart = 680

# Prepared by
canvas.drawString(170, ystart, "ER,EE")
"""


canvas.save()