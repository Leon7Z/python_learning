# import re
# reg_string = "hellolasjfo123123@lhj.com"
# reg = r"\d"
# s = re.findall(reg, reg_string)
# print(s)

movies = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, [
        "Graham Chapman", [
            "Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
# print(movies)
# for each_item in movies:
#     if isinstance(each_item,list):
#         for each_item1 in each_item:
#             if isinstance(each_item1, list):
#                 for each_item11 in each_item1:
#                     if isinstance(each_item11, list):
#                         print(each_item11)
#                     else:
#                         print(each_item11)
#             else:
#                 print(each_item1)
#     else:
#         print(each_item)
def print_movie(movie_info, indent = False, level = 0):
    for each_item12 in movie_info:
        if isinstance(each_item12,list):
            print_movie(each_item12, indent, level + 1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='')
            print(each_item12)
            
print_movie(movies, True)

