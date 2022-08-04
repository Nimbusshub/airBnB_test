# id = "1772d537-d6ba-40da-b628-04263724e587"
# objName = "BaseModel"
# objNameId = objName + "." + id


# print(objNameId, type(objNameId))
# print("{}.{}".format(objName, id), type(objNameId))

# obj = {"name": "Beloved"}
# obj2 = {}


# # if len(obj2) != 0:
# # if any(obj2):
# if obj2 is not None:
#     print("True")
# else:
#     print("False")

# Testing Eval() function
# eval(expression[, globals[, locals]])
# To evaluate a string-based expression, Python’s eval() runs the following steps:

# Parse expression
# Compile it to bytecode
# Evaluate it as a Python expression
# Return the result of the evaluation


# x = 10
# y = 20

# # print(eval("x * y"))

# print(eval("x * y"))

# greet = "Hello world"

# split_greet = greet.split(" ")

# print(greet)
# print(split_greet)
# print(split_greet[0])
# print(split_greet[1])

# all_objs = {
#     "BaseModel.35827f08-cc42-4421-9642-59c52ae228d6": {"id": "35827f08-cc42-4421-9642-59c52ae228d6", "created_at": "2022-08-05T01:48:56.133015", "updated_at": "2022-08-05T01:48:56.133099", "__class__": "BaseModel"},
#     "BaseModel.969c6425-4393-4421-9085-8065f55bf7ee": {"id": "969c6425-4393-4421-9085-8065f55bf7ee", "created_at": "2022-08-05T01:51:46.607424", "updated_at": "2022-08-05T01:51:46.607501", "__class__": "BaseModel"},
#     "BaseModel.8e4b02af-738c-4644-9de7-7f9a6e61f2fc": {"id": "8e4b02af-738c-4644-9de7-7f9a6e61f2fc", "created_at": "2022-08-05T01:51:47.854629", "updated_at": "2022-08-05T01:51:47.854692", "__class__": "BaseModel"},
#     "BaseModel.a0077019-89c5-4dc4-adee-4d8422c7d293": {"id": "a0077019-89c5-4dc4-adee-4d8422c7d293", "created_at": "2022-08-05T01:51:48.669898", "updated_at": "2022-08-05T01:51:48.669963", "__class__": "BaseModel"}
# }

# print(all_objs["BaseModel.35827f08-cc42-4421-9642-59c52ae228d6"])
# print

# t = 'BaseModel BaseModel35827f08-cc42-4421-9642-59c52ae228d6'

# t_split = t.split(" ")


# print(t_split[1][0])

# if [t_split[1][0]] == '"':
#     print("True")
# else:
#     print("False")
#     # t_split[1] = t_split[1].replace('"', " ")


# print(t_split[1])
