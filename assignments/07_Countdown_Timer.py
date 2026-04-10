#Using a while loop, print a countdown from 10 to 1, then print: "🚀 Model training started!"

permission = input("Type GO to start countdown.")
if permission =="GO":
    nums = [10,9,8,7,6,5,4,3,2,1]
    index = 0
    while index<len(nums):
        print(nums[index])
        index+=1
    else:
        print("🚀 Model training started!")