import math,os

class VEKTOR_INFOS_3D:
    def __init__(self,r,s):
        self.r = r
        self.s = s
    
    def get_vektor_informationen(self):
        R = (self.r[0]+self.r[1]+self.r[2])
        S = (self.s[1]+self.s[1]+self.s[2])
        alpha,vektor_produkt_r,vektor_produkt_s,skalar_produkt = "","","",""
        if (R > 0):
            vektor_produkt_r = (math.sqrt(R))
            if (S > 0):
                vektor_produkt_s = (math.sqrt(S))
                skalar_produkt = (self.r[0]*self.s[0]+self.r[1]*self.s[1]+self.r[2]+self.s[2])
                winkel_zwischen_vektoren = ((skalar_produkt)/(vektor_produkt_r*vektor_produkt_s))
                if (winkel_zwischen_vektoren < 1):
                    alpha = math.acos(winkel_zwischen_vektoren)
                else:
                    alpha = "Mathematischer Fehler: Cosinus von Alpha ist %s°"%(winkel_zwischen_vektoren)
            else:
                vektor_produkt_s = "Mathematischer Fehler -> %s"%(S)
        else:
            vektor_produkt_r = "Mathematischer Fehler -> %s"%(R)
        return (alpha,vektor_produkt_r,vektor_produkt_s,skalar_produkt)

if __name__ == '__main__':
    os.system("cls") #Windows
    r = (2,-1,3) #Hier kann ein beliebiger Vektor eingesetzt werden (3D)
    s = (1,0,-1) #Hier kann ein beliebiger Vektor eingesetzt werden (3D)
    vektor_infos_3d = VEKTOR_INFOS_3D(r,s)
    (alpha, pr_r, pr_s, skalar_produkt) = vektor_infos_3d.get_vektor_informationen()
    print("Vektor r: (%s,%s,%s)"%(r[0],r[1],r[2]))
    print("Vektor s: (%s,%s,%s)"%(s[0],s[1],s[2]))
    print("Winkel zischen Vektoren: %s°"%(alpha))
    print("|r| = %s"%(pr_r))
    print("|s| = %s"%(pr_s))
    print("Skalarprodukt (r und s) = %s"%(skalar_produkt))

