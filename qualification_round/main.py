import random
import argparse

import count_score
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
random.shuffle(project_name_list)
print(project_name_list)

for selected_project_name in project_name_list:
    selected_project = project[selected_project_name]
    project_end_day = 0
    for skill in selected_project.ness_skill:
        find_skilled_person = False
        for name, candidate in contributor.items():
            if candidate.ask_skill_level(skill[0]) >= skill[1] and selected_project.count_score(candidate.scheduled_period + 1) > 0:
                find_skilled_person = True
                candidate.assigned_project.add(selected_project_name)
                project_end_day = max(project_end_day, candidate.scheduled_period + selected_project.project_period)
                break
        if not find_skilled_person:
            print("{} can not be accepted!".format(selected_project_name))



        print(skill)
    

"""
submission = ["3", "WebServer", "Bob Anna", "Logging", "Anna", "WebChat", "Maria Bob"]
final_score = count_score.count_score(submission, num_contributers, project_list, project_information, contributer_list) 
print(final_score)
"""