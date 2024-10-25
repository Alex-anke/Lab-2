import xml.etree.ElementTree as ET


TREE = ET.parse('currency.xml')
ROOT = TREE.getroot()
VALUES = [float(valute.find('Value').text.replace(',', '.')) for valute in ROOT.findall('Valute')]
AVERAGE = sum(VALUES) / len(VALUES)


if __name__ == '__main__':
    print(f"Средний показатель Value: {AVERAGE}")