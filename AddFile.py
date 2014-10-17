from tkFileDialog import *
import hashlib
import tkMessageBox
import os

# to check for the presence of a file to avoid duplicates
def checkFile(testHash):
	with open('workfile', 'r') as f:
		for name, sig in testHash.items():
			for line in f:
				line = line.strip("\n")
				a,b = line.split(" : ")
				if sig == b:
					f.close()
					return True				
	f.close()
	return False

# to add files to a list from which to check against for matches
def addFile():
	
	# dictionary to store the hashes and file names from the test files
	testHash = dict()
	# open the file chooser dialogue and store chosen file and filepath
	fileName = askopenfilename()
	# reset the hasher to ensure matches for identical files
	hasher = hashlib.md5()

	# get the file, hash it and store both in dictionary
	with open(fileName, 'rb') as afile:
		buf = afile.read()
		hasher.update(buf)
		testHash[fileName]=hasher.hexdigest()
		print (testHash)
		afile.close()

	if not (checkFile(testHash)):
		#write both the the file name/path and the resulting hash to a text file
		with open('workfile', 'a') as f:
			for name, sig in testHash.items():
				f.write(name + " : " + sig + "\n")
			f.close()
			name=name.split("/")
			tkMessageBox.showinfo("File Adder", "File : " + name[-1] + " - added")
	else:
		tkMessageBox.showinfo("File Adder", "File already exists")

# to remove files from the list
def delFile():
	
	# dictionary to store the hashes and file names from the test files
	testHash = dict()
	# open the file chooser dialogue
	fileName = askopenfilename()
	# reset the hasher to ensure matches for identical files
	hasher = hashlib.md5()

	# get the file, hash it and store both in dictionary
	with open(fileName, 'rb') as afile:
		buf = afile.read()
		hasher.update(buf)
		testHash[fileName]=hasher.hexdigest()
		afile.close()

	if (checkFile(testHash)):
		#remove both the the file name/path and the resulting hash from the text file
		result = tkMessageBox.askquestion("Delete", "Are You Sure You Want\nTo Remove This File?", icon='warning')
		if result == 'yes':
			with open("workfile") as f:
			    with open("temp", "w") as f1:
				for line in f:
					for name, sig in testHash.items():
					    if not sig in line:
						f1.write(line)			
			tkMessageBox.showinfo("File Delete", "File Deleted")
			try:
				os.remove("workfile")
				os.renames("temp", "workfile")
			except OSError, e:  ## if failed, report it back to the user ##
				print ("Error: %s - %s." % (e.filename,e.strerror))
			
	else:
		tkMessageBox.showinfo("File Adder", "File does not exist!")
