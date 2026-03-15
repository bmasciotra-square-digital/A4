from task_one.task_one import task_one
from task_two.task_two import task_two
from task_three.task_three import task_three
from task_four.task_four import task_four
from task_five.task_five import task_five

if __name__ == '__main__':
    rsa = task_one()
    aes = task_two()
    task_three(rsa)
    task_four(aes)
    task_five(rsa)
