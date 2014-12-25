def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as jaf:
            data = jaf.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error' + str(ioerr))
        return(None)

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

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

clean_james2 = sorted([sanitize(each_item) for each_item in james])
clean_julie2 = sorted([sanitize(each_item) for each_item in julie])
clean_mikey2 = sorted([sanitize(each_item) for each_item in mikey])
clean_sarah2 = sorted([sanitize(each_item) for each_item in sarah])

#unique_james = []
unique_julie = []
unique_mikey = []
unique_sarah = []

#for each_item in clean_james2:
#    if each_item not in unique_james:
#        unique_james.append(each_item)
for each_item in clean_julie2:
    if each_item not in unique_julie:
        unique_julie.append(each_item)
for each_item in clean_mikey2:
    if each_item not in unique_mikey:
        unique_mikey.append(each_item)
for each_item in clean_sarah2:
    if each_item not in unique_sarah:
        unique_sarah.append(each_item)

print(sorted(set(sanitize(each_item) for each_item in james)))
print(sorted(set(sanitize(each_item) for each_item in julie)))
print(sorted(set(sanitize(each_item) for each_item in mikey)))
print(sorted(set(sanitize(each_item) for each_item in sarah)))
