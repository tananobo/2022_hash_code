class Contributer:
    def __init__(self, contributer_name, skill_num):
        self.name = contributer_name
        self.skill_num = int(skill_num)
        self.skill_set = {}
        self.work_day = 0
        

    def owned_skill(self, skill_name, skill_level):
        self.skill_set[skill_name] = int(skill_level)