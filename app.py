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

def get_current_time():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


def generate_content():
    data = None
    with requests.get(url=URL, params=URL_PARAMS, verify=False) as r:
        if r.status_code != 200:
            raise r.raise_for_status()
        data = r.json()
        print(json.dumps(data, sort_keys=True, indent=4))
    return data


def generate_table():
    retval = []
    table_header = '<table>'
    table_footer = '</table>'
    table_row_start = '\n<tr>'
    table_row_end = '\n</tr>'

    # setup table
    retval += [table_header]

    for idx, content in enumerate(generate_content()):
        table_data = f'<td>{content}</td>'
        if idx % ITEMS_PER_ROW == 0:
            if idx != 0:
                # close the previous row
                retval.append(f'{table_row_end}')
            # create a new row
            retval.append(f'{table_row_start}\n\t')
        # append the actual data
        retval.append(table_data)
    # close the previous row
    retval.append(f'{table_row_end}\n')
    # finish table
    retval.append(table_footer)
    return retval


if __name__ == '__main__':
    readme_path = f'{root}/README.md'
    with open(readme_path, "w") as f:
        f.write(DESC)
        try:
            for gif in generate_table():
                f.write(gif)
        except Exception as exc:
            f.write(f'<p style="color:red">Error: {exc}</p>')
        f.write(f'\n\nLast updated at {get_current_time()} UTC')
