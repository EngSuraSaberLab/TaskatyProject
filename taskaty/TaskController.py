from .task import Task
from datetime import date
from tabulate import tabulate
from pathlib import Path

class TaskController:
    def __init__(self, file_name) :
        self.file_name=file_name

    def _ensure_file_exists(self):
        Path(self.file_name).touch(exist_ok=True)

    def _save_tasks(self, tasks):
        with open(self.file_name, 'w') as file:
            for task in tasks:
                row = Task(
                    task['title'],
                    task['description'],
                    task['start_date'],
                    task['end_date'],
                    task['done'],
                )
                file.write(str(row) + '\n')

    def add_task(self , args):
        self._ensure_file_exists()
        if not args.start_date:
            now=date.today().isoformat()
            args.start_date=now



        task=Task(args.title, args.description , args.start_date ,args.end_date , args.done)


        with open(self.file_name , 'a') as file:
            file.write(str(task) + '\n')


    def list_tasks(self):
        self._ensure_file_exists()
        incomlated_tasks=[]
        with open (self.file_name , 'r') as file :
            for line in file:
                title, description, start_date, end_date, done =line.split(', ')
                end_date=None if end_date =='None' else end_date
                done=False if done.strip('\n') =='False' else True
                if done:
                    continue
                incomlated_tasks.append({'title':title , 'description':description ,'start_date':start_date , 'end_date':end_date})

        return incomlated_tasks
    
    def list_all_tasks(self):
        self._ensure_file_exists()
        all_tasks=[]
        with open (self.file_name , 'r') as file :
            for line in file:
                title, description, start_date, end_date, done =line.split(', ')
                end_date=None if end_date =='None' else end_date
                done=False if done.strip('\n') =='False' else True
               
                all_tasks.append({'title':title , 'description':description ,'start_date':start_date , 'end_date':end_date ,'done':done})
                
        return all_tasks
    

    def due_date(self , start , end):
        start_date=date.fromisoformat(start)
        end_date=date.fromisoformat(end)
        date_delta=end_date - start_date
        return f'{date_delta.days} days left.'
    


    def print_table(self , tasks):
        formatted_tasks=[]
        for number, task in enumerate(tasks, start=1):
            if task['start_date'] and task ['end_date']:
                due_date= self.due_date(task['start_date'], task ['end_date'])
            else:
                due_date='Open'
            formatted_tasks.append({'no.': number, **task, 'due_date': due_date})
        print(tabulate(formatted_tasks, headers='keys'))


    def display(self, args):
        tasks = self.list_all_tasks() if args.all else self.list_tasks()
        if not tasks:
            print('There are no tasks. to add a task use add <task>')
            return
        self.print_table(tasks)

    def check_task(self, args):
        tasks=self.list_all_tasks()
        if not tasks:
            print('There are no tasks. to add a task use add <task>')
            return
        index=args.task if args.task is not None else len(tasks)
        if index <= 0 or index > len(tasks):
            print(f'Tasks number ({index}) does not exist')
            return
        
        tasks[index-1]['done']= True
        self._save_tasks(tasks)


    
    def remove(self, args):
        tasks=self.list_all_tasks()
        if not tasks:
            print('There are no tasks to remove.')
            return
        if args.task:
            index = args.task
        else:
            index =len(tasks)
        if index <= 0 or index > len(tasks):
            print(f'Task number ({index}) does not exist!')
            return
        tasks.pop(index-1)

        self._save_tasks(tasks)

    def reset(self,*args):
        with open(self.file_name, 'w') as file :
            file.write('')
            print('You Have Deleted All Tasks!')


