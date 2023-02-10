import random, string

print('Rules: ')
print('Guess the position of 4 numbers')
print('there will be 3 modes of indication:')
print()
print('1) not correct number and position')
print('2) correct number but not correct position')
print('3) both correct number & position')
print()
print('(0-9 and not repeatable)')
print()

ans=random.sample(string.digits,4)


check=[]



def check_vali():
    global guess, check, ans
    for j in range(len(guess)):
        if guess[j] in ans and guess[j]==ans[j]:
            check.append(3)
        elif guess[j] in ans:
            check.append(2)
        else:
            check.append(1)


def indict():
    global check
    check.sort()
    check.reverse()
    for k in check:
        print(k, end=' ')
    print()
    check=[]


#print(ans)

chance=10
guess=list(input('Guess(1234): '))

while guess:
    check_vali()
    indict()
    if guess==ans:
        print('''Congratulations!!! You've won~''')
        break
    
    chance-=1
    if chance>0:
        print('You still have', chance,'chance. ')
    else:
        print('Oh no~')
        print('Chances use up')
        print('THe correct answer is', ''.join(ans))
        print('Game over );')
        break
    print()
    guess=list(input('Guess(1234): '))
