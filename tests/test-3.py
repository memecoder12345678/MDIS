from MDIS import MDISParser
import json

# Test case
test_cases = "Win:Lumma.A#Dropper_Loader_Obfuscator_Polymorph_Resurrector_Bypass_Injector_Stealer_C2!Phish_Script"
with open("lumma_stix.json", "w", encoding="utf-8") as f:
    json.dump(MDISParser(test_cases).to_stix_dict(), f, indent=4, ensure_ascii=False)
