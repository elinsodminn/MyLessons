team1_num = 5
team2_num = 6
team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
score_1 = 40
score_2 = 42
team1_time = 15553.45
team2_time = 16662.46
tasks_total = 0
time_avg = 0

print('В команде %s участников %s !' % (team1_name, team1_num))
print('Итого сегодня в командах участников %x и %x !' % (team1_num, team2_num))
print('Команда {} решила задач: {} !'.format(team2_name,score_2))
print('{} решили задачи за {} с !'.format(team2_name,team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'Победа команды {team1_name}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'Победа команды {team2_name}!'
else:
    challenge_result = 'Ничья!'
print(challenge_result)

tasks_total = score_1 + score_2
time_avg = (team1_time+team2_time)//tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
