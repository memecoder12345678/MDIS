<div align="center"> <img src="imgs/icon.svg" alt="MDIS"></div>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/github/license/memecoder12345678/MDIS?style=flat&logo=open-source-initiative&logoColor=white" alt="License">
  <img src="https://img.shields.io/badge/creator-MemeCoder-red" alt="Made with ❤️ by MemeCoder">
  <img src="https://img.shields.io/github/stars/memecoder12345678/MDIS?style=social" alt="Stars">
</div>
<h1 align="center">MDIS - Malware Detection and Identification System</h1>

MDIS (Malware Detection and Identification System) is a Python-based tool designed to help researchers and analysts classify and identify malware threats. It parses malware identifiers and outputs detailed reports based on behavior, infection vector, and target OS.

## Features
- Classifies malware based on identifiers like OS, family, version, behaviors, and infection vectors.
- Outputs structured JSON reports for easier analysis.

## Installation
To get started with this project, just clone the repository:

```bash
git clone https://github.com/memecoder123456/MDIS.git
```

## Usage

After cloning the repository, simply run the script to test the MDIS functionality:

```bash
python src/mdis.py
```

## Example Usage

You can test the MDIS tool with the following identifiers:

```python
from src.mdis import MDISParser

# Test case
identifier = "Win:DCry.A#Ransom!Removable"
parser = MDISParser(identifier)

if parser.is_valid():
    print(parser.to_natural())
```

## Contributing

Feel free to open issues or submit pull requests if you have any suggestions or improvements!

## More Information
For more information about the project, please refer to the [`docs/`](./docs) directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

