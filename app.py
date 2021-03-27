import pathlib

PROJECT_ROOT = root = pathlib.Path(__file__).parent.resolve()
TITLE = '# READMEOW\n'
DESC = f'{TITLE}\nA self-rewriting README powered by GitHub Actions to display cat gifs.\n\n'
ITEMS_TOTAL = 12
ITEMS_PER_ROW = 3


def generate_content():
    from datetime import datetime
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def generate_table():
    retval = []
    table_header = '<table>'
    table_footer = '</table>'
    table_row_start = '\n<tr>'
    table_row_end = '\n</tr>'

    # setup table
    retval += [table_header]

    for idx in range(ITEMS_TOTAL):
        content = generate_content()
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
    content = generate_table()
    with open(readme_path, "w") as f:
        f.write(DESC)
        for gif in content:
            f.write(gif)
