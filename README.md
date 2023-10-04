# Material-Design-Icon-Qml-Bridge-Generator
A python script to generate qml bridge of material design icon. It is possible to import `generator.py` to your own python file, you can call `write_js(tff_path, output_path)` to read tff from `ttf_path` and write js file to `output_path`.

## How to convert materialdesignicons.ttf to .js?
1. Download the lastest Material Design Icons [here](https://pictogrammers.com/library/mdi/)
2. Use the following command to convert
```sh
python generator.py -f path/to/your/ttf -o output/path/Icon.js
```
`-f`[required]: Specify the `materialdesignicons.ttf` file
`-o`[optional]: Specify the ouput path. By default, it is `./Icon.js`.

## How to use Icon.js in Qt Quick/Qml?
1. Add the font file, and Icon.js to the project's QRC file
2. Load the font, see [How to load font](#how-to-load-font)
3. Import `Icon.js` in any QML file where icons will be referenced: `import "Icon.js" as MdiFont`
4. Add the desired icon to any QML item that can display text, e.g. `MdiFont.Icon.accountCowboyHat`

## How to load font?
There are various ways to load font
1. Load in Qml
```qml
FontLoader {
    id: materialFont
    source: "qrc:/fonts/materialdesignicons.ttf"
}

Text {
    text: MdiFont.Icon.accountCowBoyHat
    font.family: materialFont.name
}
```
2. Load in PySide6
In python file
```py
from PySide6.QtGui import QFontDatabase
QFontDatabase.addApplicationFont("qrc:/fonts/materialdesignicons.ttf")
```
In Qml
```qml
Text {
    text: MdiFont.Icon.accountCowBoyHat
    font.family: "Material Font Icons"
}
```
3. Load in C++
In C++ file
```cpp
QFontDatabase::addApplicationFont("qrc:/fonts/materialdesignicons.ttf");
```
In Qml
```qml
Text {
    text: MdiFont.Icon.accountCowBoyHat
    font.family: "Material Font Icons"
}
```
