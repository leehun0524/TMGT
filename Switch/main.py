from pymodbus.client import ModbusTcpClient
class Modbus_test:
    def __init__(self,ip="host.docker.internal",port=502,startaddress=1000,count=1,slave=1): #初始設定，把變數帶入
        self.ip = ip
        self.port = int(port)            #要設定成int不然下面帶入會產生錯誤(原本格式是str)
        self.startaddress = int(startaddress)
        self.count = int(count)
        self.slave = int(slave)     
    def toggle(self):
        client = ModbusTcpClient(self.ip,port=self.port)#(ip,port=port)是固定寫法
        #client.connect()  #好像這行有沒有都沒差
        respond = client.read_holding_registers(self.startaddress,self.count)#帶入數值，並把讀取的值寫入respond
        #print(respond)
        value=[] 
        value= respond.registers #把所有值丟入list
        #print(value)
        #print(respond.isError())
        if respond.isError():
            print("-----------讀取寄存器時發生錯誤-----------")
            return
        #for i in range (0,self.count): #把設定要改的位置到要幾位數做判斷並做切換
        #   rewrite=self.startaddress+i
        if value[0] == 1:
            write_response = client.write_register(self.startaddress,0)
        elif value[0] == 0:
            write_response = client.write_register(self.startaddress,1)
        
if __name__=='__main__':

    ModbusRead = Modbus_test()
    ModbusRead.toggle()