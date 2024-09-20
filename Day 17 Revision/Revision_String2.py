# def mask_sensitive_info(info, info_type):
#     try:
#         if info_type == 'email':
#             if info.count('@') == 1:
#                 m = []
#                 n = len(info)
#
#                 i = info.index('@')
#                 m.append(info[0])
#                 m.append("***")
#                 m.append(info[i-1: n])
#                 return "".join(m)
#             else:
#                 print("Incorrect Formatting in email")
#         elif info_type == 'credit_card':
#             if info:
#                 m = []
#                 n = len(info)
#                 m.append("**** **** **** ")
#                 m.append(info[n-4:n])
#                 return "".join(m)
#             else:
#                 print("Incorrect Formatting in Credit Card")
#         else:
#             raise ValueError
#     except ValueError:
#         print("Invalid info type")
#     finally:
#         print("Code run successfully.")
#
#
# print(mask_sensitive_info("Mayura.kumari@gmail.com", 'email'))
# # print(mask_sensitive_info("1234 5678 9101 1112", 'credit_card'))









#Ashutosh_Awasthi
# def mark_sensitive_info(info,info_type):
#     try:
#         if info_type not in ["email","credit_card"]:
#             raise ValueError
#         if info_type=='credit_card':
#             n=len(info)
#             temp=['*']*(n-4) +list(info[n-4:])
#             return "".join(temp)
#         elif info_type=='email':
#             text=""
#             ch=info.index("@")
#             text=info[0]+"***"+info[ch-1:]
#             return text
#
#     except ValueError:
#         print("Invalid Input")
#
#
# print(mark_sensitive_info("Mayura.kumari@xyz.com","email"))