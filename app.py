from flask import Flask, Response
import os
import random

app = Flask(__name__)

# ▼ Zoznam SQL dotazov na precvičenie (pridaj si vlastné podľa potreby)
SQL_QUERIES = [
    "SELECT * FROM users WHERE active = 1;",
    "UPDATE products SET price = price * 0.9 WHERE category = 'Electronics';",
    "DELETE FROM sessions WHERE last_activity < NOW() - INTERVAL 30 DAY;",
    "INSERT INTO logs (user_id, action) VALUES (42, 'login');",
    "SELECT name, COUNT(*) FROM orders GROUP BY name HAVING COUNT(*) > 5;",
    "SELECT * FROM employees WHERE department = 'Sales' ORDER BY salary DESC;"
]

def build_svg(query: str) -> str:
    """Vytvorí SVG s vloženým SQL dotazom."""
    return f"""<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg">
  <style>
    .terminal {{ fill:#1e1e1e; stroke:#333; rx:10; ry:10; }}
    .titlebar {{ fill:#2d2d2d; }}
    .button {{ r:6; }}
    .text {{ font-family: monospace; fill:#fff; font-size:14px; }}
  </style>

  <rect class="terminal" width="500" height="200" rx="10" ry="10"/>
  <rect class="titlebar" width="500" height="30" rx="10" ry="10"/>
  <circle class="button" cx="15" cy="15" fill="#ff5f56"/>
  <circle class="button" cx="35" cy="15" fill="#ffbd2e"/>
  <circle class="button" cx="55" cy="15" fill="#27c93f"/>

  <text class="text" x="20" y="60">SQL practice query ⬇</text>
  <text class="text" x="20" y="90">{query}</text>
</svg>"""

@app.route("/")
def root_svg():
    """Hlavný endpoint vracajúci SVG so SQL dotazom."""
    query = random.choice(SQL_QUERIES)
    return Response(build_svg(query), mimetype="image/svg+xml")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
