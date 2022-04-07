import I2C_LCD_driver
from time import *

def display():
    mylcd = I2C_LCD_driver.lcd()
    mylcd.lcd_display_string("ANOMALI!!", 1)
    sleep(10)
    mylcd.lcd_display_string("---------", 1)
    print("basarili")