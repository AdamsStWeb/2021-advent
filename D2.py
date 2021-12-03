arr = open('input2.txt').readlines()
a = sum([int(x[1].replace('\n', '')) for x in (x.split(' ') for x in arr) if x[0] =='forward' ])
b = sum([int(x[1].replace('\n', '')) if x[0] == 'down' else (0 - int(x[1].replace('\n', ''))) for x in (x.split(' ') for x in arr) if x[0] != 'forward' ])
print( a * b)

aim, x, y = 0, 0, 0
z = [("aim = aim - {0}".format(x[1].replace('\n', '')) if x[0] == 'up' else("aim = aim + {0}".format(x[1].replace('\n', '')) if x[0] =='down' else "x,y = x + {0}, y + ({0} * aim)".format(x[1].replace('\n', '')))) for x in (x.split(' ') for x in arr) ]

for i in z: 
    exec(i)
print(x*y)
