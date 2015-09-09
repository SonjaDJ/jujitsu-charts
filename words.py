import re

def replaceWords(astr):
    """
    Replace the romanized japanese with phoenetic english that 'say' can pronounce
    """
    tempStr=astr.upper()
    tempStr=re.sub("SUTEMI","SUIT-EMMY",tempStr)    
    tempStr=re.sub("TORI","Tore-E",tempStr)    
    tempStr=re.sub("UDE","OOH-Day",tempStr)    
    tempStr=re.sub("HAITTO","High-toe",tempStr)    
    tempStr=re.sub("GEDAN","GAYDON",tempStr)    
    tempStr=re.sub("BARAI","BAR-EYE",tempStr)    
    tempStr=re.sub("TETTSUI","TET SUE E",tempStr)    
    tempStr=re.sub("SHOTEI","SHOW TAY",tempStr)    
    tempStr=re.sub("HAITO","HI TOE",tempStr)    
    tempStr=re.sub("HIJI","HEE GEE",tempStr)    
    tempStr=re.sub("OSOTO","OH SOTO",tempStr)    
    tempStr=re.sub("IPPON","EEP ON",tempStr)    
    tempStr=re.sub("SEOI","SEE OY",tempStr)    
    tempStr=re.sub("SAKOTSU","SUCK OAT SUE",tempStr)    
    tempStr=re.sub("UKI","OOH KEY",tempStr)    
    tempStr=re.sub("UKE","OOH KAY",tempStr)    
    tempStr=re.sub("\(","",tempStr)    
    tempStr=re.sub("\)","",tempStr)    
    tempStr=re.sub("GARI","GAR E",tempStr)    
    tempStr=re.sub("FUMI","FOOM E",tempStr)    
    tempStr=re.sub("KOMI","COMB-E",tempStr)    
    tempStr=re.sub("USHIRO","OOH-SHE ROW",tempStr)    
    tempStr=re.sub("GATAME","GAH-Tommy",tempStr)    
    tempStr=re.sub("HADAKA","HAH-Dacka",tempStr)    
    tempStr=re.sub("ASHI","AH-SHE",tempStr)    
    tempStr=re.sub("HISHIGI","HE-SHE Ghe",tempStr)    
    tempStr=re.sub("JIME","GEE-ME",tempStr)    
    tempStr=re.sub("KATA","CAH-TAH",tempStr)    
    tempStr=re.sub("MOROTE","MORE OH-TAY",tempStr)    
    tempStr=re.sub("SAKE","SAH-KEY",tempStr)    
    tempStr=re.sub("NAGE","NAH-GAY",tempStr)    
    tempStr=re.sub("BOW","BOUGH",tempStr)    
    tempStr=re.sub("TOMOE","TOE-MOE Ay",tempStr)    
    tempStr=re.sub("GURUMA","GUR-OOH MA",tempStr)    
    retstr=re.sub("GERI","GARY",tempStr)    
    #print retstr
    return retstr
