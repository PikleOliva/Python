vector=[1, 2, 3, 4, 5]
print ("Vector original: ",vector)
print (f"Vector original: {vector}")


nuevo=[]
nuevo.append(vector[0])
print (nuevo)
vector.remove(vector[0])
print (vector)
nuevo.append(vector[vector.len-1])
print (nuevo)
vector.remove(vector[vector.len-1])
print (vector)