while True:
    user_choose=input(" do you want to add a new To-Do item? answer by y for yes and n for no. : ")
    if user_choose.lower()=='exit':
        print("thank you for using the To-Do program, come back again soon")
        break
    elif user_choose.lower()=='y':
        user_To_Do:str=input("Enter your new to do list item: ")
        with open ("to_do.txt","a+",encoding="UTF-8") as file:
            file.write(user_To_Do+"\n")
    elif user_choose.lower()=='n':
        user_list=input("Do you want to list the to do item. answer by y or n: ")
        if user_list.lower()=='y':
            with open('to_do.txt','r',encoding='utf-8') as file:
                if file.tell()==0:
                    print("There is no content. please try to fill up your to do list.")
                else:
                    print(file.read())
    else: 
        print("there is an error please try to type your answer corretly")
