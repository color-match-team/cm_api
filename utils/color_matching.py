import math
import json
import warnings
warnings.filterwarnings("ignore")

#with open('api/sample_data.json') as f:
#    sample = json.load(f)

def distance(color1, color2):
    return math.sqrt(
        (color1['L'] - color2['L']) ** 2 +
        (color1['A'] - color2['A']) ** 2 +
        (color1['B'] - color2['B']) ** 2
    )

def find_shortest_distance(color, data):
    shortest_distance = float('inf')
    product = None
    for item in data:
        dist = distance(color, item['color'])
        if dist < shortest_distance:
            shortest_distance = dist
            product = item
    return product

color_to_match = {
    "L": 10.60330918067893,
    "A": 13.480786348810863,
    "B": -25.02938394226518
}
"""
def rgb2lab ( inputColor ) :

   num = 0
   RGB = [0, 0, 0]

   for value in inputColor :
       value = float(value) / 255

       if value > 0.04045 :
           value = ( ( value + 0.055 ) / 1.055 ) ** 2.4
       else :
           value = value / 12.92

       RGB[num] = value * 100
       num = num + 1

   XYZ = [0, 0, 0,]

   X = RGB [0] * 0.4124 + RGB [1] * 0.3576 + RGB [2] * 0.1805
   Y = RGB [0] * 0.2126 + RGB [1] * 0.7152 + RGB [2] * 0.0722
   Z = RGB [0] * 0.0193 + RGB [1] * 0.1192 + RGB [2] * 0.9505
   XYZ[ 0 ] = round( X, 4 )
   XYZ[ 1 ] = round( Y, 4 )
   XYZ[ 2 ] = round( Z, 4 )

   XYZ[ 0 ] = float( XYZ[ 0 ] ) / 95.047         # ref_X =  95.047   Observer= 2°, Illuminant= D65
   XYZ[ 1 ] = float( XYZ[ 1 ] ) / 100.0          # ref_Y = 100.000
   XYZ[ 2 ] = float( XYZ[ 2 ] ) / 108.883        # ref_Z = 108.883

   num = 0
   for value in XYZ :

       if value > 0.008856 :
           value = value ** ( 0.3333333333333333 )
       else :
           value = ( 7.787 * value ) + ( 16 / 116 )

       XYZ[num] = value
       num = num + 1

   Lab = [0, 0, 0]

   L = ( 116 * XYZ[ 1 ] ) - 16
   a = 500 * ( XYZ[ 0 ] - XYZ[ 1 ] )
   b = 200 * ( XYZ[ 1 ] - XYZ[ 2 ] )

   Lab[ 0 ] = int(round( L, 4 ))
   Lab[ 1 ] = int(round( a, 4 ))
   Lab[ 2 ] = int(round( b, 4 ))

   lab_dict = {
       'L' : Lab[0],
       'A' : Lab[1],
       'B' : Lab[2]
   }
   return lab_dict

import math
"""
def rgb2lab(color):
    # Convert hex to RGB
    r = color[0]/255
    g = color[1]/255
    b = color[2]/255

    # Assuming sRGB (D65)
    r = r / 12.92 if r <= 0.04045 else math.pow((r + 0.055) / 1.055, 2.4)
    g = g / 12.92 if g <= 0.04045 else math.pow((g + 0.055) / 1.055, 2.4)
    b = b / 12.92 if b <= 0.04045 else math.pow((b + 0.055) / 1.055, 2.4)

    # Convert to XYZ
    X = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    Y = r * 0.2126729 + g * 0.7151522 + b * 0.072175
    Z = r * 0.0193339 + g * 0.119192 + b * 0.9503041

    # D65 standard referent
    ref_X = 0.95047
    ref_Y = 1.0
    ref_Z = 1.08883

    # Convert to Lab
    X = X / ref_X
    Y = Y / ref_Y
    Z = Z / ref_Z

    X = math.pow(X, 1/3) if X > 0.008856 else 7.787 * X + 16 / 116
    Y = math.pow(Y, 1/3) if Y > 0.008856 else 7.787 * Y + 16 / 116
    Z = math.pow(Z, 1/3) if Z > 0.008856 else 7.787 * Z + 16 / 116

    L = 116 * Y - 16
    A = 500 * (X - Y)
    B = 200 * (Y - Z)

    return {"L": L, "A": A, "B": B}

# Example usage
#print(hex_to_cielab("#FF5733"))

#print(find_shortest_distance(color_to_match, sample))