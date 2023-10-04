import argparse
from fontTools.ttLib import TTFont
import os

def write_js(ttf_path, output_path):
    def cvt_name(name):
        words = name.split("-")
        return words[0] + "".join(w.capitalize() for w in words[1:])
    font = TTFont(ttf_path)
    glyphs = font.getGlyphSet()
    license_list = str(license).splitlines()
    bestCmap = font.getBestCmap()
    glyphs = {cvt_name(name): code for code, name in bestCmap.items()}

    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
    with open(output_path, "w") as f:
        for line in license_list:
            f.write("// " + line + "\n")
        f.write("\n\nvar Icon = { \n")

        for name, id in glyphs.items():
            f.write(f"  \"{name}\" : \"\\u{{{id:04X}}}\",\n")
        f.write("}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    description='Generate Qml Bridge of Material Design Icon')
    parser.add_argument('-f',
                        '--file',
                        type=str,
                        required=True,
                        help='the path to the TTF file')
    parser.add_argument('-o', "--output", type=str, default="./Icon.js")

    args = parser.parse_args()
    write_js(args.file, args.output)