# Aaryan Pal
def generate_report(title, *args, **kwargs):

    print(f"\nReport Title: {title}")
    print("================================================")

    for key, val in kwargs.items():
        if key != 'conclusion' and key != 'skip_section':
            print(f"{key.capitalize()}: {val}")

    print("\nReport Sections:")
    print("----------------")
    x = 0
    for i in args:
        if x != kwargs['skip_sections'][0] - 1:
            print(f"Section {x + 1}: {i}")
        x = x + 1

    print("\nConclusion:")
    print("-----------")
    print(f"{kwargs['conclusion']}")


generate_report("Monthly Sales Report",
                "Introduction: Overview of sales performance.",
                "Data Analysis: Breakdown of sales data by region.",
                "Market Trends: Analysis of current market trends.",
                author="John Doe",
                date="September 2024",
                conclusion="Overall, sales have increased by 15% compared to the previous month.",
                skip_sections=[2])

#
#
#
#

# Ashutosh Awasthi
# def generate_report(title,*args, **kwargs):
#     args1=args[0]
#     conclusion=input("Enter the conclusion")
#     print(f"Report Title: {title}")
#     print("=======================================")
#
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
#     print()
#     print("Report Sections :")
#     print("-----------------")
#
#     for i in args1:
#         print(i)
#
#     print("Conclusion")
#     print("-----------")
#     print(conclusion)
#
#
#
#
#
#
#
# title=input("Enter the title of the report : ")
# author=input("Enter the name of author: ")
# date=input("Enter date in dd/mm/yy format:")
# dicto={"Author":author,"date":date}
# t=[]
# while True:
#     sec=input("Enter section in report eg Section 1: Introduction XYX: ")
#     t.append(sec)
#     ch=input("Enter 1 to input for section or press any other key to generate report:")
#     if ch=="1":
#         continue
#     else:
#         break
# generate_report(title,tuple(t),author,date)
