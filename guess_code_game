import random, string

print('Rules: ')
print('Guess the position of 4 numbers')
print('there will be 3 modes of indication:')
print()
print('1) not correct number and position')
print('2) correct number but not correct position')
print('3) both correct number & position')
print()
print('(1-9 and not repeatable)')
print()

ans=random.sample(string.digits,4)
ans=list(map(int,ans))

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

chance=20
guess=list(input('Guess(1234): '))

while guess:
    guess=list(map(int,guess))
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
        print('Game over );')
        break
    print()
    guess=list(input('Guess(1 2 3 4): '))
