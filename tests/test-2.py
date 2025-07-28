from MDIS import MDISParser

# Test case
test_cases = ["And:SpyFin.II.B#Spy_Banker!Phish", "Win:DCry.A#Ransom!Removable"]
for id in test_cases:
    MDISParser(id).dump_report_file()
