# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(month, year):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def daysInMonth(month, year):
    days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeapYear(year):
        days_per_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    return days_per_month[month-1]

def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    """Test for isLeapYear"""
    test_cases1 = [(2000, True), (1900, False)]

    for (arg, answer) in test_cases1:
        result = isLeapYear(arg)
        if result == answer:
            print "Passed!"
        else:
            print "Failed!"

    """Tests for daysBetweenDates"""
    test_cases2 = [((2012,1,1,2012,2,28), 58),
                   ((2012,1,1,2012,3,1), 60),
                   ((2011,6,30,2012,6,30), 366),
                   ((2011,1,1,2012,8,8), 585 ),
                   ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases2:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

    """Tests for daysInMonth"""
    test_cases3 = [((2, 2000),29), ((2, 1900),28)]

    for (args, answer) in test_cases3:
        result = daysInMonth(*args)
        if result == answer:
            print "Passed!"
        else:
            print "Failed!"

    """Tests for nextDay"""
    test_cases4 = [((2000,2,28),(2000,2,29)), ((2000,12,31),(2001,1,1)),((2001,2,28),(2001,3,1))]

    for (args, answer) in test_cases4:
        result = nextDay(*args)
        if result == answer:
            print "Passed!"
        else:
            print "Failed!"

test()