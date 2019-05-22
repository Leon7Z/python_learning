man = []
other = []
try:
    data = open(r'd:\sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
except IOError:
    print('The datafile is missing!')
finally:
    if 'data' in locals():
        data.close()
try:
    with open(r'd:\man_data.txt', 'w') as man_file, open(r'd:\role_data.txt', 'w') as role_file:
        print(man, file=man_file)
        print(other, file=role_file)
except IOError as err:
    print('File error:' + str(err))


