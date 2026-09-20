import openpyxl
import json

wb = openpyxl.load_workbook('topics.xlsx')
sheet = wb.active

topics = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    if row[0]:  # Ensure there is a topic
        topics.append({
            "Topic": row[0],
            "Label": row[1] if len(row) > 1 else "",
            "Hook": row[2] if len(row) > 2 else "",
            "Research": row[3] if len(row) > 3 else ""
        })

with open('topics_queue.json', 'w') as f:
    json.dump(topics, f, indent=4)

print(f"Successfully extracted {len(topics)} topics to topics_queue.json")
