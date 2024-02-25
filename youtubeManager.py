import json


def load_data():
    try :
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
    
def save_data_help(videos):
    try:
        with open("youtube.txt","w") as file:
            json.dump(videos,file)
    except FileNotFoundError:
            print("File Does Not Found")
            
            
def list_all_videos(videos):
    for index,video in enumerate(videos,start=1):
        print(f"{index}.{video}")
    
    
    
def add_video(videos):
    name =input("Enter Your Video Name :")
    time = input("Enter video time :")
    videos.append({'name':name,'time':time})
    save_data_help(videos)
    # pass



def update_details(videos):
    pass



def delete_video() :
    pass



def main():
    videos=load_data()
    while True:
        print("""\t
                Youtube Manager  |Choose any Of the option\n
                1.List all Videos\n
                2.Add Youtube Video\n
                3.Update the Youtube videoDetails\n
                4.Delete Youtube Video\n
                5.Exit the App""")
        choice = input("Enter Your Choice :")
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_details(videos)
            case "4":
                delete_video(videos)
            case "5":
                # exit()
                break
            case _:
                print("invalid Choice")
        


# __name__ is also callsed as dunder 
if __name__=="__main__":
    main()