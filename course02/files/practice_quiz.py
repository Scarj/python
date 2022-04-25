#!/usr/bin/env python3
import datetime
import os.path


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        filesize = file.write(comments)
    return filesize


print(create_python_script("program.py"))


def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if not os.path.isdir(directory):
        os.mkdir(directory)

    # Create the new file inside of the new directory
    os.chdir(directory)
    with open(filename, "w") as file:
        pass

    # Return the list of files in the new directory
    return os.listdir(os.getcwd())


print(new_directory("PythonPrograms", "script.py"))

os.chdir("..")


def file_date(filename):
    # Create the file in the current directory
    with open(filename, "w") as file:
        pass

    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    modification_date = datetime.datetime.fromtimestamp(timestamp)
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return "{:.10}".format(str(modification_date))


# Should be today's date in the format of yyyy-mm-dd
print(file_date("newfile.txt"))


def parent_directory():
    # Create a relative path to the parent
    # of the current working directory
    relative_parent = os.path.join(os.getcwd(), "..")

    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)


print(parent_directory())
