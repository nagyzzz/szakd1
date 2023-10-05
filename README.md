# szakd1
A szakd1 egy olyan keretrendszer, melynek feladata a kezdő etikus hackerek munkájának segítése oly módon,
hogy néhány gyakran használt programot foglal magába és így a sérülékenységek vizsgálata és az adatgyűjtés
könnyebben áttekinthetővé válik.

## Kompatibilitás
[Kali Linux](https://www.kali.org/), [Parrot OS](https://www.parrotsec.org/), vagy bármely más disztró melyen fut az [Nmap](https://nmap.org/), [HashCat](https://hashcat.net/hashcat/) és a [John The Ripper](https://www.openwall.com/john/)

## Python
A kód futtatásához a [Python](https://www.python.org/) 3.10 verzióját használtam, ezért ezt vagy egy újabbat ajánlok.

```bash
sudo apt update && sudo apt upgrade -y

sudo apt install python3 python3-pip
```

## Szükséges csomagok telepítése
A szükséges csomagok telepítéséhez a pip package manager [pip](https://pip.pypa.io/en/stable/) a javasolt, de lehet PyCharm-ből is,
a Settings\Project\Python Interpreter menüpontban.

```bash
pip install PyQt5 PyQt5-Qt5 PyQt5-sips PyQt5-stubs decorator self setuptools unicode wheel
```

## Futtatás
A project mappában parancssorból:
```bash
python main
```
vagy PyCharmban megnyitva a projectet a main.py fájl futtatásával.
