# a3test.py
# Kore Ayoade (koa5)
# Thursday October 6th
""" Unit Test for Assignment A3"""

import colormodel
import cornelltest
import a3

def test_complement():
    """Test function complement"""
    cornelltest.assert_equals(colormodel.RGB(255-250, 255-0, 255-71),
                              a3.complement_rgb(colormodel.RGB(250, 0, 71)))


def test_round():
    """Test function round (a3 version)"""
    result= a3.round(130.59,1)
    
    cornelltest.assert_equals(130.6,  result)
    cornelltest.assert_equals(130.5,   a3.round(130.54,1))
    cornelltest.assert_equals(100.0,   a3.round(100,1))
    cornelltest.assert_equals(100.6,   a3.round(100.55,1))
    cornelltest.assert_equals(99.57,   a3.round(99.566,2))
    cornelltest.assert_equals(99.99,   a3.round(99.99,2))
    cornelltest.assert_equals(100.0,   a3.round(99.995,2))
    cornelltest.assert_equals(22.00,   a3.round(21.99575,2))
    cornelltest.assert_equals(21.99,   a3.round(21.994,2))
    cornelltest.assert_equals(10.01,   a3.round(10.013567,2))
    cornelltest.assert_equals(10.0,    a3.round(10.000000005,2))
    cornelltest.assert_equals(10.0,    a3.round(9.9999,3))
    cornelltest.assert_equals(9.999,   a3.round(9.9993,3))
    cornelltest.assert_equals(1.355,   a3.round(1.3546,3))
    cornelltest.assert_equals(1.354,   a3.round(1.3544,3))
    cornelltest.assert_equals(0.046,   a3.round(.0456,3))
    cornelltest.assert_equals(0.045,   a3.round(.0453,3))
    cornelltest.assert_equals(0.006,   a3.round(.0056,3))
    cornelltest.assert_equals(0.001,   a3.round(.0013,3))
    cornelltest.assert_equals(0.0,     a3.round(.0004,3))
    cornelltest.assert_equals(0.001,   a3.round(.0009999,3))
    
    cornelltest.assert_equals(130.57,  a3.round(130.566,2))
    cornelltest.assert_equals(12.45,  a3.round(12.453,2 ))
    cornelltest.assert_equals(100000.355,  a3.round(100000.3546,3))
    cornelltest.assert_equals(9999.999, a3.round(9999.9993,3))
    



def test_str5():
    """Test function str5"""
    cornelltest.assert_equals('130.6',  a3.str5(130.59))
    cornelltest.assert_equals('130.5',  a3.str5(130.54))
    cornelltest.assert_equals('100.0',  a3.str5(100))
    cornelltest.assert_equals('100.6',  a3.str5(100.55))
    cornelltest.assert_equals('99.57',  a3.str5(99.566))
    cornelltest.assert_equals('99.99',  a3.str5(99.99))
    cornelltest.assert_equals('100.0',  a3.str5(99.995))
    cornelltest.assert_equals('22.00',  a3.str5(21.99575))
    cornelltest.assert_equals('21.99',  a3.str5(21.994))
    cornelltest.assert_equals('10.01',  a3.str5(10.013567))
    cornelltest.assert_equals('10.00',  a3.str5(10.000000005))
    cornelltest.assert_equals('10.00',  a3.str5(9.9999))
    cornelltest.assert_equals('9.999',  a3.str5(9.9993))
    cornelltest.assert_equals('1.355',  a3.str5(1.3546))
    cornelltest.assert_equals('1.354',  a3.str5(1.3544))
    cornelltest.assert_equals('0.046',  a3.str5(.0456))
    cornelltest.assert_equals('0.045',  a3.str5(.0453))
    cornelltest.assert_equals('0.006',  a3.str5(.0056))
    cornelltest.assert_equals('0.001',  a3.str5(.0013))
    cornelltest.assert_equals('0.000',  a3.str5(.0004))
    cornelltest.assert_equals('0.001',  a3.str5(.0009999))
    
    cornelltest.assert_equals('900.0',  a3.str5(900))
    cornelltest.assert_equals('12.45',  a3.str5(12.453))
    cornelltest.assert_equals('0.000',  a3.str5(.0003))
    cornelltest.assert_equals('0.001', a3.str5(0.00099999))


def test_str5_color():
    """Test the str5 functions for cmyk and hsv."""
    cornelltest.assert_equals('(98.45, 25.36, 99.99, 21.99)',\
            a3.str5_cmyk(colormodel.CMYK(98.448, 25.362, 99.99, 21.994)));
    
    cornelltest.assert_equals('(32.33, 6.355, 0.001, 10.01)',\
    a3.str5_cmyk(colormodel.CMYK(32.3256, 6.3546, .0013, 10.013567)))
    
    
    # Tests for round5_hsv (add two)


