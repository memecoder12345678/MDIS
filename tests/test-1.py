import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from mdis import MDISParser

# Test case
test_cases = ["And:SpyFin.II.B#Spy_Banker!Phish", "Win:DCry.A#Ransom!Removable"]
for id in test_cases:
    print(
        MDISParser(id).to_natural()
        if MDISParser(id).is_valid()
        else f"'{id}' is an invalid identifier."
    )
