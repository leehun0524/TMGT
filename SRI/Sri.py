#李俊緯碩論p.30
class SRI:
    def __init__(self,ct=3,dct=1,ddct=2): #初始設定，把變數帶入
         self.ct = ct
         self.dct = dct
         self.ddct = ddct
        
    def CAL_SRIe(self):
        if self.ct <= self.dct:
            Relsult_SRIe = 0.6 * self.ct/self.dct
        if self.ct > self.dct and self.ct <= self.ddct:
            Relsult_SRIe = 0.6 + 0.4 * self.ct/self.ddct
        if self.ct > self.ddct:
            Relsult_SRIe = 1
        print(Relsult_SRIe)
        
if __name__=='__main__':
    #ct是當前聚落能夠運用的能源(Copious Total, CT)
    #dct是運行最低限度時間的關鍵負載需求(Demand Critical Total, DCT)
    #ddct是和最高運行時間的主要關鍵負載需求(Dominant Demand Critical Total, DDCT)
    sys1=SRI()
    sys1.CAL_SRIe()