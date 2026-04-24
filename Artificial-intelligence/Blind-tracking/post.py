from kanren.facts import Relation, facts, fact
from kanren.core import var, run
from kanren.goals import membero
from kanren import vars

jenis = Relation()
rasa = Relation()
original = Relation()

facts(jenis, ("makaroni balado", "makanan"),
                ("es boba", "minuman"),
                ("es jeruk", "minuman"),
                ("es teh", "minuman"),
                ("makaroni barbeque", "makanan"))

facts(rasa, ("makaroni balado", "pedas"),
                ("es boba", "manis"),
                ("es teh", "tawar"),
                ("makaroni barbeque", "barbeque"))

fact(original, "balado")
fact(original, "asin")

a = var()
makanan = run(0, a, jenis(a, "makanan"))
print("Menu berjenis makanan: ", makanan)

b = var()
minuman = run(0, b, jenis(b, "minuman"))
print("Menu berjenis minuman: ", minuman)

c = var()
minum_manis = run(0, c, jenis(c, "minuman"), rasa(c, "manis"))
print("Minuman yang memiliki rasa manis: ", minum_manis)

d = var()
makanan_original = run(0, d, jenis(d, "makanan"), original(d, "balado"), original(d, "asin"))
print("Makanan dengan jenis original: ", makanan_original)