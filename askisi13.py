NameOfFile=input('Give the file name: ')
with open(NameOfFile) as f:
    data=f.read()
symbols="1234567890-=!@#$%^&*()_+<>?:{}[]';.,\|/`~"
for letter in data:
	if letter in symbols or letter=='"':
		data=data.replace(letter," ")
data=data.strip()
lst=data.split(" ")

while('' in lst):
    for elem in lst:
        if elem=='':
            lst.pop(lst.index(elem))
#print(lst)
def Zeugarwse(lstt):
    for element in lst:
    	check=0
    	position=lst.index(element)
    	deleted=lst.pop(position)
    	for elementt in lst:
    		if len(elementt)+len(deleted)==20:
    			print("To zeugari ",elementt,",",deleted,"exei athroizma 20")
    			lst.pop(lst.index(elementt))
    			check=1
    			break;
    	if check==0:
    		lst.insert(position,deleted)
Prelist=[]

while(Prelist!=lst):
    Zeugarwse(lst)
    Prelist=lst
    Zeugarwse(lst)

print('\n'+'Azeugarota einai ta:')
for el in lst:
	print(el)
