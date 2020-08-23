time = str(input())

military_time= ""
for i in range(len(time) - 2):
    if " AM" in time:
        military_time += time   
