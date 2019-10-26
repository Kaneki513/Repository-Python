'Шахматы'
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if 1<=x1<=8 and 1<=x2 and 1<=y1 and 1<=y2<=8:
    if abs(x1 - x2)+abs(y1 - y2)<=2:
    	print('yes')
    else:
    	print('no')
else:
	print('ERROR ERROR ERROR')
