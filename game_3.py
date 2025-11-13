a=input('what do you whant:')
score=0
if a == 'shot':
    print('oh my god you can shot')
elif a== 'pas':
    print("you pass your friend")
elif a== 'shot_pawer':
    print('oh you goal ')
    score+=1
if score > 0:
    print(f"god jab you win by {score} goal")
else:
    print('what do you do')