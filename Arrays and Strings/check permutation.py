#Given two strings, write a method to decide if one is a permutation of the other.

def permutation(a,b):
	return set(a) == set(b)

def main():
	print(permutation('John Doe','Doe John'))
	print(permutation('John Doe','Kartoon'))
	print(permutation('abbcdd','abb'))
	print(permutation('abbcdd','xyz'))
	print(permutation("abcdefgh","abcdefhg"))

		       
if __name__ == '__main__':
		main()	