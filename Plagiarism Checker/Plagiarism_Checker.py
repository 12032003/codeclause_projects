# Plagiarism Checker in python

def check_plagiarism(file1, file2):
    # Read the contents of file1
    with open(file1, 'r') as f1:
        content1 = f1.read()

    # Read the contents of file2
    with open(file2, 'r') as f2:
        content2 = f2.read()

    # Compare the contents of file1 and file2
    if content1 == content2:
        print("\n The files are identical. No plagiarism detected. \n")
    else:
        print("\n The files are different. Plagiarism detected. \n")

# Example usage
check_plagiarism("file1.txt", "file2.txt")
