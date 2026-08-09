This project is focusing on understanding how imports work.

part 1: the alembic

the import structure
- import ... :
    to access the whole module directly, e.g. `import elements`, `import alchemy.element` where the module element is under folder alchemy

    but if need to import a whole folder and call the modules under this folder, an `__init__` file is needed in this folder and use `__all__` list to list all the calling functions imported from specific files under this folder. See `alchemy/__init__.py` and `ft_alembic_4.py`

- from filename import method:
    to access the calling method directly, later can just call the function without filename prefix

part 2: distillation

nested import

- no dot: absolute import
    search the `sys.path` from scratch for a top-level module/package with this name. It's a full, independent lookup starting from the top.
- one dot: same package (current directory)
- two dots: parent package (one directory up)
    each additional dot climbs one more package level up the tree before searching.

part 3: transmutation

absolute and relative imports

- import the file directly

- import the file's folder and write the calling function into this folder's `__init__` file as an element

part 4: avoid explosion

why it may happen?

Python doesn't treat import as "copy-paste this file's contents in." It treats it as: run the module's code top to bottom, once, and cache the resulting module object in sys.modules. Every subsequent import of that same module just hands back the cached object — it doesn't re-run the file.

The circular trap comes from what happens the first time, while that initial run is still in progress.

solution:
- only one side keeps a top-level import
- Invert the dependency: pass light_spell_allowed_ingredients()'s result into validate_ingredients() as an argument, so the validator never imports the spellbook at all.
- Extract the shared piece: move whatever both sides need into a third, lower-level module that neither of the original two needs to import from each other for.
- Import the module, not the names, and access attributes through it lazily — same deferral effect, different spelling: import alchemy.grimoire.light_spellbook as sb used only inside a function body.