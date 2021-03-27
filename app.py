import pathlib

PROJECT_ROOT = root = pathlib.Path(__file__).parent.resolve()
TITLE = '# READMEOW\n'
DESC = f'{TITLE}\nProject desc.\n\n'

def get_time():
    from datetime import datetime
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def generate_content():
    section_header = '## Content\n\n'
    return [section_header, f'{get_time()}']


if __name__ == '__main__':
    readme_path = f'{root}/README.md'

    content = generate_content()
    # add title text
    with open(readme_path, "w") as f:
        f.write(DESC)
        for gif in content:
            f.write(gif)
