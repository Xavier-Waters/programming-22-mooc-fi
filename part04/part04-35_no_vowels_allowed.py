# Write your solution here
def no_vowels(string):
	vowels = ["a", "e", "i", "o", "u"]
	list = []
	for x in range(len(vowels)):
	    if string.count(vowels[x]) >= 1:
	        list.append(vowels[x])
	for x in range(len(list)):
	    string = string.replace(list[x],"")
	return string
if __name__ == "__main__":
	string = "this is an example"
	print(no_vowels(string))
