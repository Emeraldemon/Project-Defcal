from phase _function import phase
x = str(input('run program? (y/n): '))
if x == 'y':
    phase()
elif x == 'n':
    print('ok, program terminated')
else:
    print('Please type y or n')