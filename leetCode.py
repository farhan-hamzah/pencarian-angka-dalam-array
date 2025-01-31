nums = list(map(int, input("Masukan Array :").split()))
target = int(input("Masukan Target :"))
i = 0
while True:
    if target == nums[i]:
        break
    i += 1
print(i)