def test_rgb_to_cmyk():
    """Test rgb_to_cmyk"""
    rgb = colormodel.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.black))
    
    
    rgb = colormodel.RGB(0, 0,0);
    cmyk = a3.rgb_to_cmyk(rgb);
    
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('100.0', a3.str5(cmyk.black))
        
    rgb = colormodel.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('80.18', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('24.42', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('14.90', a3.str5(cmyk.black))
    
    


def test_cmyk_to_rgb():
    """Test translation function cmyk_to_rgb"""
    cmyk= colormodel.CMYK(100.0, 100.0, 100.0, 100.0);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals( 0, rgb.red)
    cornelltest.assert_equals( 0, rgb.green)
    cornelltest.assert_equals( 0, rgb.blue)
    
    cmyk= colormodel.CMYK(0.000, 000.0, 000.0, 000.0);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals( 255, rgb.red)
    cornelltest.assert_equals( 255, rgb.green)
    cornelltest.assert_equals( 255, rgb.blue)
    
    cmyk= colormodel.CMYK(50.00, 50.00, 50.00, 50.00);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals( 63, rgb.red)
    cornelltest.assert_equals( 63, rgb.green)
    cornelltest.assert_equals( 63, rgb.blue)
    
    
    
     


def test_rgb_to_hsv():
    """Test translation function rgb_to_hsv"""
    rgb= colormodel.RGB(20,20,20)
    hsv= a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals( '0.000', a3.str5(hsv.hue))
    
    
    rgb= colormodel.RGB(100,25,20)
    hsv= a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals( '3.750', a3.str5(hsv.hue))
    cornelltest.assert_equals( '0.800', a3.str5(hsv.saturation))
    cornelltest.assert_equals( '0.392', a3.str5(hsv.value))
    
    rgb= colormodel.RGB(200,50,100)
    hsv= a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals( '340.0', a3.str5(hsv.hue))
    cornelltest.assert_equals( '0.750', a3.str5(hsv.saturation))
    cornelltest.assert_equals( '0.784', a3.str5(hsv.value))
    
   
    
    rgb= colormodel.RGB(20,100,20)
    hsv= a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals( '120.0', a3.str5(hsv.hue))
    cornelltest.assert_equals( '0.800', a3.str5(hsv.saturation))
    cornelltest.assert_equals( '0.392', a3.str5(hsv.value))
    
    rgb= colormodel.RGB(20,20,100)
    hsv= a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals( '240.0', a3.str5(hsv.hue))
    cornelltest.assert_equals( '0.800', a3.str5(hsv.saturation))
    cornelltest.assert_equals( '0.392', a3.str5(hsv.value))
    
    rgb= colormodel.RGB(0,0,0)
    hsv= a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals( '0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals( '0.000', a3.str5(hsv.saturation))
    cornelltest.assert_equals( '0.000', a3.str5(hsv.value))
    
    rgb= colormodel.RGB(20,25,25)
    hsv= a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals( '180.0', a3.str5(hsv.hue))
    cornelltest.assert_equals( '0.200', a3.str5(hsv.saturation))
    cornelltest.assert_equals( '0.098', a3.str5(hsv.value))
    
    



def test_hsv_to_rgb():
    """Test translation function hsv_to_rgb"""
    
    hsv= colormodel.HSV(20.00,1.000,1.000)
    rgb= a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals( 255, rgb.red)
    cornelltest.assert_equals(84, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)
    
    hsv= colormodel.HSV(60.00,1.000,1.000)
    rgb= a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals( 255, rgb.red)
    cornelltest.assert_equals(255, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)
    
    hsv= colormodel.HSV(120.00,1.000,1.000)
    rgb= a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals( 0, rgb.red)
    cornelltest.assert_equals(255, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)
    
    hsv= colormodel.HSV(180.00,1.000,1.000)
    rgb= a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals( 0, rgb.red)
    cornelltest.assert_equals(255, rgb.green)
    cornelltest.assert_equals(255, rgb.blue)
    
    hsv= colormodel.HSV(240.00,1.000,1.000)
    rgb= a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals( 0, rgb.red)
    cornelltest.assert_equals(0, rgb.green)
    cornelltest.assert_equals(255, rgb.blue)
    
    hsv= colormodel.HSV(300.00,1.000,1.000)
    rgb= a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals( 255, rgb.red)
    cornelltest.assert_equals(0, rgb.green)
    cornelltest.assert_equals(255, rgb.blue)
    
    
    
   


# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == "__main__":
    test_complement()
    test_round()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    print "Module a3 is working correctly"
