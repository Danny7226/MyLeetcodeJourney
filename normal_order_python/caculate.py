import glob

total = glob.glob('*.py')
index = total.index('caculate.py')
del total[index]
print('\nTotally, in normal order: " {} " interviews SOLVED\n'.format(len(total)))

answer = input('Input "y" to show details: ')
if (answer == 'y'):
	print(total)
