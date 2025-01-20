# MapReduce - Mapper
# Eshita Gupta - DATA228 - Assignment 2
import sys
"""
Read input from STDIN, cleanup and print each word independently followed by tab character
"""
# Read the content from STDIN
sentence = ""
for line in sys.stdin:
    sentence += line

# Remove punctuation and convert text to lowercase
sen = sentence.replace('.','').replace(',','').replace("'",'').replace("[",'').replace("]",'')
s_list = sen.strip().lower().split()

# Print each word with a tab character for Reducer job
for i in s_list:
    print(f"{i}\t")

