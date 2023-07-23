#!/bin/sh
import os

def auth_fail():
    os.system("/home/orangepi/OrbitalProject/software/lcd_stuff/auth_fail")

def auth_display():
    os.system('/home/orangepi/OrbitalProject/software/lcd_stuff/auth_display')

def de_com():
    os.system("/home/orangepi/OrbitalProject/software/lcd_stuff/de_complete")

def en_com():    
    os.system("/home/orangepi/OrbitalProject/software/lcd_stuff/en_complete")
def en_or_de():
    os.system("/home/orangepi/OrbitalProject/software/lcd_stuff/en_or_de")

def exit_c():
    os.system("/home/orangepi/OrbitalProject/software/lcd_stuff/exit_c")

def invalid_in():
    os.system("/home/orangepi/OrbitalProject/software/lcd_stuff/invalid_in")

def next_in():
    os.system("/home/orangepi/OrbitalProject/software/lcd_stuff/next_in")

def empty_screen():
    os.system("/home/orangepi/OrbitalProject/software/lcd_stuff/empty_screen")

def loading():
    os.system("/home/orangepi/OrbitalProject/software/lcd_stuff/loading")

def insertpass():
    os.system("/home/orangepi/OrbitalProject/software/lcd_stuff/insertpass")

if __name__ == "__main__":
    auth_fail()
    auth_display()
    de_com()
    en_com()
    en_or_de()
    exit_c()
    invalid_in()
    next_in()
    empty_screen()
    loading()



