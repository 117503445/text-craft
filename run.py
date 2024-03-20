#!/usr/bin/env python3

import subprocess
from pathlib import Path

dev_streamlit = "/workspace/.venv/bin/streamlit"
if Path(dev_streamlit).exists():
    dev_streamlit_cmd = "/workspace/.venv/bin/streamlit"
else:
    dev_streamlit_cmd = "streamlit"

subprocess.run(["streamlit", "run", "/workspace/src/textcraft/streamlit_app.py"], check=True)