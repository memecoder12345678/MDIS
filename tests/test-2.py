from MDIS import MDISParser

# Test case
test_cases = ["MSE:McAfee.I.A#Bypass_FakeAV_Joker_Adware!Phish_PUA ", "MSE:Avast.I.A#Bypass_FakeAV_Joker_Adware_Stealer_Resurrector_Spy!Phish_PUA"]
for id in test_cases:
    MDISParser(id).dump_report_file()
