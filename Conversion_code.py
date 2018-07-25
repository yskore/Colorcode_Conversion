# a3test.py
# Kore Ayoade (koa5)
# Thursday October 6th
""" Functions for Assignment A3"""

import colormodel
import math

def complement_rgb(rgb):
    """Returns: the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object"""
    # THIS IS WRONG.  FIX IT
    return colormodel.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def round(number, places):
    """Returns: the number rounded to the given number of decimal places.
    
    The value returned is a float.
    
    This function is more stable than the built-in round.  The built-in round
    has weird behavior where round(100.55,1) is 100.5 while round(100.45,1) is
    also 100.5.  We want to ensure that anything ending in a 5 is rounded UP.
    
    It is possible to write this function without the second precondition on
    places. If you want to do that, we leave that as an optional challenge.
    
    Parameter number: the number to round to the given decimal place
    Precondition: number is an int or float
    
    Parameter places: the decimal place to round to
    Precondition: places is an int; 0 <= places <= 3"""
    # To get the desired output, do the following
    #   1. Shift the number "to the left" so that the position to round to is
    #left of 
    #      the decimal place.  For example, if you are rounding 100.556 to the
    #first 
    #      decimal place, the number becomes 1005.56.  If you are rounding to
    #the second 
    #      decimal place, it becomes 10055.6.  If you are rounding 100.556 to
    #the nearest 
    #      integer, it remains 100.556.
    #   2. Add 0.5 to this number
    #   3. Convert the number to an int, cutting it off to the right of the
    #decimal.
    #   4. Shift the number back "to the right" the same amount that you did to
    #the left.
    #      Suppose that in step 1 you converted 100.556 to 1005.56.
    #In this case, 
    #      divide the number by 10 to put it back.
    
    if places==1:
        number=float(number)
        number=number*(10.0**places)
        number= number+0.5
        number= int(number)
        number= float(number)
        number= number/(10.0*places)
        
        
        
    if places== 2:
        number=float(number)
        number= number*(10.0**places)
        number= number+0.5
        number= int(number)
        number= float(number)
        number= number/(10.0**places)
        
    if places== 3:
        number=float(number)
        number= number*(10.0**places)
        number= number+0.5
        number= int(number)
        number= float(number)
        number= number/(10.0**places)
    
    return float(number)
        
    
       # Stub


def str5(value):
    """ Returns: value as a string, but expand or round to be exactly 5\
    characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360."""
    # Note:Obviously, you want to use the function round() that you just defined. 
    # However, remember that the rounding takes place at a different place
    #depending 
    # on how big value is. Look at the examples in the specification.
    
    value= str(value)
    length= len(value)
    dp= value.find('.')
    
    if '.' in value and length > 5 :
        value = str(value)
        length = len(value)
    
        #point = value.index('.')
        #before_point = value[:point]
        #length_before_point = len(before_point)
        round_to = 4- value.index('.')
        #value= float(value)
        new_value = round(value, round_to)
        new_value = str(new_value)
        value = new_value
        value= value[:5]
        
        if len(value)< 5 :
            add_zero= 5- (len(value))
            value=value+('0'*(add_zero))
            value= str(value)
    elif dp== -1:
        length_value= len(value)
        add= 5-(length_value+1)
        value= value+'.0'
        
    elif len(value)< 5 :
            add_zero= 5- (len(value))
            value=value+('0'*(add_zero))
            value= str(value)
    else:
        value= value
        
        
        #return new_value
    return value

        
    
    
    
    
       # Stub


def str5_cmyk(cmyk):
    """Returns: String representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces\
    after the
    commas. These must be there.
    
    Parameter cmtk: the color to convert to a string
    Precondition: cmyk is an CMYK object."""
    #value= float(str5(cmyk))
    c= str5(cmyk.cyan)
    m= str5(cmyk.magenta)
    y= str5(cmyk.yellow)
    k= str5(cmyk.black)
    
    return '('+str5(c)+', '+str5(m)+', '+str5(y)+', '+str5(k)+')'
   
    #x= colormodel.CMYK(2.0,3.0,4.0,5.0)
    
    
    
    
    #c= colormodel.CMYK[0]
    #m= colormodel.cmyk[1]
    #y= colormodel.cmyk[2]
    #k= colormodel.cmyk[3]
    
    
    
    
    
       # Stub


