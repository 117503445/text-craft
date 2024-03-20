import streamlit as st
from pathlib import Path
import json


dir_config = Path(__file__).parent.parent.parent / "config"
dir_templates = dir_config / "templates"

for dir_template in dir_templates.iterdir():

    # dir_template = dir_templates / "docker-compose"

    # 标题
    st.header(dir_template.name)

    meta = json.loads((dir_template / "meta.json").read_text())
    template = (dir_template / "template.txt").read_text()

    actual_dict = {}

    replace_dict = meta["replace"]

    for k, v in replace_dict.items():
        s = st.text_input(v)
        if s:
            actual_dict[k] = s

    for k, v in actual_dict.items():
        template = template.replace(k, v)


    language = meta.get("language", "python")

    st.code(template, language)
