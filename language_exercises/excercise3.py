#3. Write a function that counts the lines of a file. The file name is provided as a function argument. It returns the number of lines in the file.

def counter_line(file_name):
	reading = open(file_name, "rb")
	i = 0
	for line in reading:	
		i += 1
	print i

counter_line("test.txt")