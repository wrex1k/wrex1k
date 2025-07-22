from flask import Flask, Response
from datetime import datetime
import os
import random

app = Flask(__name__)

SQL_PRACTICE = [
    (
        "Write a query to select the name and email from the users table where active is 1, ordered by name ascending.",
        "SELECT name, email\nFROM users\nWHERE active = ___\nORDER BY ___ ASC;"
    ),
    (
        'Write a query to update the price of all products in the "Electronics" category by reducing it by 10%.',
        "UPDATE products\nSET price = price * 0.9\nWHERE category = '___';"
    ),
    (
        "Write a query to delete all sessions that have been inactive for more than 30 days.",
        "DELETE FROM sessions\nWHERE last_activity < NOW() - INTERVAL ___ DAY;"
    ),
    (
        "Write a query to insert a login action into the logs table for user id 42.",
        "INSERT INTO logs (user_id, action)\nVALUES (42, '___');"
    ),
    (
        "Write a query to select employee names and salaries in the Sales department ordered by salary descending.",
        "SELECT name, salary\nFROM employees\nWHERE department = '___'\nORDER BY salary DESC;"
    ),
    (
        "Write a query to find all orders placed in the last 7 days, ordered by order date descending.",
        "SELECT *\nFROM orders\nWHERE order_date >= NOW() - INTERVAL ___ DAY\nORDER BY order_date DESC;"
    ),
    (
        "Write a query to count the number of active users grouped by their country.",
        "SELECT country, COUNT(*)\nFROM users\nWHERE active = 1\nGROUP BY country;"
    ),
]

def build_svg(date_str, task, query):
    max_line_length = 40
    words = task.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:
            if current_line != "":
                current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    task_svg_lines = ""
    for i, line in enumerate(lines):
        dy = 20 if i > 0 else 0
        task_svg_lines += f'<tspan x="100" dy="{dy}">{line}</tspan>\n'

    svg = f"""<svg viewBox="0 0 500 300" xmlns="http://www.w3.org/2000/svg">
  <style>
    .terminal {{ fill:#1e1e1e; stroke:#333; rx:10; ry:10; }}
    .titlebar {{ fill:#2d2d2d; }}
    .button {{ r:6; }}
    .text {{ font-family: monospace; fill:#fff; font-size:14px; white-space: pre; }}
    .date {{ font-family: monospace; fill:#666; font-size:14px; }}
  </style>

  <rect class="terminal" width="500" height="300" rx="10" ry="10"/>
  <rect class="titlebar" width="500" height="30" rx="10" ry="10"/>
  <circle class="button" cx="15" cy="15" fill="#ff5f56"/>
  <circle class="button" cx="35" cy="15" fill="#ffbd2e"/>
  <circle class="button" cx="55" cy="15" fill="#27c93f"/>

  <text class="text small" x="20" y="50">Microsoft Windows [Version 10.0.26100.4351]</text>
  <text class="text small" x="20" y="70">(c) Microsoft Corporation. All rights reserved.</text>

  <text class="text" x="20" y="100">C:\\Users\\wrex1k&gt; python sql_practice.py</text>

  <text class="date" x="20" y="130">{date_str}</text>
  <text class="text" x="85" y="130">|{task_svg_lines}</text>

  <text class="text" x="20" y="190">C:\\Users\\wrex1k&gt; SQL query to complete:</text>
  
  <text class="text" x="20" y="210"><tspan x="20" dy="0">{query.replace('\n', '<tspan x=\'20\' dy=\'20\'>')}</tspan></text>

</svg>"""
    return svg

@app.route("/")
def root_svg():
    now = datetime.now()
    date_str = now.strftime("%-d.%-m")
    task, query = random.choice(SQL_PRACTICE)
    svg = build_svg(date_str, task, query)
    return Response(svg, mimetype="image/svg+xml")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
