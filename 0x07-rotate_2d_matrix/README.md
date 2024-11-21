# Rotate 2D Matrix

This directory contains a Python script enabling completion of the 'Rotate 2D Matrix' project described below.

## Tasks To Complete
+ [x] **0. Rotate 2D Matrix**

[0-rotate_2d_matrix.py](https://github.com/kal-kyokya/alx-interview/tree/main/0x07-rotate_2d_matrix) will: given an n x n 2D matrix, rotate it 90 degrees clockwise.

* Prototype: ```def rotate_2d_matrix(matrix):```
* This will not return anything. The matrix will be edited in-place.
* One can assume the matrix will have 2 dimensions and will not be empty.

```
kal-kyokya$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

kal-kyokya$
```
Result:
```
kal-kyokya$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
kal-kyokya$
```

---

For the “0. Rotate 2D Matrix” project, one is tasked with implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python. Below are the key concepts that one needs to grasp in order to successfully complete this project.

## Concepts Needed:

### Matrix Representation in Python:
* Understanding how 2D matrices are represented using lists of lists in Python.
* Accessing and modifying elements in a 2D matrix.

### In-place Operations:
* Performing operations on data without creating a copy of the data structure.
* The importance of minimizing space complexity by modifying the matrix in place.

### Matrix Transposition:
* Understanding the concept of transposing a matrix (swapping rows and columns).
* Implementing matrix transposition as a step in the rotation process.

### Reversing Rows in a Matrix:
* Manipulating rows of a matrix by reversing their order as part of the rotation process.

### Nested Loops:
* Using nested loops to iterate through 2D data structures like matrices.
* Modifying elements within nested loops to achieve the desired rotation.

By understanding these concepts, one will be able to approach the problem methodically:
* First transposing the matrix
* And then reversing each row to achieve a 90-degree clockwise rotation.
This project not only tests ones ability to manipulate 2D matrices but also challenges one to think about optimizing ones solution to operate in-place, thus improving their problem-solving and algorithmic thinking skills in Python.

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
	->	All code should use:
			* The 'pycodestyle' style (version 2.8.0)
	->	One is not allowed to import any module
	->	All modules and functions must be documented
	->	All files must be executable

---

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x07-rotate_2d_matrix`
-   File: `0-rotate_2d_matrix.py`
