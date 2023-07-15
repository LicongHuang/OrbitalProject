//Copyright (c) 2014, Giovanni Dante Grazioli (deroad)
#include <stdio.h>
#include <unistd.h>
#include <assert.h>
#include <linux/i2c-dev.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/ioctl.h>
#include <string.h>

#include "lcd.h"
#include "i2c.h"

void lcd_notify(lcd* l){
    assert(l);
    u8 v;
    get_i2c_data(l->dev, &v);
    set_i2c_data(l->dev, (v | 0x04) | 0x08);
    get_i2c_data(l->dev, &v);
    set_i2c_data(l->dev, (v & 0xFB) | 0x08);
}

void lcd_cmd(lcd* l, u8 cmd){
    assert(l);
    set_i2c_data(l->dev, (cmd & 0xF0)   | 0x08);
    lcd_notify(l);
    set_i2c_data(l->dev, (cmd & 0x0F)<<4| 0x08);
    lcd_notify(l);
    set_i2c_data(l->dev, 0x0 | 0x08);
}

void lcd_init(lcd* l, int dev){
    assert(l && dev > 0);
    l->dev = dev;
    l->dim = 0;
    set_i2c_data(l->dev, 0x30 | 0x08); // enable 8 bit mode
    lcd_notify(l);
    usleep(3);
    set_i2c_data(l->dev, 0x20 | 0x08); // enable 4 bit mode
    lcd_notify(l);
    usleep(3);
    lcd_notify(l);
    usleep(3);

    lcd_cmd(l, 0x28);
    lcd_cmd(l, 0x08);
    lcd_cmd(l, 0x01);
    lcd_cmd(l, 0x06);
    lcd_cmd(l, 0x0C);
    lcd_cmd(l, 0x0F);
}

void lcd_backlight(lcd* l){
    lcd_notify(l);
}

void lcd_putc(lcd* l, u8 c){
    assert(l);
    set_i2c_data(l->dev, 0x01 | (c & 0xF0)   | 0x08);
    lcd_notify(l);
    set_i2c_data(l->dev, 0x01 | (c & 0x0F)<<4| 0x08);
    lcd_notify(l);
    set_i2c_data(l->dev, 0x0 | 0x08);
}

void lcd_print(lcd* l, const char* t, u8 len, u8 line){
    assert(l && t && line < 4);
    u8 i;
	u8 rows[] = {0x00, 0x40, 0x14, 0x54};
    lcd_cmd(l, 0x80 | rows[line]);
    for(i=0; i<len; ++i)
        lcd_putc(l, t[i]);
    lcd_cmd(l, 0xC);
}

void lcd_clear(lcd* l){
    assert(l);
    lcd_cmd(l, 0x1);
    lcd_cmd(l, 0x2);
}

void lcd_set_cursor(lcd* l, u8 col, u8 row){
    assert(l && row < 4);
    u8 rows[] = {0x00, 0x40, 0x14, 0x54};
    lcd_cmd(l, 0x80 | (col + rows[row]));
}

void lcd_add_char(lcd* l, const unsigned char font[8], u8 position){
    u8 j;
    lcd_cmd(l, 0x40 | ((position & 7) << 3));
    for(j=0; j<8; ++j)
      lcd_putc(l, font[j]);
}


int open_i2c(const char* dev_path, unsigned char addr) {
    int dev;
    dev = open(dev_path, O_RDWR);

    ioctl(dev, I2C_SLAVE, addr & 0x7F);
    return dev;
}

void close_i2c(int dev) {
    close(dev);
}

int get_i2c_data(int dev, unsigned char *value) {
    int r;
    if((r = read(dev, value, 1))<0 ){
        printf("Failed to read from the i2c bus %d\n", r);
        return 1;
    }
    return 0;
}

int set_i2c_data(int dev, unsigned char val) {
    int r;
    unsigned char buf[2];
    buf[1] = 0;
    buf[0] = val;
    if((r = write(dev, buf, 1))<0 ){
        printf("Failed to write from the i2c bus %d\n", r);
        return 1;
    }
    usleep(2);
    return 0;
}

void display_lcd(char* text){
    lcd l;
    int dev = open_i2c("/dev/i2c-3", 0x27);
    if (dev < 0) {
        printf("Error: Couldn't open device! %d\n", dev);
        exit (1);
    }
    lcd_init(&l, dev);
    lcd_clear(&l);
    lcd_print(&l, text, strlen(text), 0);
    close_i2c(dev);
}
