# sort a file full of film names
# function to compare the lowercase item with the searchfor
def compare(item):
 return searchfor in item.lower()
# load the file into a list and
# close the file because the content is now in memory
with open("filmlist", "r") as film:
 filmlist = film.read().splitlines()
searchfor = input("Enter part of the film \
name you are searching for: ").lower().strip()
# use the built-in filter function, which will
# call the first parameter on every item on
# the list and, if it is true, it will use the item
foundlist = filter(compare, filmlist)
for name in foundlist:
 print(name)