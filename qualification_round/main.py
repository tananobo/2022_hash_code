import count_score
import read_input
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('problem')
args = parser.parse_args()
file_name_dict = {"a": "a_an_example.in.txt", "b": "b_better_start_small.in.txt", "c": "c_collaboration.in.txt", "d": "d_dense_schedule.in.txt", "e": "e_exceptional_skills.in.txt", "f": "f_find_great_mentors.in.txt"}
file_name = file_name_dict[args.problem]
input_filepath = "input/" + file_name
print(input_filepath)
# データ読み込み
contributer_list, skill_list, ability_matrix, project_list, project_information, project_skill_matrix = read_input.read_input(input_filepath)
""" contributer_list, skill_list, ability_matrix = info
print(contributer_list,skill_list[0],ability_matrix[0][0]) """

num_contributers = len(contributer_list)

submission = ["3", "WebServer", "Bob Anna", "Logging", "Anna", "WebChat", "Maria Bob"]
final_score = count_score.count_score(submission, num_contributers, project_list, project_information, contributer_list) 
print(final_score)