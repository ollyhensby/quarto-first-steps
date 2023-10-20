import pathlib
from textwrap import wrap
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, Image, TableStyle, SimpleDocTemplate


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

def create_styling(number_of_cols: int) -> list:
    style = [
        ('BACKGROUND', (0, 0), (1, -1), colors.black),
        ('VALIGN', (0, 0), (0, -1), 'MIDDLE'),
        ('LINEABOVE', (0, 0), (-1, 0), 3, colors.black),
        ('LINEBELOW', (0, -1), (-1, -1), 3, colors.black),
        ('LINEBEFORE', (0, 0), (0, -1), 3, colors.black),
        ('SPAN', (0, 0), (1, -1)), # Span image
        ('SPAN', (7, 1), (-1, 3)), # Span document title
    ]
    for i in range(number_of_cols):
        if i%2 == 0:
            style.append(('FONT', (0, i), (-1, i), "Calibri", 8))
            style.append(('TEXTCOLOR', (0, i), (-1, i), colors.gray))
            style.append(('VALIGN', (1, i), (-1, i), 'BOTTOM'))
            style.append(('BOTTOMPADDING', (0, i), (-1, i), 0))
        else:
            style.append(('FONT', (0, i), (-1, i), "Calibri-Bold", 11))
            style.append(('TEXTCOLOR', (0, i), (-1, i), colors.black))
            style.append(('VALIGN', (1, i), (-1, i), 'TOP'))
            style.append(('TOPPADDING', (0, i), (-1, i), 0))
    return style

def get_title_block_image(fpth_img: pathlib.Path) -> Image:
    image = Image(fpth_img)
    image.drawHeight = 30*mm * image.drawHeight/image.drawWidth
    image.drawWidth = 30*mm
    return image

def construct_title_block_data() -> list[list]:
    d = "01"
    m = "01"
    y = "23"

    project_info = {
        "project_name": "University of Oxford, Humanities Building",
        "job_number": "J4321",
        "project_leader": "OH",
        "document_name": "06667-MXF-XX-XX-SH-M-20003",
        "document_description": "A description of the document that is important t what is happening and do something that we can do more with and then jump around a bit and see what this description",
        "name_nomenclature": "project code-originator-volume-level-type-role-number",
        "revision": "P01",
        "status_code": "S2",
        "status_description": "Suitable for information"
    }
    FPTH_MF_CIRCLE_IMG = pathlib.Path(__file__).parent / "mf_circle.png"
    image = get_title_block_image(fpth_img=FPTH_MF_CIRCLE_IMG)
    issue_date = d + "/" + m + "/" + y
    document_description = "\n".join(wrap(project_info["document_description"], 45))
    name_nomenclature = project_info["name_nomenclature"].replace("-", " - ")
    document_name = project_info["document_name"].replace("-", " - ")
    data = [
        [image, "", "project", "", "", "", "", "document title", "", "", "", ""],
        ["", "", project_info["project_name"], "", "", "", "", document_description, "", "", "", ""],
        ["", "", "job number", "project leader", "issue date", "", "", "", "", "", "", ""],
        ["", "", project_info["job_number"], project_info["project_leader"], issue_date, "", "", "", "", "", "", ""],
        ["", "", "status code", "revision", "status description", "", "", name_nomenclature, "", "", "", ""],
        ["", "", project_info["status_code"], project_info["revision"], project_info["status_description"], "", "", document_name, "", "", "", ""],
    ]   
    return data


def create_title_block_table(data: list):
    table = Table(data, colWidths='*')
    styling = create_styling(len(data))
    table.setStyle(TableStyle(styling))
    return table


def build_title_block_pdf(fpth: pathlib.Path):
    data = construct_title_block_data()
    title_block_table = create_title_block_table(data)
    doc = SimpleDocTemplate(
        str(fpth), 
        pagesize=A4,
        leftMargin=0,
        rightMargin=0,
        bottomMargin=0, 
        topMargin=0
        )
    elements = [title_block_table]
    doc.build(elements)


if __name__ == "__main__":
    build_title_block_pdf(pathlib.Path(__file__).parent / "title_block.pdf")
