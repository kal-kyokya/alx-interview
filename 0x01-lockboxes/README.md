# Lockboxes
This directory contains a python script that solves the Locked boxes problem described below.

## Tasks To Complete
+ [x] **0. Lockboxes**

[0-lockboxes.py](https://github.com/kal-kyokya/alx-interview/tree/main/0x01-lockboxes) contains a function `def canUnlockAll(boxes):` that returns 'True' if all boxes can be opened, 'False' otherwise when:

n number of locked boxes are presented. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

* 'boxes' is a list of lists
* A key with the same number as a box opens that box
* It can be assumed that all keys will be positive integers
* There can be keys that do not have boxes
* The first box boxes[0] is unlocked

```
kal-kyokya@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
kal-kyokya@ubuntu:~/0x01-lockboxes$
```
Results:
```
kal-kyokya@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
kal-kyokya@ubuntu:~/0x01-lockboxes$
```

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
-   Directory: `0x00-lockboxes`
-   File: `0-lockboxes.py`
