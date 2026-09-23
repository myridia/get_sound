import os, time, sys, time, random
import argparse
from gtts import gTTS


class Get_sound:
    def __init__(self):
        print("...init class")
        self.words = []
        self.lang = ""

    def set_words(self, list):
        print("...words")
        with open(list, "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                self.words.append(word)
        return self.words

    def save_sound(self, folder):
        path = "{0}/{1}".format(folder, self.lang)
        if not os.path.exists(path):
            os.makedirs(path)

        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        for k, i in enumerate(self.words):
            filename = "{0}.mp3".format(i)
            if filename not in files:
                time.sleep(random.randint(0, 5))
                file_path = "{0}/{1}".format(path, filename)
                tts = gTTS(i, lang=self.lang, slow=True)
                tts.save(file_path)
                print("{0}/{1} \t {2}".format(k, len(self.words), file_path))


if __name__ == "__main__":
    example_text = """example:
     ./get_sound.bin --text="กระสอบทรายซ้อมมวย" --lang=th
    """
    parser = argparse.ArgumentParser(
        description="Get Sound",
        epilog=example_text,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--text", type=str, help="enter text", required=False)
    parser.add_argument("--list", type=str, help="enter list", required=False)
    parser.add_argument("--lang", type=str, help="enter lang", required=True)
    args = parser.parse_args()
    text = args.text
    list = args.list

    f = Get_sound()
    f.lang = args.lang
    if list:
        f.set_words(list)
        f.save_sound("sounds")

        """
#! /usr/bin/env python
from gtts import gTTS

# Process line by line (better for large files)

"""
"""

"""
