"""
strip(): Remove Leading/Trailing
Removes all whitespaces characters (spaces, tabs, newlines) from both ends of the string. 
The original strings remains unchanged.

lstrip(): Remove Leading
Removes all whitespaces characters from the left (leading) end of the string. 
Useful for left-justifying text or cleaning data entry.

rstrip(): Remove Trailing
Removes all whitespaces characters from the right(Trailing) end of the string. 
Ideal for removing trailing newlines from file reads or right-justified text.

"""

#text = "    hello world   "
#print(text.strip())          #output = hello world
#print(text.lstrip())          #output = hello world   
#print(text.rstrip())          #output =     hello world


url = "https://www.codeanddebug.com/"

clean_url = url.strip("https:/")
print(clean_url)


