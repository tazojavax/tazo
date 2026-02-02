# with open("titanic.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#
# print("Passengers:", len(lines) - 1)
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         data = line.strip().split(",")
#         print(data)


#savarjisho 2

# # oldes guy
#
# oldest_age = 0
# oldest_name = ""
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)  # skip header
#     for line in f:
#
#         # fix comma inside Name
#         if '"' in line:
#             first = line.find('"')
#             second = line.find('"', first + 1)
#             name = line[first:second + 1]
#             line = line.replace(name, name.replace(",", ""))
#
#         parts = line.strip().split(",")
#
#         if parts[5] != "":
#             age = float(parts[5])
#             if age > oldest_age:
#                 oldest_age = age
#                 oldest_name = parts[3]
# print(oldest_name, oldes
# _age)

#ramdeni gadarcha class shi
# survived per class
# survivors_class = {}
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         parts = line.split(",")
#         pclass = parts[2]
#         survived = parts[1]
#
#         if survived == "1":
#             survivors_class[pclass] = survivors_class.get(pclass, 0) + 1
#
# print(survivors_class)


# first class pessengers

# first_class = []
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         parts = line.split(",")
#         if parts[2] == "1":
#             first_class.append(parts[3])
#
# print(first_class)



# class passenger
#
# class_count = {}
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         pclass = line.split(",")[2]
#         class_count[pclass] = class_count.get(pclass, 0) + 1
#
# print(class_count)



# #ramdeni gadarcha
#
# survived = died = 0
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         Survived = line.split(",")[1]
#         if Survived == "1":
#             survived += 1
#         else:
#             died += 1
#
# print("Survived:", survived)
# print("Died:", died)
#
# male = female = female_survived = 0
#
# with open("titanic.txt", "r", encoding="utf-8") as f:
#     next(f)
#     for line in f:
#         Sex = line.split(",")[4]
#         Survived = line.split(",")[1]
#
#         if Sex == "male":
#             male += 1
#         else:
#             female += 1
#             if Survived == "1":
#                 female_survived += 1
#
# print("Males:", male)
# print("Females:", female)
# print("Females survived:", female_survived)

# #teoria 1
# #write , read and append
# #teoria 2
# #sheqmnis fails da shignit weras daiwyebs
# #teoria 3
# #list — ცვლილებადი სტრუქტურაა (შეიძლება დამატება/შეცვლა)
# #tuple — უცვლელია (შექმნის შემდეგ ვერ იცვლება, უფრო უსაფრთხო და სწრაფი)
# #teoria 4
# #key - გასაღები