fr=open("Desert.jpg","rb")

data=fr.read(20*1024)
i=0
while data:
	i+=1
	chunk=open("chunks/DesertChunk"+str(i)+".jpg","wb")
	chunk.write(data)
	chunk.close()
	data=fr.read(20*1024)
	
fr.close()