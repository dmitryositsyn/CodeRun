#  211. Встречи

n = int(input())
times = []
names = []

for _ in range(n):
    string = input().split()
    if string[0] == 'APPOINT':
        day = string[1]
        hh = int(string[2][0:2])
        mm = int(string[2][3:5])
        ap_start = hh*60 + mm
        
        duration = int(string[3])
        count_of_person = int(string[4])
        list_of_names = []
        for i in range(count_of_person):
            list_of_names.append(string[5+i])

        temp = (day, ap_start, duration)

        intersection = [False for _ in range(len(list_of_names))]
        for i in range(len(times)):
            time = times[i]
            if time[0] == day:
                if time[1] <= ap_start < time[1] + time[2] or \
                ap_start <= time[1] < ap_start + duration:
                    for j in range(len(list_of_names)):
                        if list_of_names[j] in names[i]:
                            intersection[j] = True
        
        if any(intersection) == False:
            times.append(temp)
            names.append(list_of_names)
            print('OK')
        else:
            print('FAIL')
            for i in range(len(intersection)):
                if intersection[i]:
                    print(list_of_names[i], end=' ')
            print()
    if string[0] == 'PRINT':
        day = string[1]
        name = string[2]
        subtimes = []
        subnames = []
        for time, l in zip(times, names):
            if time[0] == day and name in l:
                subtimes.append(time)
                subnames.append(l)
        for time, l in sorted(zip(subtimes, subnames)):
            hh = str(time[1]//60)
            mm = str(time[1]%60)
            if len(hh) == 1:
                hh = '0' + hh
            if len(mm) == 1:
                mm = '0' + mm
            print(hh + ':' + mm, time[2], ' '.join(l))