import json
import tkinter as tk
from tkinter import simpledialog

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
    print("\n")
    print("*"*90)
    for index,video in enumerate(videos,start=1):
        print(f"{index}.{video['name']} , Durathin: {video['time']}")

    print("\n")
    print("*"*90)
    
def add_video(videos):
    name =input("Enter Your Video Name :")
    time = input("Enter video time :")
    videos.append({'name':name,'time':time})
    save_data_help(videos)
    # pass



def update_details(videos):
    list_all_videos(videos)
    index =  int(input("Enter The sr.no of video which u want to update :"))
    
    if 1<=index <=len(videos):
        current_name = videos[index-1]['name']
        current_time = videos[index-1]['time']
        # # new_name = input(f"Enter the new name (current name: {current_name}): ") or current_name
        # new_name = simpledialog.askstring("Input", f"Enter the new name (current name: {current_name}): ",
        #                                   initialvalue=current_name)
        name=input(f"Enter The new video Name  (current name : {current_name}): ")
        time=input(f"Enter new video Duration (current time:{current_time}) :")
        videos[index-1]={'name':name,'time':time}
        save_data_help(videos)
    else :
        print("""Inavlid Index""")
    



def delete_video(videos) :
    list_all_videos(videos)
    index =  int(input("Enter The sr.no of video which u want to Delete :"))
    if 1<=index <len(videos):
        del videos[index-1]
        save_data_help(videos)
    else :
        print("""Inavlid Index""")


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