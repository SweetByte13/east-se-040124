import ipdb
from lib.models import Pet, Owner

  
apollo = Pet(name="Apollo", age=2, breed='Dog')
daisy = Pet(name="Daisy", breed='Dog')

emily= Owner(name='Emily', age=29)

ipdb.set_trace()