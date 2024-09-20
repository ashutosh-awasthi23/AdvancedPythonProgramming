song_list=[]
def add_song():
    global song_list
    name=input("Enter song :")
    song_list.append(name)
    print("Song added successfully")

def remove_song():
    global song_list
    print(song_list)
    name = input("Enter song u want to remove :")
    song_list.remove(name)
    print("Deleted successfully")

def display_song():
    global song_list
    print("The songs are as follows :")
    for i in song_list:
        print(i)

def slice_playlist():
    try:
        start=int(input("Enter the start index :"))
        stop=int(input("Enter the last index :"))
        if start<len(song_list) and stop<len(song_list):
            if start==stop:
                print(song_list[start])
            elif start<stop:
                print(song_list[start:stop+1])
        else:
            raise ValueError()
    except ValueError:
        print("Wrong Indices")

while True:
    ch=input("Press 1: Add a song \nPress 2: Remove a song\n Press 3: To display songs\n Press 4:Slice the playlist\n")
    if ch=="1":
        add_song()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    elif ch=='2':
        remove_song()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    elif ch=='3':
        display_song()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    elif ch=='4':
        slice_playlist()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    else:
        print("Wrong Choice Entered")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    ch2=input("Press 1 to continue")
    if ch2=='1':
        continue
    else:
        break