# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("pokemon name",["Pikachu","Squirtle","Charmandra"])
# table.add_column("Type",["Electric","Water","Fire"])
# table.align="r"
# class User:
#     def __init__(self,c):
#         self.c=c
#         print(self.c)
#     print("hello")

# user1=User("hii")
# #user1.a="ishika"
# user2=User("hola")
# # user2.a="anuj"
# # print(user1.a)
#print(user2.a)
#print(user2.c)
import random
question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"}
]
print(random.choice(question_data["text"]))