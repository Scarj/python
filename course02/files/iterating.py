with open("data/spider.txt") as file:
    for line in file:
        print(line.strip().upper())


file = open("data/spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)