def age(birthdate):
    from datetime import datetime
    from datetime import date
    date1 = date.today()
    #date1 contains todays date as a datetime.datetime object it looks like mm-dd-yyyy hours:minutes:seconds
    date2 = str(birthdate)
    #date2 takes input from user and converts it to string so that it can be converted to datetime.date object
    date3 = datetime.strptime(date2, '%d-%m-%Y').date()
    #user input is requested to be of the format dd-mm-yyyy so .date() is used as we dont collect Time of birth from users
    #print(type(date3))
    return(date1 - date3)
    #returns difference between date1 and date3 as a datetime.datetime object so time will also be there as 0:00:00


dob = input("Enter Your Date of Birth in dd-mm-yyyy Format: ")
daysoldobject = age(dob)
daysold = str(daysoldobject).strip("days, 0:00:00")
#we only need the date so we convert the returned object into a string and strip away unwanted portions, the returned object is of the format ((value) days,  0:00:00)
agepresent = int(int(daysold)/365.25)
#an year is 365.25 days that is why every 4 years we have an additional day making it a leap year
print(f"You are {daysold} days old, That is Your Present age is {agepresent}" )
