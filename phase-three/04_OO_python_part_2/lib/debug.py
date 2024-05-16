import ipdb

from models.owner import Owner
from models.cat import Cat

apollo = Cat(name="Apollo", age=2, breed='bangel', indoor = False)
daisy = Cat(name='Daisy', breed='Cat')

emiley = Owner(name='Emiley', age=29)
ayva = Owner(name='Ayva', age=17)

ipdb.set_trace()