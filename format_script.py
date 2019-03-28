name_splitter = ' - '
n = 1
c = 0
open('list.txt','w').close()
with open('list_unformated.txt','r') as list_unf:
    track = ''
    for line in list_unf:
        if(n==1):
            track = line[:-1]
        if(n==2):
            track = track +name_splitter+ line
        if(n==3):
            with open('list.txt','a') as list_f:
                list_f.write(track)
            print(track);
            c+=1

        n=n+1
        if(n>3):
            n=1
print('Обработка '+str(c)+' треков закончена')
