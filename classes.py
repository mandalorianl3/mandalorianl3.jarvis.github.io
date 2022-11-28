# sections message into more digestible parts
class Divy_message:
    def __init__(self, command, aux_one, aux_two):
        self.command = command
        self.aux_one = aux_one
        self.aux_two = aux_two


# class for storing schedule objects
class Sched_object:
    def __init__(self, due_date, description):
        print("sched object init")
        self.due_date = due_date
        self.description = description

    def __str__(self):
        return f"**{self.due_date}** - {self.description}"

# stores sched objects
class Members:
    members = []
    schedules = []

    def __str__(self, x):
        return f"{self.members[x]}"

    def add_entry(self, member, schedule_object):
        print(member)
        print(schedule_object)
        self.members.append(member)
        self.schedules.append(schedule_object)
