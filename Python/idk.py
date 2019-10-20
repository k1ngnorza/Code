aThreePoints = int(input(''))
aTwoPoints = int(input(''))
aOnePoints = int(input(''))

bThreePoints = int(input(''))
bTwoPoints = int(input(''))
bOnePoints = int(input(''))

Apples = aThreePoints * 3 + aTwoPoints * 2 + aOnePoints * 7

if Apples > Bananas:
    print('A')
elif Bananas > Apples:
    print('B')
else:
    print('T')