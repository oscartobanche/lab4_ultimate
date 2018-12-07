#Oscar Tobanche
#Prof. Diego Aguirre
#manoj saha
#CS 2302
from chaininghashtable import ChainingHashTable
from linearprobinghashtable import LinearProbingHashTable
from doublehashinghashtable import DoubleHashingHashTable


from chaininghashtable import ChainingHashTable
input = open("glove.6B.50d.txt")
input_list = input.readlines()
chaining1 = ChainingHashTable()
linear_probing = LinearProbingHashTable()
double_hashing = DoubleHashingHashTable()
for i in range(len(input_list)):
    input_list[i] = input_list[i][:-2]
for elem in input_list:
    chaining1.insert(elem)
    linear_probing.insert(elem)
    double_hashing(elem)
# Main program to test HashTable classes took it from zybooks
keys = [35, 0, 22, 94, 220, 110, 4]
chaining = ChainingHashTable()

for key in keys:
    chaining.insert(key)


print ("Chaining: initial table:")
print (chaining)
print()

print ("Linear Probing: initial table:")
print (linear_probing)
print()

print ("Double Hashing: initial table:")
print (double_hashing)
print()

# Show tables after removing item 0
print ("=======================================")
chaining.remove(0)
linear_probing.remove(0)
double_hashing.remove(0)

print ("Chaining: after removing 0:")
print(chaining)
print()

print ("Linear Probing: after removing 0:")
print(linear_probing)
print()

print ("Double Hashing: after removing 0:")
print(double_hashing)
