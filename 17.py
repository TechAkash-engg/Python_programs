str1=input("ENTER THE TEXT ")
f1=input("Enter the filename ")
file1=open(f1,"w")
file1.write(str1)
file1.close()

file = open(f1, "r")
number_of_lines = 0
number_of_words = 0
number_of_characters = 0
for line in file:
  line = line.strip("\n")

  words = line.split()
  number_of_lines += 1
  number_of_words += len(words)
  number_of_characters += len(line)
  
  for letter in line:
    if letter == " ":
      number_of_characters-=1

file.close()

print("Number of lines ", number_of_lines, "\nNumber of words ", number_of_words, "\nNumber of characters ", number_of_characters)
