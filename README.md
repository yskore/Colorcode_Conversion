# Colorcode_editor
**Code I wrote for a GUI representation of different color code conversions. e.g RGB to cmyk**

File consists of a series of tests, GUI application and the following relevant functions:

str5_cymk:
Returns: String representation of cmyk in the form "(C, M, Y, K)".
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    Example: if str(cmyk) is
          '(0.0,31.3725490196,31.3725490196,0.0)'
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces\
    after the
    commas. These must be there.
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    
str5_hsv:
Returns: String representation of hsv in the form "(H, S, V)".
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    Example: if str(hsv) is 
          '(0.0,0.313725490196,1.0)'
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    
rgb_to_cymk:
Returns: color rgb in space CMYK, with the most black possible.
    with the formulae from en.wikipedia.org/wiki/CMYK_color_model.
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object.
   
cymk_to_rgb:
Returns : color CMYK in space RGB
    With the formulae from en.wikipedia.org/wiki/CMYK_color_model.
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    
rgb_to_hsv:
Return: color rgb in HSV color space
    Formulae from wikipedia.org/wiki/HSV_color_space.
    Parameter rgb: the color to convert to a HSV object
    Precondition: rgb is an RGB object.
    
hsv_to_rgb:
Returns: color in RGB color space.
    With the formulae from http://en.wikipedia.org/wiki/HSV_color_space.
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    
    
