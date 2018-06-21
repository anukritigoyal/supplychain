from . import create
from . import send
import time
create.cr('exec starts','Mike')
for i in range(1,10000):
    create.cr(str(i)+'ab','ubuntu')
    time.sleep(1/1000)
create.cr('execution is done','Mike')