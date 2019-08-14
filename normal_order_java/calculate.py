import glob

total = glob.glob('*.java')
print(f"Totally {len(total)-1} interviews solved")
i = input('Press "Y" to see more: ')
if i.lower() == 'y':
	print(total)

