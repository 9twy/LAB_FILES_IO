import json
while True:
    user_choose=input("Do you want to add new to do to the list ? enter y or n : ")
    if user_choose=="exit":
        break
    elif user_choose.lower()=='y':
        title=input("Enter title for the the to do item: ")
        date=input("enter the date: ")
        status=input("Enter the status (Done , Not done): ")

        mydict={
            "title":title,
            "date&time":date,
            "status":status
        }
        with open ('Bonus.json','a+',encoding="UTF-8") as file:
            file.write(json.dumps(mydict))
    elif user_choose.lower()=='n':
        is_reading=input("do you want to read the whole to do list? answer by 1 if you want to search using the title enter 2 if you want to mark specific Task as Done enter 3 : ")
        if is_reading=='1':
            with open('bonus.json','r',encoding='UTF-8')  as file:
                print(file.read())
        elif is_reading=='2':
            task_title=input("Please Enter the title: ")
            with open ('Bonus.json','r',encoding="utf-8") as file:
                json_load=json.load(file)
            
            for task in json_load:
                if task['title']==task_title:
                    print(f"{task['title']}\n{task['date&time']}\n{task[status]}")
        elif is_reading=='3':
            marking_task=input("Please Enter the title to mark as done : ")
            with open ('Bonus.json','r',encoding="utf-8") as file:
                json_load=json.load(file)
            
            for task in json_load:
                if task['title']==task_title:
                    task['status']='Done'
