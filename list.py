#LIST

int_list=[1,2,3,4,5]
string_list=['mayank','niharika','sujal legend']

list1=[] #EMPTY LIST

mixed_list = [1, 'abc', True, 2.34, None] #MIXED LIST


names=['Alice','Bob', 'Sujal','Rohit', 'Varun']  #INDEXING IN THE LIST
print(names[0])
print(names[4])

names[0]='Sachin'    #LISTS ARE MUTABLE
print(names[0])


string_list=['mayank','niharika','sujal legend']  #ADD ELEMENT TO THE LIST
string_list.append("Bhavani")                         #YOU CAN USE INSERT AS WELL IN PLACE OF APPEND
print(string_list)




string_list.remove("Bhavani")
print("Bhavani")



string_list.index("sujal")  #Find Index

len(string_list)  #TO FIND LENGTH OF THE STRING



a = [1, 1, 1, 2, 3, 4]    #FREQUENCY
a.count(1) 

