# from fastapi import FastAPI
# from fastapi.responses import FileResponse
# from reportlab.lib.pagesizes import A4
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib import colors
# import datetime
# import requests

# app = FastAPI()

# # 🔗 Your real API link
# API_URL = "https://social-media-gab1.onrender.com/share"

# # ---- PDF Generator ----
# def generate_pdf_report(data, filename="report.pdf"):
#     styles = getSampleStyleSheet()
#     doc = SimpleDocTemplate(filename, pagesize=A4)
#     elements = []

#     elements.append(Paragraph("📑 Anti-India Campaign Detection Report", styles['Title']))
#     elements.append(Spacer(1, 12))
#     elements.append(Paragraph(f"Generated on: {datetime.datetime.now()}", styles['Normal']))
#     elements.append(Spacer(1, 24))

#     # Frequent Hashtags
#     if "frequent_hashtags" in data:
#         elements.append(Paragraph("🔥 Frequent Hashtags", styles['Heading2']))
#         for h in data["frequent_hashtags"]:
#             elements.append(Paragraph(f"- {h}", styles['Normal']))
#         elements.append(Spacer(1, 12))

#     # Top Accounts
#     if "top_accounts" in data:
#         elements.append(Paragraph("👤 Top Accounts", styles['Heading2']))
#         for acc in data["top_accounts"]:
#             elements.append(Paragraph(f"- {acc}", styles['Normal']))
#         elements.append(Spacer(1, 12))

#     # Time Bursts
#     if "time_bursts" in data:
#         elements.append(Paragraph("⏱ Time Bursts", styles['Heading2']))
#         tb_data = [["Time", "Posts"]] + [[str(k), str(v)] for k, v in data["time_bursts"].items()]
#         table = Table(tb_data, hAlign="LEFT")
#         table.setStyle(TableStyle([
#             ("BACKGROUND", (0,0), (-1,0), colors.lightblue),
#             ("TEXTCOLOR", (0,0), (-1,0), colors.white),
#             ("GRID", (0,0), (-1,-1), 1, colors.black),
#         ]))
#         elements.append(table)
#         elements.append(Spacer(1, 12))

#     # Influencers
#     if "influencers" in data:
#         elements.append(Paragraph("🌐 Influencers", styles['Heading2']))
#         for inf in data["influencers"]:
#             elements.append(Paragraph(f"- {inf}", styles['Normal']))
#         elements.append(Spacer(1, 12))

#     # Clusters
#     if "clusters" in data:
#         elements.append(Paragraph("🔗 Graph Clusters", styles['Heading2']))
#         for cluster in data["clusters"]:
#             if isinstance(cluster, list):
#                 elements.append(Paragraph(f"- {', '.join(cluster)}", styles['Normal']))
#             else:
#                 elements.append(Paragraph(f"- {cluster}", styles['Normal']))

#     doc.build(elements)
#     return filename

# # ---- API Endpoint ----
# @app.get("/report")
# def report():
#     """Fetch data from external API and generate PDF report."""
#     try:
#         response = requests.get(API_URL)
#         response.raise_for_status()
#         data = response.json()
#     except Exception as e:
#         return {"error": f"Failed to fetch API data: {e}"}

#     pdf_file = "campaign_report.pdf"
#     generate_pdf_report(data, pdf_file)
#     return FileResponse(pdf_file, media_type="application/pdf", filename=pdf_file)
