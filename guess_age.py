# ---------------------------------------------------------------------------------------

#                       **DOCUMENTATION**
# Take a user's name and birth year. Safely make that year an integer,
# then calculate when they'll turn 25, 50, 75, and 100. Tell 'em!
# what year will they turn 25, 50, 75, 100 ?
# print out when those years are?
# don't print any ages that have already past...
# print(name, "you'll be" age "in the Year, " year)

name = input("what is your name ")
dob_year = int(input("what is your birth year? "))

less_than_present = 2017 - dob_year # less_than_present (current_age)

if less_than_present <= 25:

    calc_future_age = 25 - less_than_present
    future_year = 2017 + calc_future_age # calc_future_age (turn_25, etc...)
    future_age = future_year - dob_year
    # print(name + ", you'll be " + future_age
    #", in the year " + future_year)
    print("You'll turn 25 in the year {}, {}".format(future_year, name))

if less_than_present <= 50:

    calc_future_age = 50 - less_than_present
    future_year = 2017 + calc_future_age
    future_age = future_year - dob_year
    #print(name + ", you'll be " + future_age
    #", in the year " + future_year)
    print("You'll turn 50 in the year {}, {}".format(future_year, name))

if less_than_present <= 75:

    calc_future_age = 75 - less_than_present
    future_year = 2017 + calc_future_age
    future_age = future_year - dob_year
    #print(name + ", you'll be " + future_age
    #", in the year " + future_year)
    print("You'll turn 75 in the year {}, {}".format(future_year, name))

if less_than_present <= 100:

    calc_future_age = 100 - less_than_present
    future_year = 2017 + calc_future_age
    future_age = future_year - dob_year
    #print(name + ", you'll be " + future_age
    #, in the year " + future_year)
    print("You'll turn 100 in the year {}, {}".format(future_year, name))
