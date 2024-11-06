# UTF-8 Validation

This directory contains a python script solving the UTF-8 Validation problem described below.

## Tasks To Complete
+ [x] **0. UTF-8 Validation**

[0-validate_utf8.py](https://github.com/kal-kyokya/alx-interview/tree/main/0x04-utf8_validation) contains a script that determines if a given data set represents a valid UTF-8 encoding.

* Prototype: ```def validUTF8(data)```
* Return: ```True``` if data is a valid UTF-8 encoding, else return ```False```
* A character in UTF-8 can be 1 to 4 bytes long
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents 1 byte of data, therefore one only need to handle the 8 least significant bits of each integer

```
kal-kyokya@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

kal-kyokya@ubuntu:~/0x04-utf8_validation$
```
Results:
```
kal-kyokya@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
kal-kyokya@ubuntu:~/0x04-utf8_validation$
```

---

For the “0x04. UTF-8 Validation” project, one will need to apply ones knowledge in bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding. Here’s a list of concepts:

## Concepts Needed:

### Bitwise Operations in Python:
* Understanding how to manipulate bits in Python, including operations like AND (&), OR (|), XOR (^), NOT (~), shifts (<<, >>).

## UTF-8 Encoding Scheme:
* Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
* Understanding the patterns that represent a valid UTF-8 encoded character.

## Data Representation:
* How to represent and work with data at the byte level.
* Handling the least significant bits (LSB) of integers to simulate byte data.

## List Manipulation in Python:
* Iterating through lists, accessing list elements, and understanding list comprehensions.

## Boolean Logic:
* Applying logical operations to make decisions within the program.

By studying these concepts, one will be equipped to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

---

## Requirements
### General

	->	Allowed editors:
			* vi,
			* vim,
			* emacs
	->	All files will be interpreted/compiled on:
			* Ubuntu 20.04 LTS
				using:
					* python3 (version 3.4.3)
	->	All files should end with a new line
	->	The first line of all files should be exactly:
			* #!/usr/bin/python3
	->	A README.md file, at the root of the folder of the project, is mandatory
	->	All code should be documented
	->	All code should use:
			* The PEP 8 style (version 1.7.x)
	->	All files must be executable

---

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x04-utf8_validation`
-   File: `0-validate_utf8.py`
