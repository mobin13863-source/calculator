a=int(input('give me a namber:'))
b=int(input('give me secone number:'))

opreshin=input('with opreshin do you want:')

if opreshin=='zarb': 
    print(a*b)

elif opreshin=='tafrik': 
    print(a+b)

elif opreshin=='jam':
    print(a-b)

elif opreshin=='taksim':
    print(a/b)

elif opreshin=='takim bedon baki mnode':
        print(a//b)

elif opreshin=='darsad bagi monde':
    print(a%b)

elif opreshin=='tavan':   
     print(a**b)

else:
    print('hanoz zode bra to jojo')
