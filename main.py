HELP = """
/help - посмотреть справку всей программы.
/add - добавить задачу в список.
/show - показать список задач.
/exit - выйти из программы.
/delete_task - удалить задачу из списка.
/delete_all - удалить все задачи из списка."""

class Commands:
    tasks_now = []
    tasks_tomorrow = []
    tasks_other = []

    def __init__(self, command: str) -> None:
        self.command = command

    def print_help(self)-> None:
        print(HELP)

    def add_task(self, task: str, date: str) -> None:
        if date.lower() == 'сегодня':
            self.tasks_now.append(task)
        elif date.lower() == 'завтра':
            self.tasks_tomorrow.append(task)
        else:
            self.tasks_other.append(task)
        print(f"Задача '{task}' добавлена на {date}.")

    def show_tasks(self)-> None:
        counter = 1
        print('Задачи на сегодня:')
        for task in self.tasks_now:
            print(f'{counter}. {task}')
            counter += 1
        counter = 1
        print('Задачи на завтра:')
        for task in self.tasks_tomorrow:
            print(f'{counter}. {task}')
            counter += 1
        counter = 1
        print('Задачи в других дня:')
        for task in self.tasks_other:
            print(f'{counter}. {task}')
            counter += 1
        counter = 1

    def delete_task(self, id_task: int) -> None:
        task = self.tasks.pop(id_task - 1)
        print(f"Задача '{task}' удалена.")
    
    def delete_all(self) -> None:
        del self.tasks[:]
        print("Все задачи удалены.")

if __name__ == '__main__':
    comand = input("Введите команду: ")
    commands = Commands(comand)

    while comand != "exit":
        if comand == "help":
            commands.print_help()
        elif comand == "add":
            date = input("Введите день (сегодня / завтра / любой): ")
            task = input("Введите задачу: ")
            commands.add_task(task, date)
        elif comand == "show":
            commands.show_tasks()
            print()
        elif comand == "delete_task":
            id_task = int(input("Введите номер задачи: "))
            commands.delete_task(id_task)
        elif comand == "delete_all":
            commands.delete_all()
        else:
            print("Нет такой команды.")
        comand = input("Введите команду: ")