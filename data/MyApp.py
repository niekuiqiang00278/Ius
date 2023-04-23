# from data.base.Dmd import Dmd
# from data.base.rpc.KRpc import KRpc
from data.bis.JesBis import JesBis
# from data.bis.KemBis import KemBis
from data.bis.PdtBis import PdtBis
from data.plux.XActivity import XActivity
class MyApp(XActivity):
    def __init__(self):
        XActivity.__init__(self)

    def base(self):
        # Dmd()
        pass

    def bis(self):
        # self.kem = KemBis()
        self.jes = JesBis()
        self.pdt = PdtBis(self.jes.km2)

    def rpc(self):
        # self.k = KRpc()
        pass

if __name__ == '__main__':
    data = MyApp()
    data.pdt.pd0()
