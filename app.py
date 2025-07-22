from flask import Flask, Response
from datetime import datetime
import os
import random
import pytz

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
    max_line_length = 50
    words = task.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:
            current_line += (" " if current_line else "") + word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    task_svg = ""
    for i, line in enumerate(lines):
        task_svg += f'<tspan x="20" dy="{20 if i > 0 else 0}">{line}</tspan>\n'

    query_lines = query.split("\n")
    query_svg = ""
    for i, line in enumerate(query_lines):
        query_svg += f'<tspan x="20" dy="{20 if i > 0 else 0}">{line}</tspan>\n'

    svg = f"""<svg viewBox="0 0 500 300" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="300" rx="10" ry="10" fill="#1e1e1e" stroke="#333"/>
  <rect width="500" height="30" rx="10" ry="10" fill="#2d2d2d"/>
  
  <circle cx="15" cy="15" r="6" fill="#ff5f56"/>
  <circle cx="35" cy="15" r="6" fill="#ffbd2e"/>
  <circle cx="55" cy="15" r="6" fill="#27c93f"/>

  <text x="20" y="50" font-family="monospace" fill="#999" font-size="12px">
    {date_str} | python sql_practice.py
  </text>

  <text x="20" y="80" font-family="monospace" fill="#fff" font-size="14px">
    {task_svg}
  </text>

  <text x="20" y="{100 + 20 * len(lines)}" font-family="monospace" fill="#fff" font-size="14px">
    SQL query to complete:
  </text>

  <text x="20" y="{120 + 20 * len(lines)}" font-family="monospace" fill="#fff" font-size="14px">
    {query_svg}
  </text>
</svg>"""
    return svg

@app.route("/")
def root_svg():
    tz = pytz.timezone("Europe/Bratislava")
    now = datetime.now(tz)
    date_str = now.strftime("%-d.%-m.%Y | %H:%M:%S")
    task, query = random.choice(SQL_PRACTICE)
    svg = build_svg(date_str, task, query)
    return Response(svg, mimetype="image/svg+xml")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
