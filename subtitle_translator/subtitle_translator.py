import argparse
from tqdm import tqdm
from googletrans import Translator



def parse_args():
    parser = argparse.ArgumentParser(description='Translate subtitles')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    return parser.parse_args()


def translate_subtitles(input_file, output_file):
    translator = Translator()

    with open(input_file) as f:
        lines = f.readlines()

    with open(output_file, 'w', encoding="utf-8") as f:
        text = ''
        for line in lines:
            line = line.strip()
            line_parts = line.split()

            if len(line_parts) > 2 and '-->' not in line:
                text = f'{text}{line}'
            else:
                if text:
                    text = translator.translate(text, dest='pl').text
                print(f'"*{text}{line}\n*"')
                f.write(f'{text}{line}\n')
                text = ''


if __name__ == '__main__':
    args = parse_args()
    translate_subtitles(args.input, args.output)
