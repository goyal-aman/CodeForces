for _ in [0]*int(input()):
	s = input()
	l = len(s)
	if len(s)>10:
		print(f'{s[0]}{len(s)-2}{s[-1]}')
	else:
		print(s)
#better_code
#for _ in [0]*int(input()):
#    s=input()
#    l=len(s)-2
#    print(	[s,s[0]+str(l)+s[-1]][l>8]	)