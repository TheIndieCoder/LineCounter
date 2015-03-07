
class token_interpreter:

    @staticmethod
    def Interpret(val=str()):
        interpreted_val =  {'LINE_START': '^',
                'LINE_END'      : '$',
                'ACHAR'         :   '[a-zA-Z ]',
                'ANY'           : '*',
                'NEW_LINE'      : '\\n'
                }.get(val)

        if interpreted_val is None:
            interpreted_val = val

        return interpreted_val

    @staticmethod
    def GenerateRegex(strLine = str()):
        strRegex = str()
        strLineSplit = strLine.split()

        if(strLineSplit[0] == 'LINE_END'):
            strRegex = token_interpreter.Interpret(strLineSplit[1])
            strRegex = strRegex + token_interpreter.Interpret('LINE_END')

        else:
            for token in strLineSplit:
                strRegex = strRegex + token_interpreter.Interpret(token)


        return strRegex