def str5_hsv(hsv):
    """Returns: String representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object."""
    
    h= str5(hsv.hue)
    s= str5(hsv.saturation)
    v= str5(hsv.value)
    
    
    return '('+str(h)+', '+str(s)+', '+str(v)+')'    # Stub


def rgb_to_cmyk(rgb):
    """Returns: color rgb in space CMYK, with the most black possible.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object"""
    # The RGB numbers are in the range 0..255.
    
    cmyk= colormodel.CMYK(0.0,0.0,0.0,0.0)
    c= 1-(rgb.red / 255.0)
    m= 1-(rgb.green / 255.0)
    y= 1-(rgb.blue / 255.0)
    
    if c == 1.0 and m == 1.0 and y== 1.0:
        cmyk= colormodel.CMYK(0.0,0.0,0.0,100.0)
       
       
    else:
        k= min(c, m, y)
        
        cmyk.cyan= (c-k)/(1-k)*100
        cmyk.magenta= (m-k)/(1-k)*100
        cmyk.yellow= (y-k)/(1-k)*100
        cmyk.black= k*100
        return cmyk
    # Change the RGB numbers to the range 0..1 by dividing them by 255.0.
     # Stub


def cmyk_to_rgb(cmyk):
    """Returns : color CMYK in space RGB.

    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object."""
    # The CMYK numbers are in the range 0.0..100.0.  Deal with them in the 
    # same way as the RGB numbers in rgb_to_cmyk()
    rgb= colormodel.RGB(0,0,0)
    
    c= cmyk.cyan/100.0
    m= cmyk.magenta/100.0
    y= cmyk.yellow/100.0
    k= cmyk.black/100.0
    
    rgb.red=int(round((1-c)*(1-k)*255,0))
    rgb.green= int(round((1-m)*(1-k)*255,0))
    rgb.blue= int(round((1-m)*(1-k)*255,0))
    
    return rgb  # Stub


def rgb_to_hsv(rgb):
    """Return: color rgb in HSV color space.

    Formulae from wikipedia.org/wiki/HSV_color_space.
   
    Parameter rgb: the color to convert to a HSV object
    Precondition: rgb is an RGB object"""
    # The RGB numbers are in the range 0..255.
    hsv= colormodel.HSV(0.0,0.0,0.0)
    r= (rgb.red)/255.0
    g= (rgb.green)/255.0
    b= (rgb.blue)/255.0
    
    big = max(r,g,b)
    small= min(r,g,b)
    
    if big==small:
        hsv.hue=0
    elif big== r and g>=b:
        hsv.hue=60.0*(g-b)/(big-small)
    elif big==r and g<b:
        hsv.hue=60.0*(g-b)/(big-small)+360.0
    elif big==g:
        hsv.hue=60.0*(b-r)/(big-small)+120.0
    elif big==b:
        hsv.hue=60.0*(r-g)/(big-small)+240.0
        
    if big==0:
        hsv.saturation=0
    else:
        hsv.saturation= 1-(small/big)
       
    hsv.value= big
    
    return hsv

    
    
    # Change them to range 0..1 by dividing them by 255.0.
     # Stub


def hsv_to_rgb(hsv):
    #add 6 cases
    """Returns: color in RGB color space.
    
    Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object."""
    rgb= colormodel.RGB(0,0,0)
    h= hsv.hue
    s= hsv.saturation
    v= hsv.value
    
   # r=rgb.red
    #g=rgb.green
    #b=rgb.blue
    
    
    hi= math.floor(h/60)
    f= (h/60)-hi
    p= v*(1-s)
    q= v*(1-(f*s))
    t= v*(1-(1-f)*s)
    
    if hi==0:
        r=v
        g=t
        b= p
    
    elif hi==1:
        r=q
        g=v
        b=p
        
    elif hi==2:
        r=p
        g=v
        b=t
        
    elif hi==3:
        r=p
        g=q
        b=v
        
    elif hi==4:
        r=t
        g=p
        b=v
    
    elif hi==5:
        r=v
        g=p
        b=q
    
    rgb.red= int(round(r*255,0))
    rgb.green= int(round(g*255,0))
    rgb.blue= int(round(b*255,0))
    
    

        
    return rgb  # Stub
