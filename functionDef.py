__author__ = 'asee2278'


def analyze_list(lst) :
    count ={}
    for item in lst :
        if item in count :
            count[item] = count[item] + 1
        else :
            count[item] = 1

    return count

fruit = ['apple','oragne','apple','bananna','apple','orange']

print analyze_list(fruit)