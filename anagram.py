print 'c' < 'C'
phrase1 = 'Clint Eastwood'
phrase2 = 'Clint Eastwood'

def isAnagram(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        sortString(string1)
        sortString(string2)
        return string1 == string2

def sortString(string):
    uString = list(string.replace(' ',''))
    counter = 0
    l = len(uString)
    print counter, uString
    while counter < l-1:
        if uString[counter] != uString[counter+1]:
            if uString[counter] > uString[counter+1]:
                tmp = uString[counter]
                uString[counter] = uString[counter+1]
                uString[counter+1] = tmp
                counter += 1
                counter = counter % l-1
                print counter, uString
            if uString[counter] < uString[counter+1]:
                counter += 1
                counter = counter % l-1
                print counter, uString
        if uString[counter] == uString[counter+1]:
            counter += 1
            counter = counter % l-1

sortString(phrase1)