def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)


with open('james.txt', 'r') as jamesdata:
    jamesspeed = jamesdata.readline()
james = jamesspeed.strip().split(',')

with open('julie.txt', 'r') as juliedata:
    juliespeed = juliedata.readline()
julie = juliespeed.strip().split(',')

with open('mikey.txt', 'r') as mikeydata:
    mikeyspeed = mikeydata.readline()
mikey = mikeyspeed.strip().split(',')

with open('sarah.txt', 'r') as sarahdata:
    sarahspeed = sarahdata.readline()
sarah = sarahspeed.strip().split(',')

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_item in james:
    clean_james.append(sanitize(each_item))

for each_item in julie:
    clean_julie.append(sanitize(each_item))

for each_item in mikey:
    clean_mikey.append(sanitize(each_item))

for each_item in sarah:
    clean_sarah.append(sanitize(each_item))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
