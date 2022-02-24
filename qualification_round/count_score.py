def count_score(submission, num_contributers, project_list, project_information, employee_list):
    """
    project info should be like:
    Logging 5 10 5 1
    """
    score = 0
    num_project = int(len(project_list))
    #print("np",num_project)
    schedule_list = [0] * num_contributers
    args_iter = submission[1:]
    #print("args_iter:", args_iter)
    employee_dict = {}
    for idx, name in enumerate(employee_list):
        employee_dict[name] = idx
    #print("employee_dict:", employee_dict)
    project_dict = {}
    for project_name, project_info in zip(project_list,project_information):
        project_dict[project_name] = [int(x) for x in project_info]
    print(project_dict)
    for i in range(num_project):
        project = args_iter[2*i]
        assignees = args_iter[2*i+1].split()
        busiest_contributer_startingday = 0
        for contributer in assignees:
            employee_idx = employee_dict[contributer]
            busiest_contributer_startingday = max(busiest_contributer_startingday, schedule_list[employee_idx])
        end_day = busiest_contributer_startingday + project_dict[project][0]
        if project_dict[project][2] - end_day > 0:
            print("max_score!")
            score += project_dict[project][1]
        else:
            score += max(0, project_dict[project][1] + project_dict[project][2] - end_day)
        for contributer in assignees:
            schedule_list[employee_dict[contributer]] = end_day
        print(project, schedule_list)
    return score
