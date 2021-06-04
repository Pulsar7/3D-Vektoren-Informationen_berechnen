import math,os

class VEKTOR_INFOS_3D:
    def __init__(self,r,s):
        self.r = r
        self.s = s
    
    def get_vektor_informationen(self):
        R = ((self.r[0])**2+(self.r[1])**2+(self.r[2])**2)
        S = ((self.s[1]**2)+(self.s[1])**2+(self.s[2])**2)
        alpha,vektor_betrag_r,vektor_betrag_s,skalar_produkt = "","","",""
        if (R > 0 and S > 0):
            vektor_betrag_r = (math.sqrt(R))
            vektor_betrag_s = (math.sqrt(S))
            skalar_produkt = (self.r[0]*self.s[0]+self.r[1]*self.s[1]+self.r[2]*self.s[2])
            quotient = ((skalar_produkt)/(vektor_betrag_r*vektor_betrag_s))
            vektor_betrag_r = "√%s"%(R)
            vektor_betrag_s = "√%s"%(S)
            if (quotient < 1):
                alpha = math.degrees(math.acos(quotient))
            else:
                alpha = "Mathematischer Fehler - Quotient = %s"%(quotient)
        else:
            if (R < 0):
                vektor_betrag_r = "Mathematischer Fehler -> %s"%(R)
            if (S < 0):
                vektor_betrag_s = "Mathematischer Fehler -> %s"%(S)
        return (alpha,vektor_betrag_r,vektor_betrag_s,skalar_produkt)

if __name__ == '__main__':
    os.system("cls") #Windows
    r = (1,3,-1)
    s = (6,2,-2)
    vektor_infos_3d = VEKTOR_INFOS_3D(r,s)
    (alpha, betrag_r,betrag_s,skalar_produkt) = vektor_infos_3d.get_vektor_informationen()
    print("""
    Vektor r      = (%s,%s,%s)
    Vektor s      = (%s,%s,%s)
    Alpha         = %s°
    |r|           = %s
    |s|           = %s
    Skalarprodukt = %s
    """%(r[0],r[1],r[2],s[0],s[1],s[2],alpha,betrag_r,betrag_s,skalar_produkt))

