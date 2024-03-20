#!/usr/bin/env python3

import subprocess

subprocess.run(["/workspace/.venv/bin/streamlit", "run", "/workspace/src/textcraft/streamlit_app.py"], check=True)