import re
import utils
import token_master

class e_block_type:
    NONE = 0
    LINE = 1

    @staticmethod
    def GetType(val=str()):
        return {'NONE' : e_block_type.NONE,
                'LINE' : e_block_type.LINE
                }.get(val)

class e_subblock_type:
    NONE                = 0
    PREPROCESSOR_DEF    = 1
    GEN_FUNCTION        = 2
    LOGICAL_LINE_OF_CODE= 3

    def GetType(val=str()):
        return {'NONE' : e_subblock_type.NONE,
                'PREPROCESSOR_DEF' : e_subblock_type.PREPROCESSOR_DEF,
                'GEN_FUNCTION' : e_subblock_type.GEN_FUNCTION,
                'LOGICAL_LINE_OF_CODE' : LOGICAL_LINE_OF_CODE
                }.get(val)

class grammar_block:
    def __init__(self):
        self.block_type = e_block_type.NONE
        self.block_sub_type = e_subblock_type.NONE
        self.start_regex = ""
        self.end_regex = ""
        self.has_next_line = True
        self.next_line_indicator = ''
        self.block_length = -1

    def Read(self, block_str = str()):
        self.block_length = len(block_str)
        assert(re.match("^START", block_str[0]))
        assert(re.match("^END", block_str[self.block_length -1]))
        self.ReadStart(block_str)
        self.ReadBody(block_str)
        self.ReadEnd(block_str)

    def ReadStart(self, block_str):
        start_line = block_str[0]
        start_line.split()

        index = 1
        for tokens in start_line[1:len(block_str)-1]:
            if index == 1:
                self.block_type = e_block_type.GetType(tokens)
            elif index == 2:
                self.block_sub_type = e_subblock_type.GetType(tokens)
            ++index

    def ReadBody(self, block):
        line_start = utils.utils.FineLineByPattern("^\tLINE_START", block[1:(self.block_length-1)])
        line_end = utils.utils.FineLineByPattern("^\tLINE_END", block[1:(self.block_length-1)])
        next_line = utils.utils.FineLineByPattern("^\tNEXT_LINE", block[1:(self.block_length-1)])
        indicator = utils.utils.FineLineByPattern("^\t\tINDICATOR", block[1:(self.block_length-1)])

        indicator_split = indicator.split()

        if len(indicator_split) == 2:
            self.next_line_indicator = indicator_split[1]

        print(self.next_line_indicator)

        self.start_regex = token_master.token_interpreter.GenerateRegex(line_start)
        self.end_regex = token_master.token_interpreter.GenerateRegex(line_end)

    def ReadEnd(self, block):
        pass

class grammar_reader:
    def __init__(self, filepath):
        self.grammar_block_lst = list()
        self.filepath = filepath
        self.str_block_list = list()

    def Read(self):
        grammar_file = open(self.filepath)
        self.str_block_list = utils.utils.GetGrammerBlocks(grammar_file)
        self.RetrieveFormats()

    def RetrieveFormats(self):
        for block_str in self.str_block_list:
            curr_block = grammar_block()
            curr_block.Read(block_str)
            self.grammar_block_lst.append(curr_block)




