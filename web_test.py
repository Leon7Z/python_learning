import pickle
from dict_test import AthleteList


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline().strip().split(',')
        return AthleteList(data.pop(0), data.pop(0), data)
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None


def put_to_store(file_list):
    all_athletes = {}
    for each_file in file_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athlete.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)  # 序列化保存
    except IOError as ioerr:
        print('File error(put_and_store):' + str(ioerr))
    return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open('athlete.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)  # 序列化读
    except IOError as ioerr:
        print('File error(get_and_store):' + str(ioerr))
    return all_athletes


