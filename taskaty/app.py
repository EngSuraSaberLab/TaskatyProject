from argparse import ArgumentParser
from .TaskController import TaskController

def main():
    controller=TaskController('tasks.txt')

    parser=ArgumentParser(description='Taskaty CLI')
    subparsers=parser.add_subparsers()


    add_task=subparsers.add_parser('add', help='Type Your Task')
    add_task.add_argument('title', help='Task Title' , type=str)
    add_task.add_argument('-d','--description',help='Description Task',type=str , default=None)
    add_task.add_argument('-s','--start_date',help='Starting task date',type=str , default=None)
    add_task.add_argument('-e','--end_date',help='Ending task date',type=str , default=None)
    add_task.add_argument('--done',help='Task status',type=str , default=False)
    add_task.set_defaults(func=controller.add_task)


    list_tasks=subparsers.add_parser('list', help='incomplated tasks')
    list_tasks.add_argument('-a', '--all', help='All Tasks',action='store_true')
    list_tasks.set_defaults(func=controller.display)


    check_task = subparsers.add_parser('check', help='check task')
    check_task.add_argument('-t','--task',help='task number to be done or last task will be done' , type=int, default=None)
    check_task.set_defaults(func=controller.check_task)

    remove=subparsers.add_parser('remove', help='remove task')
    remove.add_argument('-t','--task',help='number task to remove', type=int, default=None)
    remove.set_defaults(func=controller.remove)

    reset=subparsers.add_parser('reset',help='reset taskaty and remove all thing')
    reset.set_defaults(func=controller.reset)

    args= parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
