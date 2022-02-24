def count_score(submission, num_contributers, project_info, employee_list):
    """
    project info should be like:
    Logging 5 10 5 1
    """
    score = 0
    num_project = submission[0]
    schedule_list = [0] * num_contributers
    args_iter = submission[1:]
    employee_dict = {}
    for idx, name in enumerate(employee_list):
        employee_dict[name] = idx
    for i in range(num_project, 2):
        project = args_iter[i].split()
        assignees = args_iter[i+1].split()
        busiest_contributer_startingday = 0
        for contributer in assignees:
            employee_idx = employee_dict[contributer]
            busiest_contributer_startingday = max(busiest_contributer_startingday, schedule_list[employee_idx])
        end_day = busiest_contributer_startingday + project[1]
        if project[3] - end_day > 0:
            score += project[2]
        else:
            score += min(0, project[2] - project[3] - end_day - 1)
        for contributer in assignees:
            schedule_list[employee_dict[contributer]] = end_day
    return score



