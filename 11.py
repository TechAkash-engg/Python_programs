punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "hey[and[hy?is{was{they?ok!will{"
result=[]

for char in my_str:
   if char in punctuations:
       if char not in result:
           result.append(char)
   else:
      result.append(char) 
result=''.join(result)
print("Input:\n",my_str)
print("Output:\n",result)
