# MapReduce - Reducer
# Eshita Gupta - DATA228 - Assignment 2
import sys

# Create Empty Dictionaries
dict_avg = {}
dict1 = {}

"""
Read each line from STDIN and strip any trailing or leading blank characters
"""
for line in sys.stdin:
    line = line.strip()
    # Create key value pairs by using Key as the first character in a word and adding the word as a value. This will loop through
    # all the words and keep on adding new values to existing alphabet keys if they already exist
    # otherwise it will create a new key and add the values accordingly
    if line[0] in dict1:
        dict1[line[0]] += ',' + line 
    else:
        dict1[line[0]] = line

# Sort the created dictionary in alphabetical order
sorted_dict = {key: dict1[key] for key in sorted(dict1.keys())}

# Calculate the average word length for each starting letter and add the results to a new dictionary
for i in sorted_dict:
    dict_avg[i] = (sum(len(word) for word in sorted_dict[i].split(',')))/len(sorted_dict[i].split(','))
# Print the final results in a key value pair
for key, value in dict_avg.items():
    print(f"{key}:{value}")

