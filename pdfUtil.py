from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph
pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))  #注册字体
styles = getSampleStyleSheet()

def getStyle():
    paragraph_normal = ParagraphStyle(
        name='CustomParagraphStyle',
        parent=styles['Normal'],
        leading=20,  # 设置行间距（单位为磅，1 磅约等于 1/72 英寸）
        fontName='SimSun',  # 字体
        fontsize=16,  # 字号
    )
    paragraph_bold = ParagraphStyle(
        name='CustomParagraphStyle',
        parent=styles['Normal'],
        leading=20,  # 设置行间距（单位为磅，1 磅约等于 1/72 英寸）
        fontName='Helvetica-Bold',  # 字体
        fontsize=18,  # 字号
    )
    title_style = ParagraphStyle(
        name='Title',
        parent=styles['Title'],
        leading=30,
        fontName='Helvetica-Bold',
        fontSize=22,
    )
    return paragraph_normal, paragraph_bold, title_style


def createReport(results, pdf):
    paragraph_normal, paragraph_bold, title_style = getStyle()
    contents = [Paragraph('OCT Report', title_style)]
    for r in results:
        subtitle = 'frame_' + str(r['frame_index'])
        contents.append(Paragraph(subtitle, paragraph_bold))
    pdf.build(contents)

# # 使用示例：
# createReport("output.pdf")  # 替换为输出路径和文件名
