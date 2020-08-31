from assembler_parser import Parser
from code import Code
from symboltable import SymbolTable
import sys


def main():
    print("hello world")
    #print(format(5,'b:5.'))
    # print(bin(5))
    # print('{0:5.b}'.format(5))
    st = SymbolTable()
    filename = 'C:\\Users\\wuviv\\OneDrive\\Documents\\nand2tetris\\nand2tetris\projects\\06\\add\\Add.asm'#sys.argv[0]
    filenameout = 'test.hack'#sys.argv[1]

    first_pass(st,filename)
    second_pass(st,filename,filenameout)
    

def first_pass(st, filename):
    parser = Parser(filename)
    instcount = 0
    st_entry = ''

    while(parser.hasMoreCommands()):
        parser.advance()
        if parser.commandType() == None:
            continue
        elif parser.commandType() == 'L_COMMAND':
            st_entry = parser.symbol()
        else:
            if st_entry != '':
                st.addEntry(st_entry,instcount)
            instcount+=1


def second_pass(st,filename,filenameout):
    parser = Parser(filename)
    writefile = open(filenameout,'w')
    code = Code()
    st_add = 1024

    while(parser.hasMoreCommands()):
        parser.advance()
        if parser.commandType() == 'A_COMMAND':
            if parser.isSymbolConst():
                writefile.write('0'+format(parser.symbol(),'b')+'\n')
            else:
                if not st.contains(parser.symbol()):
                    st.addEntry(parser.symbol(),format(st_add,'b'))
                    st_add+=1
                print('0'+st.GetAdress(parser.symbol()))
                writefile.write('0'+st.GetAdress(parser.symbol())+'\n')
        if parser.commandType() == 'C_COMMAND':
            comp = code.comp(parser.comp())
            dst = code.dest(parser.dest())
            jmp = code.jump(parser.jump())
            print('111'+parser.AorM()+comp+dst+jmp)
            writefile.write('111'+comp+dst+jmp+'\n')

if __name__ == "__main__":
    main()