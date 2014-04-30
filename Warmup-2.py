# Warmup-2 Codingbat.com pyhton solutions
# Brian Martin 14/04/2014

# Given a string and a non-negative int n, 
# return a larger string that is n copies of the original string.

def string_times(str, n):
  result =""
  for i in range (n):
   result+=str
  return 
  sample change
  


# Given a string and a non-negative int n, we'll say that the front of the
#  string is the first 3 chars, or whatever is there if the 
#  string is less than length 3. Return n copies of the front;

def front_times(str, n):
 if len(str)<3:
   front = str
 else:
  front = str[:3]
 result = ""
 for i in range (n):
   result+= front
 # return result

 # Given a string, return a new string made of every other char starting
 #  with the first, so "Hello" yields "Hlo". 

 def string_bits(str):
  result = ""
  for i in range(len(str)):
   if i % 2 == 0:
    result = result + str[i]
  return result

# Given a non-empty string like "Code" return a string like "CCoCodCode". 

def string_splosion(str):
 result = ""
 for i in range(len(str)):
   result +=  str[:i+1]
 return result

# Given an array of ints, return the number of 9's in the array. 

def array_count9(nums):
  count =0
  for i in range(len(nums)):
    if nums[i]==9:
     count =count+1
  return count

  # Given an array of ints, return True if one of the first 4 elements in
  #  the array is a 9. The array length may be less than 4. 

  def array_front9(nums):
 end = len(nums)
 if end >4:
   end =4
 for num in range(end):
    if nums[num]==9:
     return True
 return False


# Given an array of ints, return True if .. 1, 2, 3, .. 
# appears in the array somewhere. 

def array123(nums):
 for i in range (len(nums)-2):
  if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
   return True
 return False
 

# Given 2 strings, a and b, return the number of the positions where they contain
#  the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, 
#  since the "xx", "aa", and "az" substrings appear 
#  in the same place in both strings. 