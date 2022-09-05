# Write your solution here
while True:
	editor = str(input("Editor: "))
	if editor.lower() == "emacs" or editor.lower() == "vim" or editor.lower() == "atom":
	    print("not good")
	elif editor.lower() == "word" or editor.lower() == "notepad":
	    print("awful")
	elif editor.lower() == "visual studio code":
	    print("an excellent choice!")
	    break
