# Log Parsing
This directory contains a python script solving the log parsing problem described below.

## Tasks To Complete
+ [x] **0. Log Parsing**

[0-stats.py](https://github.com/kal-kyokya/alx-interview/tree/main/0x03-log_parsing) contains a script that reads "stdin" line by line and computes metrics.

* Input format:
	* 'IP_Address' - 'date' "GET /projects/260 HTTP/1.1" 'status_code' 'file_size'
	* if the format is not this one, the line must be skipped
* After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
	* Total file size:
		* "File size: 'total_size'"
		* where 'total_size' is the sum of all previous 'file_size' (see input format above)
	* Number of lines by status code:
		* possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
		* if a status code doesn’t appear or is not an integer, don’t print anything for this status code
		* format:
			* 'status_code': 'number'
		* status codes should be printed in ascending order

```
kal-kyokya@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
```
Results:
```
kal-kyokya@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./0-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
kal-kyokya@ubuntu:~/0x03-log_parsing$
```

---

For the “0x03. Log Parsing” project, one will need to apply knowledge of Python programming, focusing on parsing and processing data streams in real-time.
This project involves:
	* Reading from standard input (stdin),
	* Handling data in a specific format,
	* Performing calculations based on the input data.

## Concepts Needed:

### File I/O in Python:
* Understand how to read from sys.stdin line by line.

### Signal Handling in Python:
* Handling keyboard interruption (CTRL + C) using signal handling in Python.

### Data Processing:
* Parsing strings to extract specific data points.
* Aggregating data to compute summaries.

### Regular Expressions:
* Using regular expressions to validate the format of each line.

### Dictionaries in Python:
* Using dictionaries to count occurrences of status codes and accumulate file sizes.

### Exception Handling:
* Handling possible exceptions that may arise during file reading and data processing.

By studying these concepts, one will be well-prepared to tackle the log parsing project, effectively handling:
* Data streams,
* Parsing log entries,
* Computing metrics based on the processed data.
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
-   Directory: `0x03-log_parsing`
-   File: `0-minoperations.py`
