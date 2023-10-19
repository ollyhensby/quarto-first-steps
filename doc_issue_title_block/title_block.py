from reportlab.platypus import Table, Image, TableStyle, SimpleDocTemplate
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.pagesizes import A3, landscape
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

from textwrap import wrap
import pathlib

###FONTS###
###Register Callibri fonts###
FDIR_FONTS = pathlib.Path(__file__).parent / "fonts"
TTFFILE = FDIR_FONTS / "calibri.ttf"
pdfmetrics.registerFont(TTFont("Calibri", TTFFILE))
TTFFILE = FDIR_FONTS  / "calibrib.ttf" #Bold
pdfmetrics.registerFont(TTFont("Calibri-Bold", TTFFILE))
TTFFILE = FDIR_FONTS  / "calibrili.ttf" #Light Italics
pdfmetrics.registerFont(TTFont("Calibri-Light-Italics", TTFFILE))
TTFFILE = FDIR_FONTS  / "calibrii.ttf" #Italics
pdfmetrics.registerFont(TTFont("Calibri-Italics", TTFFILE))
TTFFILE = FDIR_FONTS  / "calibril.ttf" #Light
pdfmetrics.registerFont(TTFont("Calibri-Light", TTFFILE))
TTFFILE = FDIR_FONTS  / "calibrib.ttf" #Bold Italics
pdfmetrics.registerFont(TTFont("Calibri-Bold-Italics", TTFFILE))

def DEFAULTTITLEBLOCKTABLESTYLE(lines: int):
    style = [('LINEABOVE', (0, 0), (-1, 0), 3, colors.black), #topline
                ('LINEBELOW', (0, -1), (-1, -1), 3, colors.black), #bottomline
                ('SPAN', (0,0), (2,-1)),
                ('SPAN', (3,1), (5,1)), #client
                ('SPAN', (3,5), (5,5)), #status
                ('SPAN', (6,1), (8,3)), #project
                ('SPAN', (9,1), (11,2)), #document title
                ('SPAN', (9,4), (11,4)), #document number
                ('SPAN', (9,5), (11,5)), #document number
            ]
    for i in range(lines):
        if i%2 == 0:
            style.append(('FONT', (0, i), (-1, i), "Calibri", 10))
            style.append(('TEXTCOLOR', (0, i), (-1, i), colors.gray))
            style.append(('VALIGN', (1, i), (-1, i), 'BOTTOM'))
            style.append(('BOTTOMPADDING', (0, i), (-1, i), 0))
        else:
            style.append(('FONT', (0, i), (-1, i), "Calibri-Bold", 14))
            style.append(('TEXTCOLOR', (0, i), (-1, i), colors.black))
            style.append(('VALIGN', (1, i), (-1, i), 'TOP'))
            style.append(('TOPPADDING', (0, i), (-1, i), 0))

    style.append(('BACKGROUND', (0, 0), (2, -1), colors.black))
    style.append(('VALIGN', (0, 0), (0, -1), 'MIDDLE'))
    style.append(('LINEBEFORE', (0, 0), (0, -1), 3, colors.black))

    return style

def get_title_block_image():
    I = Image(pathlib.Path(__file__).parent / "titleblock_london.PNG")
    I.drawHeight = 88*mm * I.drawHeight/I.drawWidth
    I.drawWidth = 88*mm
    return I

def construct_title_block_data():
    ''' title block for the document'''

    d = "01"
    m = "01"
    y = "23"
    s = "S0"
    status_description = "STATUS"
    doc_title = "\n" + d + "/" + m + "/" + y + " - " + s

    project_info = {
        "Client Name": "CLIENT NAME",
        "Project Name": "PROJECT NAME",
        "Job Number": "JOB NUMBER",
        "Project Leader": "PROJECT LEADER",
        "Naming Convention": "NAMING CONVENTION",
        "Document Name": "06667-MXF-XX-XX-SH-M-20003",
    }

    data = []
    data.append([get_title_block_image(), "", "", "client", "", "", "project", "", "", "document title", "", ""])
    data.append(["", "", "", project_info["Client Name"], "", "", project_info["Project Name"], "", "", "Document Issue Sheet" + doc_title, "", ""])
    data.append(["", "", "", "job no.", "project leader", "scale at A3", "", "", "", "", "", ""])
    data.append(["", "", "",  project_info["Job Number"], project_info["Project Leader"] ,"NTS", "", "", "", "", "", ""])
    data.append(["", "", "", "status code and description", "", "", "issue date", "classification", "revision", project_info["Naming Convention"], "", ""])
    data.append(["", "", "", s + status_description, "", "", d + "/" + m + "/" + y, "-", "-", project_info["Document Name"], "", ""])
    return data


def create_title_block_table(data: list):
    data[1][6] = "\n".join(wrap(data[1][6], 30))
    mytable = Table(data, colWidths='*')
    mystyle = DEFAULTTITLEBLOCKTABLESTYLE(len(data))
    mytable.setStyle(TableStyle(mystyle))
    return mytable


def produce_title_block_pdf(fpth: pathlib.Path):
    data = construct_title_block_data()
    title_block = create_title_block_table(data)
    doc = SimpleDocTemplate(str(fpth), pagesize=landscape(A3))
    elements = [title_block]
    doc.build(elements)


if __name__ == "__main__":
    produce_title_block_pdf(pathlib.Path(__file__).parent / "title_block.pdf")
