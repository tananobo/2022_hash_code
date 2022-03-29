class Project:
    def __init__(self, project_name, project_period, max_score, best_day, role_num):
        self.name = project_name
        self.period = int(project_period)
        self.max_score = int(max_score)
        self.best_day = int(best_day)
        self.role_num = int(role_num)
        self.skill_set = {}
        self.status = False

    def required_skill(self, skill_name, skill_level):
        self.skill_set[skill_name] = int(skill_level)

    def expect_score(self, day):
        if day + self.period > self.best_day:
            expect_score = max(0, self.max_score - ( (day + self.period) - self.best_day))
        else:
            expect_score = self.max_score
        
        return expect_score