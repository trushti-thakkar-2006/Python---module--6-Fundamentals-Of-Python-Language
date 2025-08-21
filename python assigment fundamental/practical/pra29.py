text = "  Python Programming is FUN!  "

# Remove extra spaces
print("Strip:", text.strip())

# Convert to lowercase
print("Lowercase:", text.lower())

# Convert to uppercase
print("Uppercase:", text.upper())

# Capitalize first letter
print("Capitalize:", text.capitalize())

# Title case (first letter of each word capitalized)
print("Title:", text.title())

# Replace a word
print("Replace 'FUN' with 'Awesome':", text.replace("FUN", "Awesome"))

# Count occurrences of a character
print("Count of 'm':", text.count("m"))

# Find position of a substring
print("Find 'Programming':", text.find("Programming"))

# Check if string starts with 'Python'
print("Starts with 'Python':", text.strip().startswith("Python"))

# Check if string ends with 'FUN!'
print("Ends with 'FUN!':", text.strip().endswith("FUN!"))

# Split into a list
print("Split:", text.strip().split())

# Join list elements into a string
words = ["Python", "is", "great"]
print("Join:", "-".join(words))
