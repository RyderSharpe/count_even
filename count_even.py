target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

sum = 0
for count in range(1, target + 2, 2):
    count -= 1
    sum += count
    #print(count)
print(sum)





