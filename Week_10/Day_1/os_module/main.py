import os
import shutil

print(os.getcwd())

head_name = 'Test'

if not os.path.exists(head_name):
    os.mkdir(head_name)
    for x in range(1, 6):
        week_name = f'Week_{x}'
        os.mkdir(os.path.join(head_name, week_name))
        for y in range(1, 6):
            day_name = f'Day_{y}'
            os.mkdir(os.path.join(head_name, week_name, day_name))
            os.mkdir(os.path.join(head_name, week_name, day_name, 'lesson'))
            os.mkdir(os.path.join(head_name, week_name, day_name, 'homework'))
else:
    shutil.rmtree(head_name, ignore_errors=True)

