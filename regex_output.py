## https://docs.python.org/3.6/howto/regex.html

## metacharacters: . ^ $ * + ? { } [ ] \ | ( )
##  [] : character class; metacharacters are ususally inactive in character class.
##	^ : complement the set when appearing as the 1st character of the class
##  \ : cancel metacharacters' special meaning; combined with special sequences
## 		\w : alphanumeric; equals [a-zA-Z0-9_]
##      \W : non-alphanumeric; equals [^a-zA-Z0-9_]
## 		\d : decimal digit; equals [0-9]
##      \D : non-digit; equals [^0-9]
##		\s : whitespace; equals [ \t\n\r\f\v]
## 		\S : nonwhitespace; equals [^ \t\n\r\f\v]
##  . : match any character except a new line
##  $ : match the end of line, which is defined by end of string or any location followed by a newline character
##  | : or

## repeatings
##  * : matched 0 or more times; "ca*t" match "ct" (0 "a" character); equals {0,}
##  + : matched 1 or more times; "ca+t" won't match "ct" but "cat" (1 "a" character); equals {1,}
##  ? : matched either 0 or 1 time (think of it marking sth. optional); equals {0,1}; "home-?brew" matches either "homebrew" or "home-brew"
##  {m,n} : matched at least m and at most n times, with m and n can be omitted, which means m=0, n=infinity; "a/{1,3}b" matches "a/b", "a//b", "a////b", and not "ab" or "a////b"



import re
p0 = re.compile("ca*t")
r0 = p0.findall("dctcatcaat")
print(r0)

p1 = re.compile("[\D]*where*[\d]*")
r10 = p1.match("where012")
r11 = p1.match("1where")
r12 = p1.match("111where12")
print(r10.group() if r10 is not None else r10)
print(r11.group() if r11 is not None else r11)
print(r12.group() if r12 is not None else r12)

## 有一个txt文件，找出里面“where”出现的次数，“where012”是有效的，“1where”是无效的
def sum_valid(s):
	l_str = s.split()
	result = sum([1 if p1.match(s) is not None else 0 for s in l_str])
	return result

print(sum_valid("123 where012 hello 123where"))
print(sum_valid("123 1where hello world"))
print(sum_valid("234 111where12 hello"))


p2 = re.compile("}$")
r20 = p2.findall("{block}")
r21 = p2.findall("{block} ")
r22 = p2.findall("{block}\n")
print(r20) # ['}']
print(r21) # []
print(r22) # ['}']

## detect double words in a string
p3 = re.compile(r'(\b\w+)\s+\1')
r30 = p3.findall('Paris in the the spring')
print(r30)

p4 = re.compile("where|hello")
r40 = p4.findall("where123")
r41 = p4.findall("hellowhere")
print(r40)
print(r41)


## the string start with exactly 2 vowels
def contains_two_vow(s):
	#### Method 1: break into 3 steps
	## first two elements are vowels
	p1 = "[aeiou]{2}.*"
	prog1 = re.compile(p1)

	## third element is a nonvowel
	p2 = ".{2}[^aeiou]+"
	prog2 = re.compile(p2)

	## third element is empty
	p3 = ".{2}$"
	prog3 = re.compile(p3)

	# result = True if prog1.match(s) else False
	# result = True if prog2.match(s) else False
	# result = True if prog3.match(s) else False

	## first two elements are vowels and 3rd element is either a nonvowel, or empty
	# if(prog1.match(s) and (prog2.match(s) or prog3.match(s))):
	# 	result = True
	# else:
	# 	result = False

	#### Method 2: combine them into one pattern 
	p = "[aeiou]{2}([^aeiou]+|$)"
	prog = re.compile(p)

	result = True if prog.match(s) else False

	return result
#### test cases
## correct
s1 = "aerrr"
s2 = "aerer" 
s3 = "ae"

## incorrect
s4 = "aeere" 
s5 = "raere"
s6 = "rarre"

## test p1: first two are vowels
# print(contains_two_vow(s1)==True)
# print(contains_two_vow(s2)==True)
# print(contains_two_vow(s3)==True)
# print(contains_two_vow(s4)==True)
# print(contains_two_vow(s5)==False)
# print(contains_two_vow(s6)==False)

## test p2: third element either empty or nonvowel
# print(contains_two_vow(s1)==True)
# print(contains_two_vow(s2)==True)
# print(contains_two_vow(s3)==True)
# print(contains_two_vow(s4)==False)
# print(contains_two_vow(s5)==False)
# print(contains_two_vow(s6)==True)

## test p3: only two letters being vowels
# print(contains_two_vow(s1)==False)
# print(contains_two_vow(s2)==False)
# print(contains_two_vow(s3)==True)
# print(contains_two_vow(s4)==False)
# print(contains_two_vow(s5)==False)
# print(contains_two_vow(s6)==False)


## test goal
print(contains_two_vow(s1)==True)
print(contains_two_vow(s2)==True)
print(contains_two_vow(s3)==True)
print(contains_two_vow(s4)==False)
print(contains_two_vow(s5)==False)
print(contains_two_vow(s6)==False)

############ old notes ############  
# Regular expression summary

# \d 			Decimal digit, 0-9.
# \D 			Matches any non-digit character.
# \w 			Matches a sinlge 'word' char: a letter or digit or underscore.
# \W 			Matches any non-word char.
# \b 			Matches boundary btw word \w and non-word \W chars.
# 			r'py\b' matches 'py', 'py.', or 'py!'
# 			but not 'python', 'py3', 'py2'
# \B 			Matches NOT at beginning or end of a word. 
# 			r'py\B' matches 'python', 'py3', 'py2'
# 			but not 'py', 'py.', 'py!'
# \s 			matches whitespace 'Pine\sapple'
# 				Yes: pine apple
# 				No: Pineapple
# \S 			matches non-whitespace 'Pine\Sapple'
# 				Yes: Pineapple
# 				No: Pine pple

# Wildcards 
# * 			zero or more of the previous item
# + 			one or more of the previous item
# ? 			zero or one of the previous item
# -
# !
# {3} 		matches exactly 3 of the previous item
# {3,6}  		matches btw 3 and 6 of the previous item
# {3,} 		matches 3 or more of the previous item
# []

# ab* 		will match 'a', 'ab', or 'a' followed by any number of 'b's
# ab+ 		will match 'a' followed by at least one 'b'; will not match just 'a'
# ab? 		will match either 'a' or 'ab'

# Single-character regular expression
# ^ 			Beginning of the line  '^From: '
# 				Yes: From: Kevyn 
# 				No: It said, 'From:...'
# $ 			End of the line (just before newline) 'Michigan$'
# 				Yes: Michigan\n
# 				No: Michigan, U.S.A.\n
# . 			Matches any char except newline \n 'F..m:'
# 				Yes: Farm:
# 				Yes: Foom:
# 				No: Firm.			
# % 			
# <

# .* 		greedy 			101000000000100----1.*1---->1010000000001
# .*?		non-greedy		101000000000100-----1.*?1-->101

# (?<!...)		Matches if the current position in the string is not preceded by a match for .... This is called a negative lookbehind assertion. Similar to positive lookbehind assertions, the contained pattern must only match strings of some fixed length and shouldn’t contain group references. Patterns which start with negative lookbehind assertions may match at the beginning of the string being searched.
