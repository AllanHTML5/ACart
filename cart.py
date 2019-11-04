#SHOPPING CART R1 BY ALLANDEV
#LIST DEFINE SECTION
ProductList = []
PriceList = []
AmountList = []
TotalList = []

#MAIN CLASS SECTION

class Cart:
    def __init__(self, item, amount, price, cclient, shippingaddress, card, shippingcost):
        self.item = item
        self.price = price
        self.amount = amount
        self.cclient = cclient
        self.shippingaddress = shippingaddress
        self.card = card
        self.shippingcost = shippingcost
    def greetingmessage(self):
        print("-------------------------------------------------------")
        print("                SHOPPING CART ALSYSTEM R1")
        print("     DEVELOPED BY ALLANDEV, ALL RIGHTS RESERVED 2019")
        print("-------------------------------------------------------")
    def shippingcalc(self):
        self.cost = len((ProductList)*10)
    def clientinfoget(self):
        print("             INGRESE EL NOMBRE DEL CLIENTE:")
        print("-------------------------------------------------------")
        self.cclient = input()
        print("--------------------------------")
        print("INGRESE EL NÚMERO DE LA TARJETA:")
        print("--------------------------------")
        self.card = input()
        print("--------------------------------")
        print("INGRESE LA DIRECCIÓN DE ENVIO:")
        print("--------------------------------")
        self.shippingaddress = input()
    def dataget(self):
        print("--------------------------------")
        print("INGRESE EL NOMBRE DEL PRODUCTO:")
        print("--------------------------------")
        self.item = input()
        print("--------------------------------")
        print("INGRESE EL PRECIO DEL PRODUCTO:")
        print("--------------------------------")
        self.price = int(input())
        print("--------------------------------------")
        print("¿CUÁNTOS PRODUCTOS LLEVA DE ESTE TIPO?")
        print("--------------------------------------")
        self.amount = int(input())
    def listadder(self):
        ProductList.append(self.item)
        PriceList.append(self.price)
        AmountList.append(self.amount)
        self.eval1 = self.price * self.amount
        TotalList.append(self.eval1)
        self.totalamount = sum(TotalList)
    def listremover(self):
        print("-------------------------------------------------")
        print("INGRESE EL NOMBRE DEL PRODUCTO QUE DESEA REMOVER:")
        print("PRODUCTOS QUE LLEVA ACTUALENTE: ", ProductList)
        print("-------------------------------------------------")
        self.RemovalItem = input()
        print("-------------------------------------------------")
        print("INGRESE EL VALOR TOTAL DEL PRODUCTO REMOVIDO:")
        print("VALORES ACTUALES DEL TOTAL: ", TotalList)
        print("-------------------------------------------------")
        self.RemovalTotal = int(input())
        ProductList.remove(self.RemovalItem)
        TotalList.remove(self.RemovalTotal)
        if len(ProductList)>1 and len(ProductList)<3:
            ObjectI.dataprinterI()
        else:
            if len(ProductList)>2 and len(ProductList)<4:
                ObjectI.dataprinterII()
            else:
                if len(ProductList)>3 and len(ProductList)<5:
                    ObjectI.dataprinterIII()
                else:
                    ObjectI.dataprinter()
    def shippingchargeHN(self):
        self.chargeamount = 0
        TotalList.append(self.chargeamount)
    def shippingchargeELSE(self):
        self.equation = len((ProductList)*10)
        TotalList.append(self.equation)
    def dataprinter(self):
        self.cost = len((ProductList)*10)
        print("-------------------------------------------------------")
        print("                SHOPPING CART ALSYSTEM R1")
        print("     DEVELOPED BY ALLANDEV, ALL RIGHTS RESERVED 2019")
        print("-------------------------------------------------------")
        print("     Nombre del cliente: ", self.cclient)
        print("     últimos 4 dígitos de su tarjeta: ", self.card[-4:])
        print("     Dirección de Envio: ", self.shippingaddress)
        print("-------------------------------------------------------")
        print("                 PRODUCTOS QUE USTED LLEVA:")
        print("  NOMBRE    |    PRECIO    |   CANTIDAD    |    PRECIO TOTAL")
        print(" ", ProductList[0], "           ", PriceList[0], "           ", AmountList[0], "           ", TotalList[0])
        print("---------------------------------------------------------")
        print("        COSTO DEL ENVIÓ LOCAL CÓDIGO HN: GRATIS")
        print(" COSTO DEL ENVIÓ EXTERIOR: ", self.cost, "$/TIPO PRODUCTO.")
        print("---------------------------------------------------------")
        print("      EL TOTAL DE ESTA COMPRA:", (sum(TotalList)))
        print("---------------------------------------------------------")
    def dataprinterI(self):
        self.cost = len((ProductList)*10)
        print("-------------------------------------------------------")
        print("                SHOPPING CART ALSYSTEM R1")
        print("     DEVELOPED BY ALLANDEV, ALL RIGHTS RESERVED 2019")
        print("-------------------------------------------------------")
        print("     Nombre del cliente: ", self.cclient)
        print("     últimos 4 dígitos de su tarjeta: ", self.card[-4:])
        print("     Dirección de Envio: ", self.shippingaddress)
        print("-------------------------------------------------------")
        print("                 PRODUCTOS QUE USTED LLEVA:")
        print("  NOMBRE    |    PRECIO    |   CANTIDAD    |    PRECIO TOTAL")
        print(" ", ProductList[0], "           ", PriceList[0], "           ", AmountList[0], "           ", TotalList[0])
        print(" ", ProductList[1], "           ", PriceList[1], "           ", AmountList[1], "           ", TotalList[1])
        print("---------------------------------------------------------")
        print("        COSTO DEL ENVIÓ LOCAL CÓDIGO HN: GRATIS")
        print(" COSTO DEL ENVIÓ EXTERIOR: ", self.cost, "$/TIPO PRODUCTO.")
        print("---------------------------------------------------------")
        print("      EL TOTAL DE ESTA COMPRA:", (sum(TotalList)))
        print("---------------------------------------------------------")
    def dataprinterII(self):
        self.cost = len((ProductList)*10)
        print("-------------------------------------------------------")
        print("                SHOPPING CART ALSYSTEM R1")
        print("     DEVELOPED BY ALLANDEV, ALL RIGHTS RESERVED 2019")
        print("-------------------------------------------------------")
        print("     Nombre del cliente: ", self.cclient)
        print("     últimos 4 dígitos de su tarjeta: ", self.card[-4:])
        print("     Dirección de Envio: ", self.shippingaddress)
        print("-------------------------------------------------------")
        print("                 PRODUCTOS QUE USTED LLEVA:")
        print("  NOMBRE    |    PRECIO    |   CANTIDAD    |    PRECIO TOTAL")
        print(" ", ProductList[0], "           ", PriceList[0], "           ", AmountList[0], "           ", TotalList[0])
        print(" ", ProductList[1], "           ", PriceList[1], "           ", AmountList[1], "           ", TotalList[1])
        print(" ", ProductList[2], "           ", PriceList[2], "           ", AmountList[2], "           ", TotalList[2])
        print("---------------------------------------------------------")
        print("        COSTO DEL ENVIÓ LOCAL CÓDIGO HN: GRATIS")
        print(" COSTO DEL ENVIÓ EXTERIOR: ", self.cost, "$/TIPO PRODUCTO.")
        print("---------------------------------------------------------")
        print("      EL TOTAL DE ESTA COMPRA:", (sum(TotalList)))
        print("---------------------------------------------------------")
    def dataprinterIII(self):
        self.cost = len((ProductList)*10)
        print("-------------------------------------------------------")
        print("                SHOPPING CART ALSYSTEM R1")
        print("     DEVELOPED BY ALLANDEV, ALL RIGHTS RESERVED 2019")
        print("-------------------------------------------------------")
        print("     Nombre del cliente: ", self.cclient)
        print("     últimos 4 dígitos de su tarjeta: ", self.card[-4:])
        print("     Dirección de Envio: ", self.shippingaddress)
        print("-------------------------------------------------------")
        print("                 PRODUCTOS QUE USTED LLEVA:")
        print("  NOMBRE    |    PRECIO    |   CANTIDAD    |    PRECIO TOTAL")
        print(" ", ProductList[0], "           ", PriceList[0], "           ", AmountList[0], "           ", TotalList[0])
        print(" ", ProductList[1], "           ", PriceList[1], "           ", AmountList[1], "           ", TotalList[1])
        print(" ", ProductList[2], "           ", PriceList[2], "           ", AmountList[2], "           ", TotalList[2])
        print(" ", ProductList[3], "           ", PriceList[3], "           ", AmountList[3], "           ", TotalList[3])
        print("---------------------------------------------------------")
        print("        COSTO DEL ENVIÓ LOCAL CÓDIGO HN: GRATIS")
        print(" COSTO DEL ENVIÓ EXTERIOR: ", self.cost, "$/TIPO PRODUCTO.")
        print("---------------------------------------------------------")
        print("      EL TOTAL DE ESTA COMPRA:", (sum(TotalList)))
        print("---------------------------------------------------------")

