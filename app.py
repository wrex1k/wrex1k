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
        "Write a query to update the price of all products in the 'Electronics' category by reducing it by 10%.",
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
]

def build_svg(date_str, time_str, task, query):
    query_lines = query.split('\n')
    query_svg_lines = ""
    y = 150
    for line in query_lines:
        query_svg_lines += f'<tspan x="20" dy="20">{line}</tspan>'

    svg = f"""<svg viewBox="0 0 500 300" xmlns="http://www.w3.org/2000/svg">
  <style>
    .terminal {{ fill:#1e1e1e; stroke:#333; rx:10; ry:10; }}
    .titlebar {{ fill:#2d2d2d; }}
    .button {{ r:6; }}
    .text {{ font-family: monospace; fill:#fff; font-size:14px; }}
    .small {{ font-size: 12px; fill: #999; }}
  </style>

  <rect class="terminal" width="500" height="300" rx="10" ry="10"/>
  <rect class="titlebar" width="500" height="30" rx="10" ry="10"/>
  <circle class="button" cx="15" cy="15" fill="#ff5f56"/>
  <circle class="button" cx="35" cy="15" fill="#ffbd2e"/>
  <circle class="button" cx="55" cy="15" fill="#27c93f"/>

  <text class="text small" x="20" y="50">{date_str} | {time_str} | python sql_practice.py</text>
  <text class="text" x="20" y="80">Task: {task}</text>
  <text class="text" x="20" y="130">SQL query to complete:</text>
  <text class="text" x="20" y="150">{query_svg_lines}</text>
</svg>"""
    return svg

@app.route("/")
def root_svg():
    now = datetime.now()
    date_str = now.strftime("%d.%m.%Y")
    time_str = now.strftime("%H:%M:%S")
    
    task, query = random.choice(SQL_PRACTICE)

    svg = build_svg(date_str, time_str, task, query)
    return Response(svg, mimetype="image/svg+xml")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
