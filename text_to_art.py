# Vesion 0.2
# python text-to-art.py "a b c d e f h i j k l m n o p q r s t u b w x y z"

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
            if sequence[letter].upper() == ' ':
                art[0] += " "
                art[1] += " "
                art[2] += " "
                art[3] += " "
                art[4] += " "
            elif sequence[letter].upper() == 'A':
                art[0] += "⬛️⬛️⬛️"
                art[1] += "⬛️ ⬛️"
                art[2] += "⬛️⬛️⬛️"
                art[3] += "⬛️ ⬛️"
                art[4] += "⬛️ ⬛️"
            elif sequence[letter].upper() == 'B':
                art[0] += "⬛️⬛️ "
                art[1] += "⬛️ ⬛️"
                art[2] += "⬛️⬛️ "
                art[3] += "⬛️ ⬛️"
                art[4] += "⬛️⬛️ "
            elif sequence[letter].upper() == 'C':
                art[0] += "⬛️⬛️⬛️"
                art[1] += "⬛️   "
                art[2] += "⬛️   "
                art[3] += "⬛️   "
                art[4] += "⬛️⬛️⬛️"
            elif sequence[letter].upper() == 'D':
                art[0] += "⬛️⬛️ "
                art[1] += "⬛️ ⬛️"
                art[2] += "⬛️ ⬛️"
                art[3] += "⬛️ ⬛️"
                art[4] += "⬛️⬛️ "
            elif sequence[letter].upper() == 'E':
                art[0] += "⬛️⬛️⬛️"
                art[1] += "⬛️  "
                art[2] += "⬛️⬛️⬛️"
                art[3] += "⬛️  "
                art[4] += "⬛️⬛️⬛️"
            elif sequence[letter].upper() == 'F':
                art[0] += "⬛️⬛️⬛️"
                art[1] += "⬛️  "
                art[2] += "⬛️⬛️⬛️"
                art[3] += "⬛️  "
                art[4] += "⬛️  "
            elif sequence[letter].upper() == 'G':
                art[0] += "⬛️⬛️⬛️⬛️"
                art[1] += "⬛️   "
                art[2] += "⬛️ ⬛️⬛️"
                art[3] += "⬛️  ⬛️"
                art[4] += "⬛️⬛️⬛️⬛️"
            elif sequence[letter].upper() == 'H':
                art[0] += "⬛️ ⬛️"
                art[1] += "⬛️ ⬛️"
                art[2] += "⬛️⬛️⬛️"
                art[3] += "⬛️ ⬛️"
                art[4] += "⬛️ ⬛️"
            elif sequence[letter].upper() == 'I':
                art[0] += "⬛️⬛️⬛️"
                art[1] += " ⬛️ "
                art[2] += " ⬛️ "
                art[3] += " ⬛️ "
                art[4] += "⬛️⬛️⬛️"
            elif sequence[letter].upper() == 'J':
                art[0] += "⬛️⬛️⬛️"
                art[1] += "  ⬛️"
                art[2] += "  ⬛️"
                art[3] += "  ⬛️"
                art[4] += "⬛️⬛️ "
            elif sequence[letter].upper() == 'K':
                art[0] += "⬛️ ⬛️"
                art[1] += "⬛️⬛️ "
                art[2] += "⬛️  "
                art[3] += "⬛️⬛️ "
                art[4] += "⬛️ ⬛️"
            elif sequence[letter].upper() == 'L':
                art[0] += "⬛️  "
                art[1] += "⬛️  "
                art[2] += "⬛️  "
                art[3] += "⬛️  "
                art[4] += "⬛️⬛️⬛️"
            elif sequence[letter].upper() == 'M':
                art[0] += "⬛️   ⬛️"
                art[2] += "⬛️ ⬛️ ⬛️"
                art[3] += "⬛️   ⬛️"
                art[4] += "⬛️   ⬛️"
            elif sequence[letter].upper() == 'N':
                art[0] += "⬛️   ⬛️"
                art[1] += "⬛️⬛️  ⬛️"
                art[2] += "⬛️ ⬛️ ⬛️"
                art[3] += "⬛️  ⬛️⬛️"
                art[4] += "⬛️   ⬛️"
            elif sequence[letter].upper() == 'O':
                art[0] += "⬛️⬛️⬛️"
                art[1] += "⬛️ ⬛️"
                art[2] += "⬛️ ⬛️"
                art[3] += "⬛️ ⬛️"
                art[4] += "⬛️⬛️⬛️"
            elif sequence[letter].upper() == 'P':
                art[0] += "⬛️⬛️⬛️"
                art[1] += "⬛️ ⬛️"
                art[2] += "⬛️⬛️⬛️"
                art[3] += "⬛️  "
                art[4] += "⬛️  "
            elif sequence[letter].upper() == 'Q':
                art[0] += "⬛️⬛️⬛️ "
                art[1] += "⬛️ ⬛️ "
                art[2] += "⬛️ ⬛️ "
                art[3] += "⬛️ ⬛️ "
                art[4] += "⬛️⬛️⬛️⬛️"
            elif sequence[letter].upper() == 'R':
                art[0] += "⬛️⬛️⬛️"
                art[1] += "⬛️ ⬛️"
                art[2] += "⬛️ ⬛️"
                art[3] += "⬛️⬛️ "
                art[4] += "⬛️ ⬛️"
            elif sequence[letter].upper() == 'S':
                art[0] += "⬛️⬛️⬛️"
                art[1] += "⬛️  "
                art[2] += "⬛️⬛️⬛️"
                art[3] += "  ⬛️"
                art[4] += "⬛️⬛️⬛️"
            elif sequence[letter].upper() == 'T':
                art[0] += "⬛️⬛️⬛️"
                art[1] += " ⬛️ "
                art[2] += " ⬛️ "
                art[3] += " ⬛️ "
                art[4] += " ⬛️ "
            elif sequence[letter].upper() == 'U':
                art[0] += "⬛️ ⬛️"
                art[1] += "⬛️ ⬛️"
                art[2] += "⬛️ ⬛️"
                art[3] += "⬛️ ⬛️"
                art[4] += "⬛️⬛️⬛️"
            elif sequence[letter].upper() == 'V':
                art[0] += "⬛️   ⬛️"
                art[1] += "⬛️   ⬛️"
                art[2] += " ⬛️ ⬛️ "
                art[3] += " ⬛️ ⬛️ "
                art[4] += "  ⬛️  "
            elif sequence[letter].upper() == 'W':
                art[0] += "⬛️   ⬛️"
                art[1] += "⬛️   ⬛️"
                art[2] += "⬛️   ⬛️"
                art[3] += "⬛️ ⬛️ ⬛️"
                art[4] += "  ⬛️ ⬛️  "
            elif sequence[letter].upper() == 'X':
                art[0] += "⬛️   ⬛️"
                art[1] += " ⬛️ ⬛️ "
                art[2] += "  ⬛️  "
                art[3] += " ⬛️ ⬛️ "
                art[4] += "⬛️   ⬛️"
            elif sequence[letter].upper() == 'Y':
                art[0] += "⬛️   ⬛️"
                art[1] += " ⬛️ ⬛️ "
                art[2] += "  ⬛️  "
                art[3] += "  ⬛️  "
                art[4] += "  ⬛️  "
            elif sequence[letter].upper() == 'Z':
                art[0] += "⬛️⬛️⬛️⬛️"
                art[1] += "   ⬛️"
                art[2] += " ⬛️⬛️  "
                art[3] += "⬛️    "
                art[4] += "⬛️⬛️⬛️⬛️⬛️"
            letter += 1
            
        print("```")
        for row in art:
           print(row)
        print("```")
