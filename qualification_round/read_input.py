


input_dir = "input/a_an_example.in.txt"

def read_input(input_dir):

    #人の名前を入れるリスト
    contributer_list = []
    #スキル名を入れるリスト
    skill_list = []
    #人とスキルのマトリクスを入れるリスト
    ability_matrix = []

    project_list = []
    project_information = []
    project_skill_matrix = []

    input_file = open(input_dir, "r", encoding = "UTF-8")
    input_data = input_file.readlines()
    input_length = len(input_data)

    for i in range(input_length):
        input_data[i] = input_data[i].rstrip("\n")
        input_data[i] = input_data[i].split(" ")

    ##人のリストとスキルのリストを作る
    skill_num = 0 
    contributer_cnt = 0
    for i in range(input_length):
        if i == 0:
            contributer_num = int(input_data[i][0])
            project_num = int(input_data[i][1])

        elif contributer_cnt < contributer_num:
            if skill_num == 0:
                contributer_list.append(input_data[i][0])
                skill_num = int(input_data[i][1])
                skill_cnt = 0
            else:
                skill_list.append(input_data[i][0])
                skill_cnt += 1
                if skill_cnt == skill_num:
                    skill_num = 0
                    contributer_cnt += 1
        else:
            if len(input_data[i]) == 5:
                project_list.append(input_data[i][0])
                project_information.append(input_data[i][1:5])
            else:
                continue


    skill_list = list(set(skill_list))    

    ##マトリクスを作る
    for i in range(len(contributer_list)):
        skill_row = [0]*len(skill_list)
        ability_matrix.append(skill_row)

    for i in range(len(project_list)):
        skill_row = [0]*len(skill_list)
        project_skill_matrix.append(skill_row)
    ##
    skill_num = 0 
    contributer_cnt = 0
    project_cnt = 0
    for i in range(input_length):
        if i == 0:
            continue
        elif contributer_cnt < contributer_num:
            if skill_num == 0:
                contributer_name = input_data[i][0]
                contributer_index = contributer_list.index(contributer_name)
                skill_num = int(input_data[i][1])
                skill_cnt = 0
            else:
                skill_name = input_data[i][0]
                skill_index = skill_list.index(skill_name)
                ability_matrix[contributer_index][skill_index] = int(input_data[i][1])
                skill_cnt += 1
                if skill_cnt == skill_num:
                    skill_num = 0
                    contributer_cnt += 1

        else:
            if len(input_data[i]) == 5:
                project_name = input_data[i][0]
                project_index = project_list.index(project_name)
            else:
                skill_name = input_data[i][0]
                skill_index = skill_list.index(skill_name)
                project_skill_matrix[project_index][skill_index] = int(input_data[i][1])

    return contributer_list, skill_list, ability_matrix, project_list, project_information, project_skill_matrix


""" contributer_list, skill_list, ability_matrix, project_list, project_information, project_skill_matrix = read_input(input_dir)
print(contributer_list)
print(skill_list)
print(ability_matrix)
print(project_list)
print(project_information)
print(project_skill_matrix)
 """