from enum import Enum

class User:
    def __init__(self, name, level, discipline_points, best_progress, worst_progress):
        self.name = name
        self.level = level
        self.discipline_points = discipline_points
        self.best_progress = best_progress
        self.worst_progress = worst_progress

class Skill:
    def __init__(self, name, skill_type, discipline_points, progress):
        self.name = name
        self.skill_type = skill_type
        self.discipline_points = discipline_points
        self.progress = progress

class SkillType(Enum):
    SKILLS = 1
    PROGRESS = 2
    GRAPH = 3
    USER = 4

class SkillList:
    def __init__(self, skill_list):
        self.skill_list = skill_list

    def add_skill(self, skill):
        self.skill_list.append(skill)

class Plan:
    def __init__(self, id, name, plan_status):
        self.id = id
        self.name = name
        self.plan_status = plan_status

class PlanStatus(Enum):
    IN_PROGRESS = 1
    COMPLETED = 2

class PlanList:
    def __init__(self, plan_list):
        self.plan_list = plan_list

    def add_plan(self, plan):
        self.plan_list.append(plan)

    def update_plan(self, plan):
        self.plan_list[plan.id] = plan

    def remove_plan(self, plan):
        self.plan_list.remove(plan)