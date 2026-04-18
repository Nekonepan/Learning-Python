from kanren.core import var, run
from kanren.facts import Relation, facts

ayah1 = Relation()
facts(ayah1, ("Slamet", "Amin"),
            ("Slamet", "Anang"))

ayah2 = Relation()
facts(ayah2, ("Amin", "Badu"),
      ("Amin", "Budi"),
      ("Anang", "Didi"),
      ("Anang", "Dadi"))

kakek = Relation()
facts(kakek, ("Slamet", "Badu"),
            ("Slamet", "Budi"),
            ("Slamet", "Didi"),
            ("Slamet", "Dadi")
      )

paman = Relation()
facts(paman, ("Anang", "Badu"),
            ("Anang", "Budi"),
            ("Amin", "Didi"),
            ("Amin", "Dadi")
      )

x = var()
output = run(1, x, ayah2(x, "Badu"))
print("\nNama ayah Badu: ", output[0])

output1 = run(1, x, paman(x, "Badu"))
print("\nNama Paman Badu: ", output1[0])

output2 = run(1, x, kakek(x, "Badu"))
print("\nNama Kakek Badu: ", output2[0])