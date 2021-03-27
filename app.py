import pathlib

PROJECT_ROOT = root = pathlib.Path(__file__).parent.resolve()
TITLE = '# READMEOW\n'
DESC = f'{TITLE}\nProject desc.\n\n'


def generate_content():
    return ['## Content\ntest']


if __name__ == '__main__':
    readme_path = f'{root}/README.md'

    content = generate_content()
    # add title text
    with open(readme_path, "w") as f:
        f.write(DESC)
        for gif in content:
            f.write(gif)
