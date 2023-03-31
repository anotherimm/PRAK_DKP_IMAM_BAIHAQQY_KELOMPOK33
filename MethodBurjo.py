class Pesanan:
    def __init__(self):
        self.__list__pesanan = []
        self.__total_pesanan = []

    def tambah_pesanan(self, menu):
        self.__list__pesanan.append(menu)
    
    def tambah_total(self, total):
        self.__total_pesanan.append(total)
 
    def total_pesanan(self):
        for i in range (len(self.__list__pesanan)):
            print(str(self.__total_pesanan[i]) + " " + self.__list__pesanan[i])