#OBJECT SECTION
ObjectI = Cart("Allan", 36, 5, "AllanDev", "Tegucigalpa", 254545645446, 1523135)
ObjectI.greetingmessage()
ObjectI.clientinfoget()
ObjectI.dataget()
ObjectI.listadder()
#IFS SECTION
print("--------------------------------------")
print("     ¿DESEA AGREGAR OTRO PRODUCTO?"    )
print("YES=1 <--------SELECCIÓN--------> NO=2")
print("--------------------------------------")
ANSWER=int(input())
while ANSWER==1:
    ObjectI.dataget()
    ObjectI.listadder()
    print("--------------------------------------")
    print("     ¿DESEA AGREGAR OTRO PRODUCTO?"    )
    print("YES=1 <--------SELECCIÓN--------> NO=2")
    print("--------------------------------------")
    ANSWER=int(input())
else:
    if len(ProductList)>1:
        print("--------------------------------------")
        print("  ¿DESEA REMOVER ALGÚN PRODUCTO?")
        print("YES=1 <--------SELECCIÓN--------> NO=2")
        print("--------------------------------------")
        removalchoice = int(input())
        if removalchoice==1 and len(ProductList)>1:
            ObjectI.listremover()
        else:
            print("--------------------------------------")
            print("  ¿LE GUSTARÍA ENVIAR ESTE PRODUCTO?"  )
            print("YES=1 <--------SELECCIÓN--------> NO=2")
            print("--------------------------------------")
            shippingchoice = int(input())
            if shippingchoice==1:
                print("------------------------------------------")
                print("  INGRESE SU CÓDIGO DE PAÍS PARA EL ENVÍO  ")
                print("       EJEMPLO DE CÓDIGO DE PAÍS: US")
                print("------------------------------------------")
                shippingcountry = input()
                if shippingcountry=="HN":
                    ObjectI.shippingchargeHN()
                    if len(ProductList)==2:
                        ObjectI.dataprinterI()
                    else:
                        if len(ProductList)==3:
                            ObjectI.dataprinterII()
                        else:
                            if len(ProductList)==4:
                                ObjectI.dataprinterIII()
                            else:
                                if len(ProductList)==1:
                                    ObjectI.dataprinter()
                else:
                    ObjectI.shippingchargeELSE()
                    if len(ProductList)>1 and len(ProductList)<3:
                        ObjectI.dataprinterI()
                    else:
                        if len(ProductList)>2 and len(ProductList)<4:
                            ObjectI.dataprinterII()
                        else:
                            if len(ProductList)>3 and len(ProductList)<5:
                                ObjectI.dataprinterIII()
                            else:
                                ObjectI.dataprinter()
    else:
        if len(ProductList)>1 and len(ProductList)<3:
            ObjectI.dataprinterI()
        else:
            if len(ProductList)>2 and len(ProductList)<4:
                ObjectI.dataprinterII()
            else:
                if len(ProductList)>3 and len(ProductList)<5:
                    ObjectI.dataprinterIII()
                else:
                    ObjectI.dataprinter()