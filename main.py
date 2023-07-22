HELP = """
/help - посмотреть справку всей программы.
/add - добавить задачу в список.
/show - показать список задач.
/delete_task - удалить одну задачу.
/delete_date - удалить все задачи по дате.
/delete_all - удалить все задачи.
/exit - выйти из программы."""

class Commands:
    tasks = dict()

    def __init__(self, command: str) -> None:
        self.command = command

    def print_help(self)-> None:
        print(HELP)

    def add_task(self, date: str, task: str) -> None:
        if date in self.tasks:
            self.tasks[date].append(task)
        else:
            self.tasks[date] = [task]
        print(f"Задача '{task}' добавлена на {date}.")

    def show_tasks(self)-> None:
        for key, value in self.tasks.items():
            print(key)
            counter = 1
            for task in value:
                print(f'{counter}. {task}')
                counter += 1
            counter = 1

    def delete_task(self, task: str) -> None:
        if task in self.tasks.values():
            for task in self.tasks.values():
                if task == task:
                    self.tasks.pop(task)
        print(f"Задача '{task}' удалена.")
    
    def delete_date(self, date: str) -> None:
        self.tasks.pop(date)
    
    def delete_all(self) -> None:
        self.tasks.clear()
        print("Все задачи удалены.")

if __name__ == '__main__':
    comand = input("Введите команду: ")
    commands = Commands(comand)

    while comand != "exit":
        if comand == "help":
            commands.print_help()
            print('-' * 40)
        elif comand == "add":
            date = input("Введите дату (ДД-ММ-ГГГГ): ")
            task = input("Введите задачу: ")
            commands.add_task(date, task)
            print('-' * 40)
        elif comand == "show":
            commands.show_tasks()
            print('-' * 40)
        elif comand == "delete_task":
            task = input("Введите задачу для удаления: ")
            commands.delete_task(task)
            print('-' * 40)
        elif comand == "delete_date":
            date = input("Введите дату для удаления всех задач в ней: ")
            commands.delete_date(date)
            print('-' * 40)
        elif comand == "delete_all":
            commands.delete_all()
            print('-' * 40)
        else:
            print("Нет такой команды.")
        comand = input("Введите команду: ")