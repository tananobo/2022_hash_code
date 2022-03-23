import random
import argparse

# import count_score
from input_reader import Project, Contributor, read_input

# recieve input problem "a-f" from CLI / output file path
parser = argparse.ArgumentParser()
parser.add_argument('problem')
args = parser.parse_args()
file_name_dict = {"a": "a_an_example.in.txt", "b": "b_better_start_small.in.txt", "c": "c_collaboration.in.txt", "d": "d_dense_schedule.in.txt", "e": "e_exceptional_skills.in.txt", "f": "f_find_great_mentors.in.txt"}
file_name = file_name_dict[args.problem]
input_filepath = "input/" + file_name
print("read_data_from :", input_filepath)

# read data from input file
contributor, project = read_input(input_filepath)

project_name_list = [key for key in project]
sorted_project_name_list = []

for project_name in project_name_list:
    sorted_num = project[project_name].best_day - project[project_name].project_period
    sorted_project_name_list.append((sorted_num, project_name))

project_name_list = [a for _, a in sorted(sorted_project_name_list)]

# random.shuffle(project_name_list)
# print(project_name_list)

num_recieved_project = 0
name_recieved_project = []
for selected_project_name in project_name_list:
    selected_project = project[selected_project_name]
    project_end_day = 0
    for skill in selected_project.ness_skill:
        find_skilled_person = False
        for name, candidate in contributor.items():
            if selected_project_name in candidate.assigned_project:
                continue
            if candidate.ask_skill_level(skill[0]) >= skill[1] and selected_project.count_score(candidate.scheduled_period + selected_project.project_period) > 0:
                find_skilled_person = True                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                candidate.assigned_project.add(selected_project_name)
                project_end_day = max(project_end_day, candidate.scheduled_period + selected_project.project_period)
                selected_project.assignee_name.append(candidate.contributor_name)
                break
        if not find_skilled_person:
            # print("{} can not be accepted!".format(selected_project_name))
            break
    if not find_skilled_person:
        continue
    else:
        for name, skill in zip(selected_project.assignee_name, selected_project.ness_skill):
            if contributor[name].ask_skill_level(skill[0]) == skill[1]:
                print("=====level up!=====")
                print(contributor[name].contributor_name, contributor[name].ask_skill_level(skill[0]))
                contributor[name].levelup_skill(skill[0])
                print(contributor[name].contributor_name, contributor[name].ask_skill_level(skill[0]))
    num_recieved_project += 1
    name_recieved_project.append(selected_project_name)

with open(args.problem+'.txt',mode="w") as f:
    f.write(str(num_recieved_project)+"\n")
    for project_name in name_recieved_project:
        f.write(project_name+"\n")
        f.write(" ".join(project[project_name].assignee_name)+"\n")


#submission = ["3", "WebServer", "Bob Anna", "Logging", "Anna", "WebChat", "Maria Bob"]
#final_score = count_score.count_score(submission, num_contributers, project_list, project_information, contributer_list) 
#print(final_score)

"""
submission = []
print(num_recieved_project)
submission.append(str(num_recieved_project))


"""