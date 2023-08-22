from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph

import config

pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))  #注册字体
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


def createReport(result, pdf):
    if type(pdf) == str:
        pdf = SimpleDocTemplate(pdf)
    paragraph_normal, paragraph_bold, title_style = getStyle()
    contents = [Paragraph('OCT Report', title_style)]
    summary_all = '共检测到{}帧存在病灶'.format(len(result))
    for r in result:
        subtitle = 'frame_' + str(r['frame_index']) + ':'
        contents.append(Paragraph(subtitle, paragraph_bold))
        para_content = '共存在{}种病灶。<br/>'.format(len(config.NIDUS_TYPE))

        for nidus in config.NIDUS_TYPE:
            if len(r[nidus]) <= 0:
                continue
            para_content += (nidus + ':<br/>')
            for rect in r[nidus]:
                para_content += '病灶位置：左上角坐标({}, {})，右下角坐标({}, {})<br/>'.format(rect[0], rect[1], rect[2], rect[3])
        contents.append(Paragraph(para_content, paragraph_normal))

    pdf.build(contents)

# 使用示例：
results = [{
    'frame_index': 0,
    'js': [[0, 0, 100, 100, 0.9]],
    'kq': [[0, 0, 100, 100, 0.9]],
    'xs': [[0, 0, 100, 100, 0.9]],
},{
    'frame_index': 1,
    'js': [[0, 0, 100, 100, 0.9]],
    'kq': [[0, 0, 100, 100, 0.9]],
    'xs': [[0, 0, 100, 100, 0.9]],
},{
    'frame_index': 2,
    'js': [[0, 0, 100, 100, 0.9]],
    'kq': [[0, 0, 100, 100, 0.9]],
    'xs': [[0, 0, 100, 100, 0.9]],
}
]
createReport(results, "output.pdf")  # 替换为输出路径和文件名
