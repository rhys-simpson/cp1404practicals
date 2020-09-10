"""
Redo Pull request
CP1404 - Practical
Hex colours dictionary

Rhys Simpson
"""

hex_colours = {"AliceBlue": "#f08ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff", "beige":
               "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000", "BlanchedAlmond": "	#ffebcd", "blue1": 	"#0000ff",
               "BlueViolet": "#8a2be2"}
print(hex_colours)

colour = input("Enter a colour name: ")
while colour != "":
    print(colour, "code is", hex_colours.get(colour))
    colour = input("Enter a colour name: ")
