# DecoNet

**DecoNet** (Declarative Config for Networks) is a proof-of-concept DSL for defining and managing fiber optic router configurations. It lets you specify router components hierarchically, set constraints (including between connected routers), validate configs, and optimize them.

## Goals
- Define router specs (line cards, modules, optics) declaratively.
- Validate existing configs against constraints.
- Optimize configs (e.g., cost per capacity) with OR-Tools.

## Stack
- **Python**: Core language.
- **TextX**: DSL parsing.
- **OR-Tools**: Constraint solving and optimization.

## Structure

```
deconet/
├── dsl/            # DSL grammar (deconet.tx) and sample configs
├── src/            # Python logic (model, validate, optimize)
├── tests/          # Tests
├── main.py         # Entry point
└── pyproject.toml  # Deps and config
```
