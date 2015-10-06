

from Tkinter import *
import pickle
import os
from task import Task

class ToDoList(Tk):

    task_dict = {}
    task_list = []
    num_tasks = 0

#The problem appears to be in re-initalizing the tasks see 'try' clause below
    def __init__(self,master):
        td_frame = Frame(master)
        td_frame.grid()
        button_frame = Frame(master)
        button_frame.grid()
        if not os.path.exists('listpersist.txt'):
            self.txt_create()
        try:
            saved_file = open(r'listpersist.txt','rb')
            build_list = pickle.load(saved_file)
            saved_file.close()
            for key in build_list:
                value = build_list[key]
                self.add_task(value,td_frame)
                self.task_list_add(value)
        except EOFError:
            print 'no previous save'



        master.title('TODO v. 1')
        task_input = Entry(master)
        task_input.grid()
        add_button = Button(master,text='add task',command=lambda:
                        self.create_task_object(task_input.get(),button_frame))
        add_button.grid()
        master.bind("<Return>",lambda a:ToDoList.add_task(self,task_input.get(),
                                             button_frame))
        save_button = Button(master, text='save',command=lambda:
                             self.save_tasks())
        save_button.grid()

        self.debug_element_printer("__init__")
    def create_task_object(self,task_ID,frame):
        #List.num_tasks+=1

        new_task = Task(task_ID)
        self.add_task(new_task,frame)
        #ToDoList.task_list.append(new_task)
        self.task_list_add(new_task)
        self.debug_element_printer("create_task_object")

    def task_list_add(self,task_to_add):
        ToDoList.task_list.append(task_to_add)

    def add_task(self,task_object,frame):
        ToDoList.num_tasks += 1

        single_task = Checkbutton(frame,text=task_object.name,
                        foreground=task_object.color,
                        command=lambda:
                        self.remove_task(task_object,frame,single_task))
                        #self.remove_task(single_task,frame,task_ID))

        single_task.grid(row=ToDoList.num_tasks,column=1)

        self.debug_element_printer("add_task")

    def remove_task(self,task_object,frame,task_name):
        ToDoList.num_tasks-=1
        task_name.grid_forget()
        ToDoList.task_list.remove(task_object)
        self.debug_element_printer("remove_task")

    def save_tasks(self):
        key_counter = 0
        for item in ToDoList.task_list:
            ToDoList.task_dict[key_counter]=item
            key_counter += 1
        print ToDoList.task_dict

        save_file = open(r'listpersist.txt','wb')
        save_file.truncate()
        pickle.dump(ToDoList.task_dict,save_file)
        save_file.close()
        self.debug_element_printer("save_tasks")

    def txt_create(self):

        save_file = 'listpersist.txt'
        list_persist = open(save_file, 'a')
        list_persist.close()

    def debug_element_printer(self,function):
        print "After running {0} the current number of tasks is: {1}".format(function,ToDoList.num_tasks)
        print "--------------------------------"
        print "After running {0} the current task dictionary is: {1}".format(function,ToDoList.task_dict)
        print "--------------------------------"
        print "After running {0} the current task list is: {1}".format(function, ToDoList.task_list)
        print "--------------------------------\n"*2


root = Tk()
root.attributes("-alpha",1)
starter = ToDoList(root)
root.mainloop()