def change_line(a, b, line):
    line = line.replace(line[a:b+1], "")
    return line

filename = input("Unesi ime titlova: ") + ".srt"
#print(filename)

f = open(filename, "r+")
L = list(f)
for line_index in range(0, len(L)):
    line = L[line_index]
    if("font color" in line):
        for i in range(0,len(line)):
            if(line[i] == "<"):
                for j in range(i, len(line)):
                    if (line[j] == ">"):
                        if("font color" in line[i:j]):
                            L[line_index] = change_line(i,j,line)
                        break

    line1 = L[line_index]                
    if("(" in line1):
        for i in range(0, len(line1)):
            if(line1[i] == "("):
                for j in range(i, len(line1)):
                    if(line1[j] == ")" and line1[i+1:j].isupper):
                        line2 = change_line(i,j,line)
                        L[line_index] = line2
                        break

    
new_file = ''.join(L)
f.close()

f = open(filename, "w")
f.write(new_file)
f.close()

        
  
        
