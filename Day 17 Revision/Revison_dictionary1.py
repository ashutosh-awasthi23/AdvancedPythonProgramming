movie_dict={}
def add_movie():
    global movie_dict
    name=input("Enter movie :")
    movie_dict[name]=0
    print("Movie added successfully")

def vote_movie():
    global movie_dict
    print(list(movie_dict.keys()))
    name = input("Enter movie u want to vote for :")
    movie_dict[name] +=1
    print("Voted successfully")

def remove_movie():
    global movie_dict
    print(list(movie_dict.keys()))
    name = input("Enter movie u want to remove :")
    del(movie_dict[name])
    print("Deleted successfully")

def display_result():
    global movie_dict
    print("The results are as follows :")
    for key,value in movie_dict.items():
        print(f"{key}:{value}")

def top_movie():
    global movie_dict
    i=list(movie_dict.values()).index(max(list(movie_dict.values())))
    print(f"The movie with the most vote is{list(movie_dict.keys())[i]}")

while True:
    ch=input("Press 1: Add a movie \n Press 2: Vote for a movie \n Press 3: Remove a movie\n Press 4: To display results\n Press 5:Find top Movie\n")
    if ch=="1":
        add_movie()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    elif ch=='2':
        vote_movie()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    elif ch=='3':
        remove_movie()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    elif ch=='4':
        display_result()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    elif ch=='5':
        top_movie()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    else:
        print("Wrong Choice Entered")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    ch2=input("Press 1 to continue")
    if ch2=='1':
        continue
    else:
        break