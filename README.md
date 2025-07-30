<div align="center"> <img src="https://raw.githubusercontent.com/memecoder12345678/MDIS/refs/heads/main/imgs/icon.svg" alt="MDIS"></div>

<div align="center">
  <img src="https://img.shields.io/badge/creator-MemeCoder-red" alt="Made with ❤️ by MemeCoder">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/github/license/memecoder12345678/MDIS?style=flat&logo=open-source-initiative&logoColor=white" alt="License">
  <img src="https://img.shields.io/github/stars/memecoder12345678/MDIS?style=social" alt="Stars">
</div>
<h1 align="center">MDIS - Malware Detection and Identification System</h1>

MDIS (Malware Detection and Identification System) is an identifier format that standardizes malware classification. The syntax is designed to encode a threat's primary attributes, including its behavior, infection vector, and target OS.

## Features
- Classifies malware based on identifiers like OS, family, version, behaviors, and infection vectors.
- Outputs structured JSON reports for easier analysis.

## Why MDIS?
- All essential threat info packed into a single line
- Easy for analysts to interpret
- Suitable for automation, threat intelligence sharing
- Expandable to include new behaviors, vectors, OSes

## Installation
To get started with this project,  just install it via `pip`:

```bash
pip install mdis-sec
```

## Example Usage
You can test the MDIS tool with the following identifiers:

```python
from MDIS import MDISParser

# Test case
test_cases = ["And:SpyFin.II.B#Spy_Banker!Phish", "Win:DCry.A#Ransom!Removable"]
for id in test_cases:
    print(
        MDISParser(id).to_natural()
        if MDISParser(id).is_valid()
        else f"'{id}' is an invalid identifier."
    )

```

## Contributing
Feel free to open issues or submit pull requests if you have any suggestions or improvements!

## More Information
For more information about the project, please refer to the [`docs/`](./docs) directory.

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

