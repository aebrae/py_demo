#!/usr/bin/env python3
"""definition of generate_report function to build PDF reports"""

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
        report = SimpleDocTemplate(attachment)
        styles = getSampleStyleSheet()
        report_title = Paragraph(title, styles["h1"])
        report_table = Table(data=paragraph,hAlign="LEFT")
        report.build([report_title, report_table])
