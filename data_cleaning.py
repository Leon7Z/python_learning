def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


def read_data(filename):
    try:
        with open('d:\\' + filename + '.txt') as data:
            return data.readline().strip().split(',')
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None
#sorted把set转换为了list，所以可以切片
print(sorted(set([sanitize(each_t) for each_t in read_data('james')]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in read_data('julie')]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in read_data('mikey')]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in read_data('sarah')]))[0:3])

# with open(r'd:\james.txt') as jaf:
#     data = jaf.readline()
#     james = data.strip().split(',')
# with open(r'd:\julie.txt') as juf:
#     data = juf.readline()
#     julie = data.strip().split(',')
# with open(r'd:\mikey.txt') as mif:
#     data = mif.readline()
#     mikey = data.strip().split(',')
# with open(r'd:\sarah.txt') as saf:
#     data = saf.readline()
#     sarah = data.strip().split(',')
#
# clean_james = []
# clean_julie = []
# clean_mikey = []
# clean_sarah = []

#列表迭代
# for each_t in james:
#     clean_james.append(sanitize(each_t))
# for each_t in julie:
#     clean_julie.append(sanitize(each_t))
# for each_t in mikey:
#     clean_mikey.append(sanitize(each_t))
# for each_t in sarah:
#     clean_sarah.append(sanitize(each_t))

#列表推导
# clean_james = [sanitize(each_t) for each_t in james]
# clean_julie = [sanitize(each_t) for each_t in julie]
# clean_mikey = [sanitize(each_t) for each_t in mikey]
# clean_sarah = [sanitize(each_t) for each_t in sarah]
#
# print(sorted(clean_james))
# print(sorted(clean_julie))
# print(sorted(clean_mikey))
# print(sorted(clean_sarah))

