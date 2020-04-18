###========================================================================================
##                                                                                      ##
##                    created by YASSINE BAGHDADI at 18-04-2020 18:02                   ##
##                                                                                      ##
##========================================================================================

###========================================================================================
##                                                                                      ##
## for Sayeed AK's challenge                                                            ##
##                                                                                      ##
##========================================================================================

temp0 = []
temp1 = []
letters = []
while len(temp0) != 9:
    print('must be 9 letters like this : d g f a b e i h c')
    temp0 = sorted([x.upper() for x in input().split() if x]) 

print(temp0)#  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

places = [4, 0, 5, 3, 8, 1, 7, 2, 6]
for v in places:
    temp1.append(temp0[v])

print(temp1)# ['E', 'A', 'F', 'D', 'I', 'B', 'H', 'C', 'G']

for i in range(0, len(temp1)-1, 3):
    letters.append([temp1[i], temp1[i+ 1] , temp1[i + 2]])

print(letters)#  [['E', 'A', 'F'], ['D', 'I', 'B'], ['H', 'C', 'G']]
for line in letters:
    print(f'{line[0]} {line[1]} {line[2]}')

'''
E A F
D I B
H C G
'''

