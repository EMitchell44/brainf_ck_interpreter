import keyboard


def getch():
    key = None
    shifted_chars = {
        "!": "1",
        "@": "2",
        "#": "3",
        "$": "4",
        "%": "5",
        "^": "6",
        "&": "7",
        "*": "8",
        "(": "9",
        ")": "0",
        ":": ":",
        "\"": "'",
    }
    for letter in [chr(x) for x in range(65, 91)]:
        shifted_chars[letter] = letter.lower()
    unshifted_chars = {
        "[": "{",
        "]": "}",
        "\\": "|",
        ",": "<",
        ".": ">",
        "/": "?"

    }
    while True:
        keys = [chr(x) for x in range(32, 127)]
        for k in keys:
            if keyboard.is_pressed(k):
                if k in shifted_chars.keys():
                    if keyboard.is_pressed("shift"):
                        key = k
                    else:
                        key = shifted_chars[k]
                if k in unshifted_chars:
                    if keyboard.is_pressed("shift"):
                        key = unshifted_chars[k]
                    else:
                        key = k
            if key:
                if not keyboard.is_pressed(key):
                    return key
