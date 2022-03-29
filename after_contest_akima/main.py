from contributer import Contributer
from project import Project

import read_input
import time



#input_dir = "a_an_example"
#input_dir = "b_better_start_small"
#input_dir = "c_collaboration"
#input_dir = "d_dense_schedule"
#input_dir = "e_exceptional_skills"
#input_dir = "f_find_great_mentors"

def Run(input_dir, roop):
    start = time.time()
    print(input_dir + " Start!")
    contributer_dict, project_dict = read_input.read_input("input/"+input_dir+".in.txt")
    day = 0

    

    ans_project = []
    ans_contributer = []

    for x in range(roop):
        ###得点が高い順に並べる（貪欲法）

        priority_project_list = []
        for i in project_dict.values():
            priority_project_list.append([i.expect_score(day), i.name])

        priority_project_list = sorted(priority_project_list, reverse = True)

        ##正の得点が得られなくなったら終了
        if priority_project_list[0][0] <= 0:
            break

        for i in priority_project_list:
            assign_list = []
            cnt = 0
            ###仕事が終了済みか確認
            if project_dict[i[1]].status == False:
                ###必要なスキル
                #print(project_dict[i[1]].skill_set)
                for skill in project_dict[i[1]].skill_set.keys():
                    for person in contributer_dict.values():
                        ###
                        if skill in person.skill_set:
                            if person.skill_set[skill] >= project_dict[i[1]].skill_set[skill] and person.work_day == 0 and person.name not in assign_list:
                                assign_list.append(person.name)
                                cnt += 1
                                break
                if len(assign_list) == project_dict[i[1]].role_num:
                    ans_project.append(i[1])
                    project_dict[i[1]].status = True
                    ans_contributer.append(assign_list)
                    for j in assign_list:
                        contributer_dict[j].work_day = project_dict[i[1]].period
                            
            else:
                continue
        
        day += 10

        for i in contributer_dict.values():
            if i.work_day > 0:
                i.work_day = max(i.work_day-10, 0)

    #print(ans_project)
    #print(ans_contributer)

    with open("output/"+input_dir+"_out.txt", mode="w") as f:
        f.write(str(len(ans_project))+"\n")
        for i in range(len(ans_project)):
            f.write(ans_project[i]+"\n")
            f.write(" ".join(ans_contributer[i])+"\n")
        

    end_all = time.time()
    print(end_all-start)
    print("End!")

#input_list = ["a_an_example", "b_better_start_small", "c_collaboration", "d_dense_schedule", "e_exceptional_skills", "f_find_great_mentors"]
#roop_list = [5, 10000, 100, 100, 100, 100]
input_list = ["b_better_start_small", "e_exceptional_skills"]
roop_list = [10000, 100]

for i in range(len(input_list)):
    Run(input_list[i], roop_list[i])
#print(priority_project_list)


#print(contributer_dict["Anna"].skill_set)
#print(project_dict["WebServer"])