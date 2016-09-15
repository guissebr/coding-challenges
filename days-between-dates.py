# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    #returns the total number of days that have passed between two dates; accounts for leap years via the numOfLeapYears and daysSoFar functions.
    #c = complete
    if year2 - year1 <=1:
        c_year = 0
    else:
        if year2 - year1 > 1 and year2-year1 < 3:
            c_year = 1
    c_years = year2 - year1 -1
    c_leap_years = numOfLeapYears(year1, year2)
    total_days = c_years * 365 + c_leap_years + daysSoFar(year2, month2, day2) + (365-daysSoFar(year1, month1, day1))
    return total_days


def numOfLeapYears(year1, year2):
    #returns the number of leap years that have passes between two given years (non-inclusive); leverages the isLeapYear function.
    leap_years = 0
    while year1+1 < year2:
        if isLeapYear(year1+1) == True:
            leap_years +=1
            year1+=1
        year1+=1
    return leap_years

def isLeapYear(year):
    #for a given year, returns True if it's a leap year and False otherwise.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def daysSoFar(year, month, day):
    #returnsthe number of days that have passed so far in a given year for the given month and day.
    daysOfMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeapYear(year) and ((month == 2 and day > 28) or month > 2)  == True:
        days = 1
        counter = 0
        while counter < month-1:
            days = days + daysOfMonths[counter]
            counter +=1
        days = days + day
        return days
    days = 0
    counter = 0
    while counter < month-1:
        days = days+ daysOfMonths[counter]
        counter +=1
    days = days + day
    return days


# Test routine
def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()