

from Tkinter import *
import pickle
import os

class List(Tk):

    task_dict = {}
    task_list = []
    num_tasks = 0

    def __init__(self,master):
        td_frame = Frame(master)
        td_frame.grid()

        if not os.path.exists('listpersist.txt'):
            List.txt_create(self)
        try:
            saved_file = open(r'listpersist.txt','rb')
            build_list = pickle.load(saved_file)
            saved_file.close()
            for key in build_list:
                value = build_list[key]
                List.add_task(self,value,td_frame)
        except EOFError:
            print 'no previous save'



        master.title('TODO v. 1')
        task_input = Entry(master)
        task_input.grid()
        add_button = Button(master,text='add task',command=lambda:
                            self.add_task(task_input.get(),td_frame))
        add_button.grid()
        master.bind("<Return>",lambda a:List.add_task(self,task_input.get(),
                                             td_frame))
        save_button = Button(master, text='save',command=lambda:
                             self.save_tasks())
        save_button.grid()

    def add_task(self,task_ID,frame):
        List.num_tasks+=1

        single_task = Checkbutton(frame,text=task_ID,command=lambda:
                                  self.remove_task(single_task,frame,task_ID))
        single_task.grid(row=List.num_tasks,column=1)
        List.task_list.append(task_ID)
        #print List.task_list

    def remove_task(self,task,frame,task_ID):
        List.num_tasks-=1
        task.grid_forget()
        List.task_list.remove(task_ID)
        #print List.task_list

    def save_tasks(self):
        key_counter = 1
        for item in List.task_list:
            List.task_dict[key_counter]=item
            key_counter += 1
        #print List.task_dict

        save_file = open(r'listpersist.txt','wb')
        save_file.truncate()
        pickle.dump(List.task_dict,save_file)
        save_file.close()

    def txt_create(self):

        save_file = 'listpersist.txt'
        list_persist = open(save_file, 'a')
        list_persist.close()




root = Tk()
root.attributes("-alpha",1)
starter = List(root)
root.mainloop()