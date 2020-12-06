# read line by line assigning the values to a rrays
cross_schools=[]
track_schools=[]
schools=[]
with open('newcrosslist.txt', mode='r', encoding='utf-8') as crosslist:

    for line in crosslist.readlines():
        # find the index of the word d2 or d1
        line=line.split()
        try:
            division=line.index('D2')
            division_name='D2'
        except:
            division=line.index('D1')
            division_name='D1'
        line=line[:division+1]
        line.pop(division-1)
        line=line[:-1]
        name_of_school=''
       
        for item in line:
            name_of_school+=item+' '
        cross_schools.append([name_of_school.strip(),division_name])
    # print(cross_schools)
    crosslist.close()
with open('newtracklist.txt',mode='r',encoding='utf-8') as track:
    print('\n\n\n\ntrack schools\n\n\n\n')
    for line in track.readlines():
        # find the index of the word d2 or d1
        line=line.split()
        try:
            division=line.index('D2')
            division_name='D2'
        except:
            division=line.index('D1')
            division_name='D1'
        line=line[:division+1]
        line.pop(division-1)
        line=line[:-1]
        name_of_school=''
       
        for item in line:
            name_of_school+=item+' '
        track_schools.append([name_of_school.strip(),division_name])
    # print(schools)
    track.close()
schools = cross_schools[:]
[schools.append(i) for i in track_schools if i not in cross_schools] 

# 622 schools in total
with open('d2_schools.txt', mode='w+',encoding='utf-8') as compiled:
    for item in schools:
        div=item[1]
        if div == 'D2':
            compiled.write(item[0]+'\n')
            # write the school
with open('d1_schools.txt', mode='w+',encoding='utf-8') as compiled:
    for item in schools:
        div=item[1]
        if div == 'D1':
            compiled.write(item[0]+'\n')
            # write the school
