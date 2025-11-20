from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('SimSun', 'font/SimSun.ttf'))  # 注册字体
styles = getSampleStyleSheet()


def getStyle():
    paragraph_normal = ParagraphStyle(
        name='CustomParagraphStyle',
        parent=styles['Normal'],
        leading=20,  # 设置行间距（单位为磅，1 磅约等于 1/72 英寸）
        fontName='SimSun',  # 字体
        fontSize=14,  # 字号
        spaceAfter=15,  # 段落后间距
    )
    paragraph_bold = ParagraphStyle(
        name='CustomParagraphStyle',
        parent=styles['Normal'],
        leading=30,  # 设置行间距（单位为磅，1 磅约等于 1/72 英寸）
        fontName='Helvetica-Bold',  # 字体
        fontSize=15,  # 字号
    )
    title_style = ParagraphStyle(
        name='Title',
        parent=styles['Title'],
        leading=40,
        fontName='Helvetica-Bold',
        fontSize=22,
    )
    return paragraph_normal, paragraph_bold, title_style
