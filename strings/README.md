### Problem 1: Given two strings that represent two integers. e.g: "1232" and "201" Write a function that compares the two strings as numbers. Write a function larger_than(string1, string2): it returns true if the first arg is larger than the second arg, else false

Clarifying questions: Could the string be empty?
ans: No, assume they are never empty

Could the numbers be negative?
ans: always positive

Can I use int(str) to convert the string to numbers
ans: try to compare without converting with int(str)
You can use "3" > "2" comparison. Char comparisons
return true for larger numbers

What if they are the same number?
Then, the larger_than("22","22") should return False
