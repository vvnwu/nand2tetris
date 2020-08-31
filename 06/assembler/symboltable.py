class SymbolTable:
    def __init__(self):
        self.table = {
             'SP' : bin(0),
             'LCL': bin(1),
             'ARG': bin(2),
             'THIS': bin(3),
             'THAT': bin(4),
             'R0': bin(0),
             'R1': bin(1),
             'R2': bin(2),
             'R3': bin(3),
             'R4': bin(4),
             'R5': bin(5),
             'R6': bin(6),
             'R7': bin(7),
             'R8': bin(8),
             'R9': bin(9),
             'R10': bin(10),
             'R11': bin(11),
             'R12': bin(12),
             'R13': bin(13),
             'R14': bin(14),
             'R15': bin(15),
             'SCREEN': bin(16384),
             'KBD': bin(24576),
         }
    
    def addEntry(self, str, address):
        self.table[str] = address

    def contains(self, str):
        return getattr(self.table,str,None) != None

    def GetAdress(self,str):
        return self.table[str]
