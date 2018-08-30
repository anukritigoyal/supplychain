state = {}

def create(name, dept, role, check):
    role_check = {role : check}
    obj = Ptype(name, dept, role_check)
    state[name] = obj

def retrieve(dept):
    rets = {}
    i = 0
    for data in state:
        if data.dept == dept:
            rets[i] = data
            i = i + 1
    return rets

class Ptype(object):
    def __init__(self, ptype_name, dept, role):
        self.name = ptype_name
        self.dept = dept
        self.role = role