import json
import os

manifest_path = 'static/.vite/manifest.json'
template_path = 'index.html'

def update_template_with_vite_assets(manifest_path, template_path):
    with open(manifest_path, 'r') as manifest_file:
        manifest = json.load(manifest_file)

    js_file = css_file = None
    for key, value in manifest.items():
        if value.get('isEntry'):
            if key.endswith('.js'):
                js_file = value['file']
            elif key.endswith('.css'):
                css_file = value['file']

    with open(template_path, 'r') as template_file:
        content = template_file.read()

    if js_file:
        content = content.replace('{% static \'main-BySKFQF.js\' %}', f"{{% static '{js_file}' %}}")
    if css_file:
        content = content.replace('{% static \'main-BGMQSKmu.css\' %}', f"{{% static '{css_file}' %}}")

    with open(template_path, 'w') as template_file:
        template_file.write(content)

if __name__ == "__main__":
    if os.path.exists(manifest_path) and os.path.exists(template_path):
        update_template_with_vite_assets(manifest_path, template_path)
        print(f"Template {template_path} updated with Vite assets from {manifest_path}.")
    else:
        print(f"Error: {manifest_path} or {template_path} not found.")
