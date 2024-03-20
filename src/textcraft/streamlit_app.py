import streamlit as st
from pathlib import Path
import json


dir_config = Path(__file__).parent.parent.parent / "config"
dir_templates = dir_config / "templates"
dir_templates.mkdir(parents=True, exist_ok=True)


if len(list(dir_templates.iterdir())) == 0:
    print("No templates found, creating example template")
    dir_template = dir_templates / "example"
    dir_template.mkdir(parents=True, exist_ok=True)
    (dir_template / "meta.json").write_text(
        json.dumps({"replace": {"{{name}}": "Name", "{{age}}": "Age"}})
    )
    (dir_template / "template.txt").write_text("Name: {{name}}, Age: {{age}}")

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
