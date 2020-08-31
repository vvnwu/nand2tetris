from code import Code
class Parser:
    def __init__(self,filename):
        self.input_file = open(filename,'r').readlines()
        self.currline =""
        self.index = -1

    def hasMoreCommands(self):
        return self.index < (len(self.input_file)-1)

    def advance(self):
        code = Code()
        self.index+=1
        print(self.index)
        print(self.input_file[self.index])
        self.currline = self.input_file[self.index]
        print(self.commandType())
        if self.commandType() == 'C_COMMAND':
            print('dest: ' + self.dest() + ' ' + code.dest(self.dest()))
            print('comp: ' + self.comp() + ' ' + code.comp(self.comp()))
            print('jump: ' + self.jump() + ' ' + code.jump(self.jump()))
        print('----------------')
    
    def commandType(self):
        if self.currline[0] == '@':
            return 'A_COMMAND'
        elif self.currline[0] == '(':
            return 'L_COMMAND'
        elif self.currline.strip()[0:2] == '//' or not self.currline.strip():
            return None
        else:
            return 'C_COMMAND'

    def symbol(self):
        if self.commandType() == 'A_COMMAND':
            return self.currline[1:]
        elif self.commandType() == 'L_COMMAND':
            return self.currline[1:-1]
        else:
            return None

    def isSymbolConst(self):
        return self.symbol().isdigit()

    def AorM(self):
        return '1' if self.comp().find('M') != -1 else '0'
    
    def dest(self):
        loc = self.currline.find('=')
        return 'null' if loc == -1 else self.currline[0:loc].strip()
    
    def comp(self):
        if self.dest() != 'null':
            return self.currline.split('=')[1].strip()
        elif self.jump() != 'null':
            return self.currline.split(';')[0].strip()
    
    def jump(self):
        loc = self.currline.find(';')
        return 'null' if loc == -1 else self.currline[loc:].strip()
        