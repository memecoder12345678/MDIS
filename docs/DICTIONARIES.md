# MDIS - Malware Dictionaries

This document describes the complete set of dictionaries used by **MDIS** (Malware Detection and Identification System) to standardize and define malware. These dictionaries allow the system to easily parse, extract, and display information in a human-readable and machine-processable format.

---

## Target Operating Systems

| Code    | Operating System             |
| ------- | ---------------------------- |
| Win     | Windows                      |
| Lin     | Linux                        |
| And     | Android                      |
| Mac     | macOS                        |
| iOS     | iOS                          |
| IoT     | Internet of Things           |
| BSD     | BSD-based OS                 |
| Web     | Web Applications             |
| MSE     | Multi-Platform               |
| VM      | Virtualization Environments  |
| Kai     | KaiOS                        |
| Tiz     | Tizen                        |
| Palm    | Palm OS                      |
| Chrome  | Chrome OS                    |
| RTOS    | Generic RTOS                 |
| Zeph    | Zephyr                       |
| Contiki | Contiki                      |
| RIOT    | RIOT OS                      |
| Tiny    | TinyOS                       |
| ZOS     | IBM z/OS                     |
| AIX     | IBM AIX                      |
| OpenVMS | OpenVMS                      |
| Solaris | Solaris                      |
| Alpine  | Alpine Linux                 |
| Photon  | Photon OS                    |
| Clear   | Clear Linux                  |
| RHEL    | Red Hat Enterprise Linux     |
| SLES    | SUSE Linux Enterprise Server |
| Nix     | NixOS                        |

---

## Malware Behaviors

| Code         | Behavior Description                    |
| ------------ | --------------------------------------- |
| Ransom       | Encrypts data for ransom                |
| Spy          | Espionage/data collection               |
| Banker       | Financial theft                         |
| DDoS         | Denial-of-service attacks               |
| Miner        | Cryptocurrency mining                   |
| Dropper      | Deploys other malware                   |
| Worm         | Self-replicating network spread         |
| Backdoor     | Maintains remote access                 |
| RAT          | Remote Access Trojan                    |
| Wiper        | Data destruction                        |
| Stealer      | Information theft                       |
| Adware       | Unwanted advertising                    |
| Rootkit      | System concealment                      |
| Keylogger    | Records keystrokes                      |
| Bootkit      | Affects the boot process                |
| Hijacker     | Takes control of browser or application |
| FakeAV       | Fake antivirus software                 |
| Rogue        | Fake legitimate software for fraud      |
| Locker       | Locks the screen or device              |
| Injector     | Injects code into another process       |
| Sniffer      | Monitors network traffic                |
| Bypass       | Evades detection techniques             |
| Resurrector  | Self-recovers after being deleted       |
| FileInfector | Infects legitimate files                |
| Polymorph    | Self-modifies code to avoid detection   |
| Obfuscator   | Obfuscates code to hinder analysis      |
| Downloader   | Downloads additional payloads remotely  |
| Trojan       | Disguises as legitimate software        |
| Joker        | Tricks users with fake threats          |
| RogueModule  | Malicious plugin or extension           |
| C2           | Used as a Command-and-Control           |
| Loader       | Used to load other malware              |
| Packer       | Packed to avoid detection               |
| Scanner      | Scans for vulnerabilities               |

---

## Infection Vectors

| Code        | Infection Method                              |
| ----------- | --------------------------------------------- |
| Phish       | Phishing emails/websites                      |
| Exploit     | Software vulnerability exploitation           |
| Removable   | USB/removable devices                         |
| PUA         | Potentially Unwanted Applications             |
| DriveBy     | Malicious websites                            |
| NetShare    | Network shares                                |
| Social      | Social media platforms                        |
| IM          | Instant messaging apps                        |
| Watering    | Watering hole attacks                         |
| Supply      | Supply chain compromise                       |
| Brute       | Brute-force attacks                           |
| EmailAttach | Email attachments                             |
| FakeApp     | Fake apps in app stores                       |
| Torrent     | Peer-to-peer file sharing software            |
| Malvertise  | Malicious advertising                         |
| Preload     | Pre-installed (OEM, cracked OS)               |
| Script      | Malicious macros, PowerShell, JS, etc.        |
| DriveAuto   | Spreads via autorun.inf (legacy Windows)      |
| Unknown     | Vector not identified (needs deeper analysis) |
| None        | No self-propagation (manual install only)     |

---

> **Note:** This dictionary may be extended to support additional platforms, behaviors, or infection vectors. Pull requests are always welcome at the [official repository](https://github.com/memecoder123456/MDIS.git) ❤️
