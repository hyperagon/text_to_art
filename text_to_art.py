# Vesion 0.1

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Text to Art: Usage = python text_to_art.py "TEXT"')
    else:
        sequence = sys.argv[1]
        print('Text to Arting', f'"{sequence}"')
        letter = 0
        art = ["", "", "", "", ""]
        while letter < len(sequence):
            if sequence[letter].lower() == ' ':
                art[0] += " "
                art[1] += " "
                art[2] += " "
                art[3] += " "
                art[4] += " "
            if sequence[letter].lower() == 'a':
                art[0] += " ⬛️ "
                art[1] += "⬛️ ⬛️"
                art[2] += "⬛️⬛️⬛️"
                art[3] += "⬛️ ⬛️"
                art[4] += "⬛️ ⬛️"
            if sequence[letter].lower() == 'b':
                art[0] += "⬛️⬛️ "
                art[1] += "⬛️  ⬛️⬛️"
                art[2] += "⬛️⬛️⬛️  "
                art[3] += "⬛️  ⬛️⬛️"
                art[4] += "⬛️⬛️⬛️  "
            letter += 1

        print("```")
        for row in art:
           print(row)
        print("```")
