from . import create
from . import send

create.cr('exec starts','Mike')
for i in range(1,10000):
    create.cr(str(i),'ubuntu')
create.cr('execution is done','Mike')