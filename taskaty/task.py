
class Task:
    def __init__(self ,title ,describtion=None ,start_date=None ,end_date=None ,done=False):

        self.title=title
        self.describtion=describtion
        self.start_date=start_date
        self.end_date=end_date
        self.done=done


    def __str__(self) :
        return f'{self.title}, {self.describtion}, {self.start_date}, {self.end_date}, {self.done}'