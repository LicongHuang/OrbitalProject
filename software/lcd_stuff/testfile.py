import lcd_display as lcd
import time

def first():
    num = [1,2,3]
    for x in num:
        lcd.auth_fail()
        time.sleep(3)
        lcd.auth_display()
        time.sleep(3)
        lcd.de_com()
        time.sleep(3)
        lcd.en_com()
        time.sleep(3)
        lcd.en_or_de()
        time.sleep(3)
        lcd.exit_c()
        time.sleep(3)
        lcd.invalid_in()
        time.sleep(3)
        lcd.next_in()
        time.sleep(3)
        lcd.empty_screen()
        time.sleep(3)
        lcd.loading()
        time.sleep(3)
        lcd.insertpass()
        time.sleep(3)

def sec():
    num = [1,2,3]
    for x in num:
        lcd.auth_fail()
        #time.sleep(3)
        lcd.auth_display()
        #time.sleep(3)
        lcd.de_com()
        #time.sleep(3)
        lcd.en_com()
        #time.sleep(3)
        lcd.en_or_de()
        #time.sleep(3)
        lcd.exit_c()
        #time.sleep(3)
        lcd.invalid_in()
        #time.sleep(3)
        lcd.next_in()
        #time.sleep(3)
        lcd.empty_screen()

def main():
    first()
    #sec()

if __name__ == "__main__":
    main()
