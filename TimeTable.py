prof_list = ['skd', 'vs', 'dr', 'sc', 'nk', 'mk']
print('\n', prof_list)

subject_list_1 = ['cpp', 'auto', 'arch', 'cbnst']
# subject_list_3 = ['os', 'se', 'ada', 'java']
# subject_list_5 = ['ai', 'adbms', 'parallel', 'graph']

prof_prefer_sub = [['0' for _ in range(6)] for y in range(3)]

prof_prefer_sub[0][0] = '-'
prof_prefer_sub[0][1] = 'cpp'
prof_prefer_sub[0][2] = 'auto'
prof_prefer_sub[0][3] = '-'
prof_prefer_sub[0][4] = 'arch'
prof_prefer_sub[0][5] = 'cbnst'

prof_prefer_sub[1][0] = '-'
prof_prefer_sub[1][1] = 'os'
prof_prefer_sub[1][2] = 'se'
prof_prefer_sub[1][3] = 'ada'
prof_prefer_sub[1][4] = 'java'
prof_prefer_sub[1][5] = '-'

prof_prefer_sub[2][0] = 'ai'
prof_prefer_sub[2][1] = '-'
prof_prefer_sub[2][2] = '-'
prof_prefer_sub[2][3] = 'adbms'
prof_prefer_sub[2][4] = 'parallel'
prof_prefer_sub[2][5] = 'graph'

# for i in range(3):
#   print(prof_prefer_sub[i], '\n')

print()
time_table_1 = [[None for _ in range(5)] for _ in range(6)]
time_table_3 = [[None for _ in range(5)] for _ in range(6)]
time_table_5 = [[None for _ in range(5)] for _ in range(6)]

# prof_sub_map = {'prof_number' : {semester : [subjects to be taught in that semester]}}
prof_sub_map = {'skd': {1: None, 3: ['os'], 5: ['ai']},
                'vs': {1: ['cpp'], 3: ['se'], 5: None},
                'dr': {1: ['auto'], 3: ['ada'], 5: None},
                'sc': {1: None, 3: ['java'], 5: ['adbms']},
                'nk': {1: ['arch'], 3: None, 5: ['parallel']},
                'mk': {1: ['cbnst'], 3: None, 5: ['graph']}
                }

# for i in range(6):
#  print(time_table_1[i])


def create_time_table(profs, subject, semester, prof_sub_map):
    time_slot = 0

    for day in range(5):
        if day == 0:
            for prof in profs:
                if prof_sub_map[prof][semester] is not None:
                    time_table_1[time_slot][day] = prof
                    if time_slot >= 5:
                        time_slot = 0
                    else:
                        time_slot += 1
        else:
            time_slot = 0
            for i in range(1, 6):
                time_table_1[time_slot][day] = time_table_1[i][day - 1]
                if time_slot >= 5:
                    time_slot = 0
                else:
                    time_slot += 1

            day, slot = 1, 3
            for i in range(1, 5):
                time_table_1[slot][i] = time_table_1[0][day - 1]
                day += 1

    print()
    for i in range(6):
        print(time_table_1[i])



    print()
    for i in range(6):
        print(time_table_1[i])


create_time_table(prof_list, subject_list_1, 1, prof_sub_map)
# print()
# create_time_table(prof_list, subject_list_1, 3, prof_sub_map)
# print()
# create_time_table(prof_list, subject_list_1, 5, prof_sub_map)
