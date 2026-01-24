# A savoir

**Set (ensemble)**  ne peut donc pas stocker de données mutables tels que les listes,
les dictionnaires, ou d’autres ensemble car en effet les ensembles eux, sont des objets mutables

**Syntaxe :**

- nomDeLensemble = set()
- nomDeLensemble = set(cle_1, cle_2, ..., cle_n)
- nomDeLensemble = {cle_1, cle_2, ..., cle_n}
- nomDeLensemble = set((cle_1, cle_2, ..., cle_n))
- nomDeLensemble = set([cle_1, cle_2, ..., cle_n])

## méthodes et fonctions  applicables aux ensembles en python

- remove() : permet de supprimer un élément d’un ensemble
**Nb :** Si l’élément à supprimer n’est pas dans l’ensemble, cette opération renverra une exception

- discard() : permettra de supprimer un élémens d’un ensemble., uniquement si celui-ci est
bien dans cet ensemble. Dans le cas contraire rien ne sera fait

- clear() : pour supprimer tous les élements d'un set

Nb : **toutes les opérations classiques propres aux ensembles renvoient un nouvel ensemble en résultat.**

Role des set : **sont grandement utiles lorsqu’il faut faire un test d’appartenance**
