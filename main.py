from complementary_code_generator import CCG
from complementary_code_generator import uni
from basic_func import string_inv

k = 3
[A,B] = CCG(k)

[A1,A2] = uni(A)
[B1,B2] = uni(B)

print(A,B)
print(A1,A2,B1,B2)

# Output the data stream into sequence file
file = open("seqA1.txt","w")

characters = A1.copy()
file.write(characters）
file.close()
