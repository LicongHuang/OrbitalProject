#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include <fcntl.h>
#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#include <stdlib.h>

#include "i2c.h"
#include "lcd.h"

#define I2C_FILE_NAME "/dev/i2c-3"

const char* txt[]  = {
    "Next Input:"
};


void display_letter(char* txt, int pos){
    int i2c_dev;
    lcd lcd0;
    // 0x27 is the address of the i2c device
    i2c_dev = open_i2c(I2C_FILE_NAME, 0x27);
    if(i2c_dev <0){
       printf("Errore: %d\n", i2c_dev);
       return;
    }
    lcd_init(&lcd0, i2c_dev);
    //lcd_clear(&lcd0);
    lcd_print(&lcd0, txt, strlen(txt), pos);
    close_i2c(i2c_dev);
    return ;
}

int main(){
  lcd lcd0;
  lcd_clear(&lcd0);
  display_letter((char*) txt[0], 0);
  //display_letter((char*) txt[1], 1);
  return 0;

}

