import os

TOP_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
ALL_WORDS_PATH = os.path.join(TOP_DIR, 'data', 'words_alpha.txt')
SASS_WORDS_PATH = os.path.join(TOP_DIR, 'data', 'sass_words.txt')

def file_exists(filepath: str, use_top_dir: bool = False) -> bool:
    filepath = _check_top_dir(filepath, use_top_dir)
    return os.path.exists(filepath)

def read_file(filepath: str, use_top_dir: bool = False) -> list[str]:
    filepath = _check_top_dir(filepath, use_top_dir)
    with open(os.path.join(TOP_DIR, filepath), 'r') as infile:
        return [
            line.strip()
            for line
            in infile.readlines()
        ]

def write_file(filepath: str, lines: list[str], use_top_dir: bool = False):
    filepath = _check_top_dir(filepath, use_top_dir)
    with open(os.path.join(TOP_DIR, filepath), 'w') as outfile:
        for line in lines:
            outfile.write(line + '\n')

def _check_top_dir(filepath: str, use_top_dir: bool) -> str:
    if use_top_dir:
        filepath = os.path.join(TOP_DIR, filepath)
    return filepath
