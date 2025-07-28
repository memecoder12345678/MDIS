# MDIS Draft v0.9

### Purpose:
To define a minimal yet expressive malware identifier that includes:

- Target OS
- Malware Family and Variant
- Behavior(s)
- Infection Vector(s)

### Format:
`{OS}:{Family}.{Variant}#{Behavior}!{Vector}`

Example:
- `Win:DCry.A#Ransom_Removable` -> `Windows, Encrypts data for ransom, Family DCry Build 1 of Major Variant 1, USB/removable devices-based delivery`
- `And:SpyFin.II.B#Spy_Banker!Phish` -> `Android, Espionage/data collection, Financial theft, Family SpyFin Build 2 of Major Variant 2, Phishing emails/websites-based delivery`

### Benefits:
- Fast parsing
- Readable by humans and machines
- Extensible dictionary system
