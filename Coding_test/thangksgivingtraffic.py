import datetime

def solution(lines):
    start_bucket = []
    end_bucket = []
    for i in lines:
        parsing = i.split(" ")
        end_bucket.append(datetime.datetime.strptime(parsing[0] +" "+ parsing[1], '%Y-%m-%d %H:%M:%S.%f'))
    for i in range(0,len(lines)):        
        parsing = lines[i].split(" ")
        sec = int(parsing[2].replace("s","").split(".")[0])
        try:
            micro = int(parsing[2].replace("s","").split(".")[1])
        except:
            micro = 0
        print(str(sec) + "." + str(micro))
        start_bucket.append(end_bucket[i]-datetime.timedelta(seconds = sec,microseconds = micro*1000)+datetime.timedelta(microseconds = 1000))
    total_ps = []
    length = len(start_bucket)
    for i in range(0,length):
        min = end_bucket[i] 
        max = end_bucket[i] + datetime.timedelta(microseconds = 999000)
        counter = 0
        for j in range(0,length):
            if min <= start_bucket[j] <= max:
                counter += 1
            elif min <= end_bucket[j] <= max:
                counter += 1
            elif (start_bucket[j] <= min) and (end_bucket[j] >= max):
                counter += 1
        total_ps.append(int(counter))
    total_ps.sort()
    answer = total_ps[-1]
    return answer



lines = ["2016-09-15 20:59:57.421 0.351s",
             "2016-09-15 20:59:58.233 1.181s",
             "2016-09-15 20:59:58.299 0.8s",
             "2016-09-15 20:59:58.688 1.041s",
             "2016-09-15 20:59:59.591 1.412s",
             "2016-09-15 21:00:00.464 1.466s",
             "2016-09-15 21:00:00.741 1.581s",
             "2016-09-15 21:00:00.748 2.31s",
             "2016-09-15 21:00:00.966 0.381s",
             "2016-09-15 21:00:02.066 2.62s"]
solution(lines)