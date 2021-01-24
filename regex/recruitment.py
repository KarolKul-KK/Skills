import re

Text1 = '''HRB 12 286 -- 20. 12. 2001: Beispiel Corp GmbH, Wiesbaden.
Hans Wundertoll ist zum Vorsitzenden des Vorstandes ernannt.
Prokura zusammenmit einem Prokuristen oder mit einem Vorstandsmitglied: Udo Martin, 19. 03. 1945, 51234 Mainz; Frank Fischer, 01. 01. 1960,
32340 Oberaula; Eckart Gärtner, 27. 12. 1967, 55127 Mainz'''

Text2 ='''HRB 12286: Beispiel Zwei AG, Kormoranstarsse 5, 65244 Wiesbaden.
Bestelltals Vorstand: Mathias, Tanja, Ober(Taunus), *04.05.1973; Dr. Jung, Ole, Wiesbaden, *27.08.1999.'''

def integer_finder(integer):
    """This function finds all number commercial register numbers."""

    crm = re.findall(r"[A-Z]\w+\s\d{2}.?\d{3}", integer)
    print('Commercial register numbers:',crm)

integer_finder(Text1)

def string_finder(string):
    '''This function finds all strings what we need'''
    company = re.findall(r"[A-Z]\w+\s[A-Z]\w+\s[A-Z]\w+", string)
    people = re.findall(r"([A-Z]\w+.?\s[A-Z]\w+[,]\s.?)(\d\d.\s?\d\d.\s?\d{4}.\s\d{5}\s[A-Z]\w+|[A-Z]\w+.?[A-Z]?\w+.?[,]\s.\d{2}.\d{2}.\d{4})", string)
    print('Company:', company)
    print('People: ', people)

string_finder(Text2)
