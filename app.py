import pathlib
import requests
import os
import json
from datetime import datetime

PROJECT_ROOT = root = pathlib.Path(__file__).parent.resolve()
TITLE = '# READMEOW\n'
DESC = f'{TITLE}\nA self-rewriting README powered by GitHub Actions to display cat gifs.\n\n'
ITEMS_PER_ROW = 3

API_KEY = os.environ.get('GIPHY_API_KEY')
URL = f'http://api.giphy.com/v1/gifs/search'
SEARCH_STR = 'CAT'
SEARCH_LIMIT = 12
URL_PARAMS = params = {
    "q": SEARCH_STR,
    "api_key": API_KEY,
    "limit": SEARCH_LIMIT
}
IMG_CSS = '\
<style type="text/css"> \
    #photos { \
    /* Prevent vertical gaps */ \
    line-height: 0; \
    -webkit-column-count: 3; \
    -webkit-column-gap:   0; \
    -moz-column-count:    3; \
    -moz-column-gap:      0; \
    column-count:         3; \
    column-gap:           0; \
    } \
    #photos img { \
    width: 100% !important;\
    height: auto !important;\
    }\
</style>'


def get_current_time():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


def generate_content():
    with requests.get(url=URL, params=URL_PARAMS, verify=False) as r:
        if r.status_code != 200:
            raise r.raise_for_status()
        return r.json().get('data')
    return None


def generate_img(title, image):
    width = image.get('width')
    height = image.get('height')
    source = image.get('url')
    return f'<img src="{source}" width="{width}" height="{height}" title="{title}">'

def generate_table():
    retval = [f'## Cats\n\n{IMG_CSS}\n<section id="photos">\n']
    for idx, content in enumerate(generate_content()):
        img = generate_img(content.get('title'), content.get('images').get('downsized_medium'))
        table_data = f'{img}'
        # append the actual data
        retval.append(table_data)
    retval.append('</section>')
    return retval


if __name__ == '__main__':
    readme_path = f'{root}/README.md'
    with open(readme_path, "w") as f:
        f.write(DESC)
        try:
            for gif in generate_table():
                f.write(gif)
        except Exception as exc:
            import traceback
            traceback.print_exc()
            f.write(f'<p style="color:red">Error: {exc}</p>')
        f.write(f'\n\nLast updated at {get_current_time()} UTC')
