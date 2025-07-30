from MDIS import MDISParser

# Test case
test_cases = ["MSE:McAfee.I.A#Bypass_FakeAV_Joker_Adware!Phish ", "MSE:Avast.I.A#Bypass_FakeAV_Joker_Adware_Stealer_Resurrector_Spy!Phish"]
for id in test_cases:
    print(
        MDISParser(id).to_natural()
        if MDISParser(id).is_valid()
        else f"'{id}' is an invalid identifier."
    )
