import csv

#nyc data
with open('csv/nyc.csv', 'rb') as n:
    reader = csv.reader(n)
    nyc_list = list(reader)
#print nyc_list

#nyc doe data
with open('csv/nycdoe.csv', 'rb') as d:
    reader = csv.reader(d)
    doe_list = list(reader)
#print doe_list

#nyc doe specialized high school data
with open('csv/specializedhs.csv', 'rb') as hs:
    reader = csv.reader(hs)
    hs_list = list(reader)
#print hs_list

def racepercent(borough, year):
    races = dict()
    for row in nyc_list[1:]:
        for n in range(len(row)):
            if row[0].strip() == borough and int(row[1].strip()) == year:
                population = int(row[2].strip()) * 1.0
                white = int(row[3].strip()) / population
                black = int(row[5].strip()) / population #do not be alarmed! I KNOW HOW TO COUNT!
                asian = int(row[6].strip()) / population
                other = int(row[7].strip()) / population
                if (row[8].strip() != 'null'):
                    hispanic = int(row[8].strip()) / population
                else:
                    hispanic = 0
                foreign = int(row[9].strip()) / population
                races.update({'population': population, 'white': white, 'black': black, 'asian': asian, "other": other, 'hispanic': hispanic, 'foreign': foreign})
    return races
##THIS IS WHERE I NEED HELP IM NOT SURE WHY IT WONT ADD THE DATA TO THE DICT
p = racepercent('manhattan', 1900)
print p.keys()

##IGNORE THIS FOR NOW ONCE THE FIRST FUNCITON WORKS, THESE WILL ALL BE VERY SIMILAR
def doe_genderpercent(borough, year):
    genders = {}
    for row in doe[1:]:
        print row
        if (row[0] == borough and row[1] == year):
            total = row[2] * 1.0
            female = row[3] / total
            male = row[4] / population
            genders = {"total": total, "female": female, "male": male}
    return genders

def doe_racepercent(borough, year):
    races = {}
    for row in doe[1:]:
        print row
        if (row[0] == borough and row[1] == year):
            total = row[2] * 1.0
            asian = row[3] / total
            black = row[4] / total
            hispanic = row[5] / total
            other = row[6] / total
            white = row[7] / total
            races = {"total": total, "asian": asian, "black": black, "hispanic": hispanic, "other": other, "white": white}
    return races

def hs_genderpercent(borough, year):
    genders = {}
    for row in hs[1:]:
        print row
        if (row[0] == borough and row[1] == year):
            total = row[2] * 1.0
            female = row[3] / total
            male = row[4] / population
            genders = {"total": total, "female": female, "male": male}
    return genders

def hs_racepercent(borough, year):
    races = {}
    for row in hs[1:]:
        print row
        if (row[0] == borough and row[1] == year):
            total = row[2] * 1.0
            asian = row[3] / total
            black = row[4] / total
            hispanic = row[5] / total
            other = row[6] / total
            white = row[7] / total
            races = {"total": total, "asian": asian, "black": black, "hispanic": hispanic, "other": other, "white": white}
    return races

