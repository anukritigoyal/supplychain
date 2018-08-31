state = {}

def create(name, dept, role, check):
    role_check = {role : check}
    obj = Ptype(name, dept, role_check)
    state[name] = obj

def retrieve():
    return state

class Ptype(object):
    def __init__(self, ptype_name, dept, role):
        self.name = ptype_name
        self.dept = dept
        self.role = role

# def create(name, dept, role, check, action):
#     if action == "create":
#         state = {}
#         role_check = {role : check}
#         obj = Ptype(name, dept, role_check)
#         state[name] = obj
#     elif action == "retrieve":
#         return state