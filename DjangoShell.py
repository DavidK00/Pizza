import os
from pydoc_data.topics import topics 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzaria.settings")

import django

django.setup()

from MainApp.models import Pizza

pizza = Pizza.objects.all()

for p in pizza:
    print(p.id, '  ',p.text)

p = Pizza.objects.get(id = 1)

print(p.text)

toppings = p.topping_set.all()

for t in topics:
    print(t.text)