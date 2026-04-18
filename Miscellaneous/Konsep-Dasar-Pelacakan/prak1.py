from kanren.core import var, run
from kanren.facts import Relation, facts

parent = Relation()
facts(parent,   ("Homer", "Bart"),
                ("Homer", "Lisa"), 
                ("Abe", "Homer"))

x = var()
output = run(1, x, parent(x, "Bart"))
output1 = run(1, x, parent(x, "Homer"))
print("\nNama ayah Bart: ", output[0])
print("\nNama anak Abe: ", output1[0])