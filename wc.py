import sys
def open_file(data):
    try:
        f = open(data, 'r')
    except IOError:
        print("File %s not found" % data)
        raise SystemExit
def byte(data):
	open_file(data)
	e = open(data, 'r').read()
	return len(e.encode('utf-8'))
def word(data):
	open_file(data)
	e = open(data, 'r').read()
	return len(e.split())
def line(data):
	open_file(data)
	e = open(data, 'r').read()
	return len(e.split("\n"))-1
def char(data):
	e = open(data, 'r').read()
	return (len(e) - e.count(' '))
def maxLine(data):
	return len(max(open(data,'r'), key=len))-1

if __name__ == '__main__':
	ss, total = [], []
	file, totalc, totall, totalw, bLine = 0,0,0,0,-1
	wcc = False
	for f in sys.argv[1:]:	
		if f == '--help':
			print("Print help")
			raise SystemExit
		elif f == '--version':
			print("Created by William Kemp btw")
			raise SystemExit
		elif f == '-w' or f == '--words':
			ss.append('-w')
		elif f == '-c' or f == '--bytes':
			ss.append('-c')
		elif f == '-l' or f == '--lines':
			ss.append('-l')
		elif f == '-m' or f == '--chars':
			ss.append('-m')
		elif f == '-L' or f == '--max-line-length':
			ss.append('-L')
		# loop files
		else:
			bigLine = -1
			numlist = []
			file += 1
			# if no flags
			if len(ss) == 0:
				wcc = True
				totalc += byte(f)
				totall += line(f)
				totalw += word(f)	
				print(line(f),"	",word(f),"	",byte(f),f)
			#loop through flags
			for x in ss:			
				if x == '-w':
					numlist.append(word(f))
				if x == '-c':
					numlist.append(byte(f))
				if x == '-l':
					numlist.append(line(f))
				if x == '-m':
					numlist.append(char(f))
				if x == '-L':
					bLine = 0
					xLine = maxLine(f)
					if xLine > bLine:
						bLine = xLine
			# initizalise list with num of flags
			if file == 1:
				total = [0] * len(ss)
			total = list(map(lambda x,y:x+y, total, numlist))	
			# print multiple flag line
			if len(ss) > 0: 
				uu = open(f, 'r')
				if bLine > -1:
					numlist.append(xLine)
				# print each file instance
				print('\t'.join(str(x) for x in numlist),uu.name)		
	#print no flags mulitple files
	if wcc == True and file > 1:
		print(totall,"	",totalw,"	",totalc,"total")
	elif file > 1 and bLine >= 0:
		# print multiple file/flag total
		total.append(bLine)
		print('\t'.join(map(str, total)),"total")
	elif file > 1 and bLine == -1:
		# print multiple file/flag total
		print('\t'.join(map(str, total)),"total")		
	
