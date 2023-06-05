#Write a Python function calles is_palindrome that checks if a given word is a palindrome.
#THe function should have proper error handling and be tested with unittest.
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True

print(isPalindrome('arroz')) 
print(isPalindrome('abracadabra'))
print(isPalindrome('nun'))
print(isPalindrome('mom'))