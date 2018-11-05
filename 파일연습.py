outfile=open("c:\\users\\이한나\\documents\\f.txt","w")
outfile.write("fame")
outfile.close()

infile=open("c:\\users\\이한나\\documents\\f.txt","a")
infile.write("\nfriday\nframe\nfast\nfall\nfuture\nall we are challengers")
infile.close()

infile=open("c:\\users\\이한나\\documents\\f.txt","r")
for line in infile:
    line=line.rstrip()
    word_list=line.split()
    for word in word_list:
        print(word)
infile.close()
