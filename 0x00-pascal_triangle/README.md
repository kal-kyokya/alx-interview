# Pascal's Triangle
This directory contains python scripts created during resolution of the Pascal's triangle task.

## Tasks To Complete
+ [x] **0. Pascal's Triangle**

[0-pascal_triangle.py](https://github.com/kal-kyokya/alx-interview/tree/main/0x00-pascal_triangle) contains a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal's triangle of `n`:

* It returns an empty list if `n <= 0`.
* Works with the assumption that `n` will be always an integer.

```
kal-kyokya@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

kal-kyokya@ubuntu:~/0x00$ 
kal-kyokya@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
kal-kyokya@ubuntu:~/0x00$ 
```

---

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x00-pascal_triangle`
-   File: `0-pascal_triangle.py`
