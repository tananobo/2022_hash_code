import count_score
import recieve_input
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('problem')
args = parser.parse_args()
file_name_dict = {"a": "a_an_example.in.txt", "b": "b_better_start_small.in.txt", "c": "c_collaboration.in.txt", "d": "d_dense_schedule.in.txt", "e": "e_exceptional_skills.in.txt", "f": "f_find_great_mentors.in.txt"}
file_name = file_name_dict[args.problem]
input_filepath = "input_data/" + file_name

# データ読み込み
info = read_input_data.read_input_data(input_filepath)
print("customer num is: ", info[0])

input_info = recieve_input(problem)
final_score = count_score(submission, num_contributers, project_info, employee_list)