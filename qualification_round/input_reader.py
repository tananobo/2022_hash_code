
class Project:
    def __init__(self, project_name, project_period, max_score, best_day, num_role):
        self.project_name = project_name
        self.project_period = int(project_period)
        self.max_score = int(max_score)
        self.best_day = int(best_day)
        self.num_role = int(num_role)
        self.ness_skill = []
        self.assignee_name = []
        print("new Project {} has been created!".format(project_name))

    def add_skill(self, skill_name, skill_level):
        self.ness_skill.append((skill_name, skill_level))

    def count_score(self, start_day):
        if start_day + self.project_period <= self.best_day:
            return self.max_score
        else:
            return max(self.max_score - (start_day + self.project_period - self.best_day), 0)


class Contributor:
    def __init__(self, contributor_name, num_skill):
        self.contributor_name = contributor_name
        self.num_skill = int(num_skill)
        self.skillset = {}
        self.scheduled_period = 0
        self.assigned_project = set()
        print("new Contributor {} has been hired!".format(contributor_name))

    def add_skill(self, skill_name, skill_level):
       self.skillset[skill_name] = skill_level

    def levelup_skill(self, skill_name):
        if skill_name in self.skillset:
            self.skillset[skill_name] += 1
        else:
            self.skillset[skill_name] = 1

    def ask_skill_level(self, skill_name):
        if skill_name in self.skillset:
            return self.skillset[skill_name]
        return 0


def read_input(location):
    with open(location) as f:
        contributor_num, project_num = map(int, f.readline().split())
        contributor = {}
        for i in range(contributor_num):
            name, num_skill = f.readline().split()
            contributor[name] = Contributor(name, int(num_skill))
            for j in range(int(num_skill)):
                skill_name, skill_level = f.readline().split()
                contributor[name].add_skill(skill_name, int(skill_level))
        line = f.readline()
        project = {}
        while line:
            project_name, project_period, max_score, best_day, num_role = line.split()
            project[project_name] = Project(project_name, project_period, max_score, best_day, int(num_role))
            for i in range(int(num_role)):
                skill_name, skill_level = f.readline().split()
                project[project_name].add_skill(skill_name, int(skill_level))
            line = f.readline()
    return contributor, project


if __name__ == "__main__":
    contributor, project = read_input("input/a_an_example.in.txt")
    print(contributor)
    print(project)
