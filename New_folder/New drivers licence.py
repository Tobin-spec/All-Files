import math

name = input()
no_of_agents = int(input())
people = input().split()

people.append(name)
people.sort()

find_pos = people.index(name)
pos = find_pos + 1

timming = pos / no_of_agents
time = math.ceil(timming) * 20
print(time)

