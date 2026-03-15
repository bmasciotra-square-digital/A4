from task_one.task_one import task_one
from task_two.task_two import task_two
from task_three.task_three import task_three
from task_four.task_four import task_four
from task_five.task_five import task_five

if __name__ == '__main__':
    # Task One
    rsa = task_one()

    # Task Two
    aes = task_two()

    # Task Three
    task_three(rsa)
    task_four(rsa, aes)
    task_five(rsa)
