# Thumb Defendor

This is an Orbital 2023 project by Licong and Yan Xu.

This project is a hardware centric project that encrypts a usb drive

It has hardware and software aspects to the project


<h1>Milestone 1:</h1>

<h2>Software</h2>

<h3>In Docker</h3>

----------

 - [X] Generate random bits to be used as encryption key
 - [X] Store and use key in database
 - [X] Encrypt and Decrypt file 

To test the software:
Prerequiste : Have docker installed
```
cd ./software/todo-app/
./script.sh

```
This would create a docker container, once inside the container:
```
./startupscript.sh
```

The above command generates a python virtual environment and run the encryption and decryption on test files in `usb_test`, run:
``` bash
./test -e #to encrypt usb_test
./test -d # to decrypt usb_test
```


<h1>Milestone 2:</h1>
