def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs

# 定制类写法
# class Athlete:
#     def __init__(self, name, dob=None, times=[]):
#         self.name = name
#         self.dob = dob
#         self.times = times
#
#     def top3(self):
#         return sorted(set([sanitize(each_t)
#                                for each_t in self.times]))[0:3]
#
#     def add_time(self, new_time):
#         self.times.append(new_time)
#
#     def add_times(self, new_times):
#         self.times.extend(new_times)


# 继承类写法
class AthleteList(list):
    def __init__(self, name, dob=None, times=[]):  # 先继承，在重构
        list.__init__([])  # 继承父类的构造方法，也可以写成：super(Chinese,self).__init__(name,age)
        self.name = name  # 定义类的本身属性
        self.dob = dob
        self.extend(times)

    def top3(self):
        return sorted(set([sanitize(each_t) for each_t in self]))[0:3]



def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline().strip().split(',')
        return AthleteList(data.pop(0), data.pop(0), data)
        #     althlete_dict = dict()
        #     althlete_dict['Name'] = data.pop(0)
        #     althlete_dict['DOB'] = data.pop(0)
        #     althlete_dict['Times'] = data
        # return althlete_dict
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None


sarah_data = get_coach_data('d:\\sarah2.txt')
james_data = get_coach_data('d:\\james2.txt')
julie_data = get_coach_data('d:\\julie2.txt')
mikey_data = get_coach_data('d:\\mikey2.txt')
# sarah_data = {}
# # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# sarah_data['Name'] = sarah.pop(0)
# sarah_data['DOB'] = sarah.pop(0)
# sarah_data['Times'] = sarah
# print(sarah_data['Name'] + "'s fastest times are:" + \
#       str(sorted(set([sanitize(each_t) for each_t in sarah_data['Times']]))[0:3]))
print(sarah_data.name + "'s fastest times are:" + str(sarah_data.top3()))
print(james_data.name + "'s fastest times are:" + str(james_data.top3()))
print(julie_data.name + "'s fastest times are:" + str(julie_data.top3()))
print(mikey_data.name + "'s fastest times are:" + str(mikey_data.top3()))




