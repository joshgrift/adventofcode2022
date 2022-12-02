f = open(r"input.txt", "r")
raw = f.readlines()

elves = [0]
maxAmount = 0
maxElf = 0

for i in raw:
  if i == "\n":
    if elves[len(elves) - 1] > maxAmount:
      maxAmount = elves[len(elves) - 1]
      maxElf = len(elves)

    elves.append(0)
  else:
    elves[len(elves) - 1] += int(i.strip())

print("amount:" + str(maxAmount))
print("elf:" + str(maxElf))

elves.sort()
e = len(elves)
total = elves[e - 1] + elves[e - 2] + elves[e-3]
print("Top three total:" + str(total))