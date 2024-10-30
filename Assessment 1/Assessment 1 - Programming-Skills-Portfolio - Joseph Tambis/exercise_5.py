# Exercise 5: Days of the Month

months = {1:31,
          2:[28,29],
          3:31,
          4:30,
          5:31,
          6:30,
          7:31,
          8:31,
          9:30,
          10:31,
          11:30,
          12:31}
print("This program will tell you how many days a month has after you input that month's number.")
query = int(input("Please input the month number here:  "))

if query > 0 and query <= 12:
    if query == 2:
        input ("Is the year a leap year?  ").lower()
        if input == "yes":
            print(f"That month has {months[query][1]} days.")
        else:
            print(f"That month has {months[query][0]} days.")
    else:
        print(f"That month has {months[query]} days.")
else:
    print('No month matches your input number.')