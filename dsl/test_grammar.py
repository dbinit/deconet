import os

from textx import metamodel_from_file
from textx.exceptions import TextXSyntaxError


def test_grammar():
    # Get the directory of this script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Create metamodel from grammar file
    grammar_file = os.path.join(current_dir, "deconet.tx")
    metamodel = metamodel_from_file(grammar_file)

    # Test parsing the sample config
    sample_file = os.path.join(current_dir, "sample_config.dcn")
    try:
        model = metamodel.model_from_file(sample_file)
        print("✅ Grammar test passed!")
        print("\nParsed configuration:")
        print(f"Found {len(model.routers)} routers:")
        for router in model.routers:
            print(f"\nRouter: {router.name}")
            print(f"Components: {len(router.components)}")
            for component in router.components:
                print(f"  - {component.__class__.__name__}: {component.name}")

        print(f"\nFound {len(model.constraints)} constraints:")
        for constraint in model.constraints:
            print(f"  - {constraint.name}: {constraint.type}")

    except TextXSyntaxError as e:
        print("❌ Grammar test failed!")
        print(f"Error: {e}")
        print(f"Line: {e.line}, Column: {e.col}")


if __name__ == "__main__":
    test_grammar()
