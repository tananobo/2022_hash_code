import pandas as pd


import read_input


#input_dir = "input/a_an_example.in.txt"
#input_dir = "input/b_better_start_small.in.txt"
input_dir = "input/c_collaboration.in.txt"
#input_dir = "input/d_dense_schedule.in.txt"
#input_dir = "input/e_exceptional_skills.in.txt"
#input_dir = "input/f_find_great_mentors.in.txt"


contributor_df, project_df, project_skill_df = read_input.read_input(input_dir)

day = 0
roop = 100
ans = []

for i in range(roop):

    ##仕事をやった時に得られる得点を求める
    project_df["expected_point"] = project_df["max_score"]     
    project_df.loc[project_df["best_day"] < project_df["project_period"] + day, "expected_point"] = project_df["max_score"] - ( project_df["project_period"] + day - project_df["best_day"] )
    project_df = project_df[project_df["status"] == False]
    project_df = project_df.sort_values("expected_point", ascending=False)

    if project_df.at[project_df.index[0], "expected_point"] <= 0:
        break

    ##その仕事がやれるかを判定する
    for index, data in project_df.iterrows():
        
        candidate_list = []
        data = project_skill_df.loc[index]
        data = data[data>0]

        #その仕事が終わっていないか判定
        if project_df.at[index, "status"] == False:
            for skill, level in data.iteritems():
                #print(skill)
                candidate = contributor_df.loc[(contributor_df[skill] >= level) & (contributor_df["status"] == False)].sort_values(skill)
                if len(candidate) > 0:
                    name = candidate.index[0]
                    candidate_list.append(name)
                    contributor_df.at[name, "status"] = True
            
            if len(candidate_list) == len(data):
                ans.append(index)
                ans.append(candidate_list)
                project_df.at[index, "status"] = True
                for j in candidate_list:
                    contributor_df.at[j, "work_days"] = project_df.at[index, "project_period"]

    day += 1
    contributor_df.loc[contributor_df["work_days"] > 0, "work_days"] -= 1
    contributor_df.loc[contributor_df["work_days"] == 0, "status"] = False

#print(contributor_df)
#print(project_df)
#print(project_skill_df)
#print(ans)
print(int(len(ans)//2))

for i in range(len(ans)):
    if i%2 == 0:
        print(ans[i])
    else:
        print(*ans[i])