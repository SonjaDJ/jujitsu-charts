import re

def getPhonetic(aString):
    """
        input: english-y transliterated japanese string
        output: phonetic version of string for text-to-speech to read
    """
    return multiple_replace(myWords,aString)

#http://stackoverflow.com/questions/15175142/how-can-i-do-multiple-substitutions-using-regex-in-python
def multiple_replace(di,te):
    te2=te.upper()
    regex=re.compile("(%s)" % "|".join(map(re.escape,di.keys())))
    return regex.sub(lambda x: di[x.string[x.start():x.end()]],te2)

#dictionary of replacements to use with multiple_replace
myWords={
    "KUBI":"COO BEE",
    "SODE":"SO DAY",
    "TSURIKOMI":"SUREY COMEY",
    "GOSHI":"GO SHE",
    "KUCHIKI TAOSHI":"COO CHEEKY TIE OH SHE",
    "KATA ASHI HISHIGI":"KAH TAH AH SHE HE SHE GHKAH TAH AH SHE HE SHE GHEE",
    "HADAKE":"HAH DAH CAH",
    "URAS":"OOH RAHS",
    "HITTSUI":"HIT SOO E",    
    "SUTEMI":"SUIT EMMY",    
    "TORI":"Tore-E",    
    "UDE":"OOH-Day",    
    "HAITTO":"High-toe",    
    "GEDAN":"GAYDON",    
    "BARAI":"BAR-EYE",    
    "TETTSUI":"TET SUE E",    
    "SHOTEI":"SHOW TAY",    
    "HAITO":"HI TOE",    
    "HIJI":"HEE GEE",    
    "OSOTO":"OH SOTO",    
    "IPPON":"EEP ON",    
    "SEOI":"SEE OY",    
    "SAKOTSU":"SUCK OAT SUE",    
    "UKI":"OOH KEY",    
    "UKE":"OOH KAY",    
    "(":"",    
    ")":"",    
    "GARI":"GAR E",    
    "FUMI":"FOOM E",    
    "KOMI":"COMB E",    
    "USHIRO":"OOH SHE ROW",    
    "GATAME":"GAH Tommy",    
    "HADAKA":"HAH Dacka",    
    "ASHI":"AH SHE",    
    "HISHIGI":"HE SHE Ghe",    
    "JIME":"GEE ME",    
    "KATA":"CAH TAH",    
    "MOROTE":"MORE OH TE",    
    "SAKE":"SAH KEY",    
    "NAGE":"NAH GAY",    
    "KAGE":"CAH GAY",    
    "AGE":"AH GAY",    
    " BOW":" BOUGH",    
    "TOMOE":"TOE MOE Ay",    
    "GURUMA":"GUR OOH MA",    
}

