# loop on tuple

a= (1,2,3)

for x in a:
    print(x)


# join method in tuple

a1= (1,2,3)
a2= (4,5,6)
a3= a1+a2
print(a3)  #(1,2,3,4,5,6)

# we can join two tuple using multiply as well

t1= (1,2,3,4)
t2= t1*2
print(t2) #(1, 2, 3, 4, 1, 2, 3, 4)



# Count method in tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)  # return count of 5 in tuple   # 2


# index()	Searches the tuple for a specified value and returns the position of where it was found (return first occurence index)


# Syntex === tuple.index(value, start, end)

#value	---> Required. The item to search for
#start  ---> Optional. Where to start the search
# end   ---> Optional. Where to end the search
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8, 5)

print(x)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8, 4, 7)

print(x)