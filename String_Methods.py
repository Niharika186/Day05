# print('ALL'.isidentifier()) # true
# print('_'.isidentifier()) # true
# print('1all'.isidentifier()) # false
# print(' all'.isidentifier()) # false
# print(''.isspace()) # false
# print(' '.isspace()) # true
# print('    '.isspace()) # true
# print(isinstance('world',int)) # false
# print(isinstance('world',float)) # false
# print(isinstance('world',str)) # true
# a=8
# print(isinstance(a,int)) # true
# print('python'.isalpha()) # true
# print('pyt hon'.isalpha()) # false
# print('pyt5hon'.isalpha()) # false
# print('pyt_hon'.isalpha()) # false
# print('1234'.isalnum()) # true
# print('pot1234'.isalnum()) # true
# print('_1234'.isalnum()) # false
# print('  1234'.isalnum()) # false
print('goodmorning'.find('r')) # 6
print('goodmorning'.find('w')) # -1
print('goodmorning'.find('o',2)) # 2
print('goodmorning'.rfind('o')) # 5
print('goodmorning'.rfind('p')) # -1