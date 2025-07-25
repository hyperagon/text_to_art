# Vesion 1.0, 5x5
# python text-to-art.py "a b c d e f g h i j k l m"
# python text-to-art.py "n o p q r s t u v w x y z"
# python text-to-art.py "1 2 3 4 5 6 7 8 9 0"

import sys

ART = {
" ":["  ", "  ", "  ", "  ", "  "],
"A":[
"╔═══╗",
"║   ║",
"╠═══╣",
"║   ║",
"║   ║",
],"B":[
"╔═══╗",
"║  ╔╝",
"╠══╣ ",
"║  ╚╗",
"╚═══╝",
],"C":[
"╔════",
"║    ",
"║    ",
"║    ",
"╚════",
],"D":[
"╔══╗ ",
"║  ╚╗",
"║   ║",
"║  ╔╝",
"╚══╝ ",
],"E":[
"╔════",
"║    ",
"╠═══ ",
"║    ",
"╚════",
],"F":[
"╔════",
"║    ",
"╠═══ ",
"║    ",
"║    ",
],"G":[
"╔═══ ",
"║    ",
"║ ══╗",
"║   ║",
"╚═══╝",
],"H":[
"║   ║",
"║   ║",
"╠═══╣",
"║   ║",
"║   ║",
],"I":[
"══╦══",
"  ║  ",
"  ║  ",
"  ║  ",
"══╩══",
],"J":[
"    ║",
"    ║",
"    ║",
"   ╔╝",
"═══╝ ",
],"K":[
"║   ║",
"║╔══╝",
"╠╣   ",
"║╚══╗",
"║   ║",
],"L":[
"║    ",
"║    ",
"║    ",
"║    ",
"╚════",
],"M":[
"╔═╦═╗",
"║ ║ ║",
"║   ║",
"║   ║",
"║   ║",
],"N":[
"╔═╗ ║",
"║ ║ ║",
"║ ╚╗║",
"║  ║║",
"║  ╚╝",
],"O":[
"╔═══╗",
"║   ║",
"║   ║",
"║   ║",
"╚═══╝",
],"P":[
"╔═══╗",
"║   ║",
"╠═══╝",
"║    ",
"║    ",
],"Q":[
"╔═══╗",
"║   ║",
"║   ║",
"║   ║",
"╚═══╣",
],"R":[
"╔═══╗",
"║   ║",
"╠═══╝",
"╠═══╗",
"║   ║",
],"S":[
"╔════",
"║    ",
"╚═══╗",
"    ║",
"════╝",
],"T":[
"══╦══",
"  ║  ",
"  ║  ",
"  ║  ",
"  ║  ",
],"U":[
"║   ║",
"║   ║",
"║   ║",
"║   ║",
"╚═══╝",
],"V":[
"║   ║",
"║   ║",
"╚╗ ╔╝",
" ║ ║ ",
" ╚╦╝ ",
],"W":[
"║   ║",
"║   ║",
"║   ║",
"║ ║ ║",
"╚═╩═╝",
],"X":[
"║   ║",
"╚═╦═╝",
"  ║  ",
"╔═╩═╗",
"║   ║",
],"Y":[
"║   ║",
"║   ║",
"╚═╦═╝",
"  ║  ",
"  ║  ",
],"Z":[
"════╗",
"   ╔╝",
" ╔═╝ ",
"╔╝   ",
"╚════",
],"1":[
"║",
"║",
"║",
"║",
"║",
],"2":[
"╔══╗",
"   ║",
"  ╔╝",
"╔═╝  ",
"╚═══",
],"3":[
"╔══╗",
"   ║",
" ══╣",
"   ║",
"╚══╝",
],"4":[
"║  ║",
"║  ║",
"╚══╣",
"   ║",
"   ║",
],"5":[
"╔══",
"║  ",
"╚═╗",
"  ║",
"══╝",
],"6":[
"╔══╗",
"║   ",
"╠══╗",
"║  ║",
"╚══╝",
],"7":[
"═══╗",
"   ║",
" ══╣",
"   ║",
"   ║",
],"8":[
"╔══╗",
"║  ║",
"╠══╣",
"║  ║",
"╚══╝",
],"9":[
"╔══╗",
"║  ║",
"╚══╣",
"   ║",
"   ║",
],"0":[
"╔══╗",
"║ ╔╣",
"║╔╝║",
"╠╝ ║",
"╚══╝",
],"+":[
"     ",
"  ║  ",
"══║══",
"  ║  ",
"     ",
],"-":[
"     ",
"     ",
"═════",
"     ",
"     ",
]
}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Text to Art: Usage = python text_to_art.py "TEXT"')
    else:
        sequence = sys.argv[1]
        print('Text to Arting', f'"{sequence}"')
        letter = 0
        art = ["", "", "", "", ""]
        while letter < len(sequence):
            target = sequence[letter].upper()
            #print(target)
            if target in ART:
                art[0] += ART[target][0]
                art[1] += ART[target][1]
                art[2] += ART[target][2]
                art[3] += ART[target][3]
                art[4] += ART[target][4]
            letter += 1
            
        print("```")
        for row in art:
           print(row)
        print("```")

