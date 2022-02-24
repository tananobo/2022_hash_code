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
info = read_input.read_input(input_filepath)
contributer_list, skill_list, ability_matrix = info
print(contributer_list,skill_list[0],ability_matrix[0][0])

num_contributers = len(contributer_list)

submission = ["3", "WebServer", "Bob Anna", "Logging", "Anna", "WebChat", "Maria Bob"]
project_info = ["Logging 5 10 5 1", "WebServer 7 10 7 2", "WebChat 10 20 20 2"]
final_score = count_score.count_score(submission, num_contributers, project_info, contributer_list) 
print(final_score)