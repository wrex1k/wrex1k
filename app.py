from flask import Flask, Response
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Welcome to the dynamic terminal SVG!</h1>
    <p><a href="/terminal.svg" target="_blank">Open terminal.svg</a></p>
    <img src="/terminal.svg" alt="Terminal SVG">
    """

@app.route("/terminal.svg")
def terminal_svg():
    current_time = datetime.now().strftime("%H:%M:%S")

    svg = f"""<svg viewBox="0 0 500 300" xmlns="http://www.w3.org/2000/svg">
  <style>
    .terminal {{ fill: #1e1e1e; stroke: #333; rx: 10; ry: 10; }}
    .titlebar {{ fill: #2d2d2d; }}
    .button {{ r: 6; }}
    .text {{ font-family: monospace; fill: #fff; font-size: 14px; }}
    .blink {{ animation: blink 1s steps(2, start) infinite; }}
    @keyframes blink {{ to {{ visibility: hidden; }} }}
  </style>

  <rect class="terminal" width="500" height="300" rx="10" ry="10"/>
  <rect class="titlebar" width="500" height="30" rx="10" ry="10"/>
  <circle class="button" cx="15" cy="15" fill="#ff5f56"/>
  <circle class="button" cx="35" cy="15" fill="#ffbd2e"/>
  <circle class="button" cx="55" cy="15" fill="#27c93f"/>

  <text class="text" x="20" y="60">Microsoft Windows [Version 10.0.22631.3737]</text>
  <text class="text" x="20" y="80">(c) Microsoft Corporation. All rights reserved.</text>
  <text class="text" x="20" y="110">C:\\Users\\wrex1k&gt; cd Desktop</text>
  <text class="text" x="20" y="130">C:\\Users\\wrex1k\\Desktop&gt; python time.py</text>
  <text class="text" x="20" y="150">{current_time}</text>
  <text class="text blink" x="20" y="170">_</text>
</svg>"""

    return Response(svg, mimetype='image/svg+xml')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
