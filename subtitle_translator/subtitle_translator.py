import argparse
from tqdm import tqdm
import deepl


class SubtitleTranslator:
    def __init__(self, api_key, target_lang, input_file, output_file):
        self.translator = deepl.Translator(api_key)
        self.target_lang = target_lang
        self.input_file = input_file
        self.output_file = output_file

    def translate_subtitles(self):

        with open(self.input_file) as f:
            lines = f.readlines()

        with open(self.output_file, 'w', encoding="utf-8") as f:
            text = ''
            for line in tqdm(lines):
                line = line.strip()

                if self.is_sentence(line):
                    text = f'{text}{line}'
                else:
                    if text:
                        text = self.translator.translate_text(text, target_lang=self.target_lang).text + '\n'

                    f.write(f'{text}{line}\n')
                    text = ''

    @classmethod
    def is_sentence(cls, line: str) -> bool:
        return cls._is_sentence(line) and not cls._is_time(line)
    
    @staticmethod
    def _is_time(line: str) -> bool:
        return '-->' in line

    @staticmethod
    def _is_sentence(line: str) -> bool:
        line_parts = line.split()
        return len(line_parts) > 1


def main(args):
    translator = SubtitleTranslator('YOUR_API_KEY', 'PL', args.input, args.output)
    translator.translate_subtitles()

def parse_args():
    parser = argparse.ArgumentParser(description='Translate subtitles')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    main(args)
