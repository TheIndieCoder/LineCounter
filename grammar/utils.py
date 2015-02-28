import re

class utils:

    @staticmethod
    def IsACommentedLine(strline = ""):
        match_ret = re.match("^#", strline)
        return True if match_ret else False

    @staticmethod
    def FineLineByPattern(strPattern = "", line_list = []):
        matched_line = ""
        for line in line_list:
            match_ret = re.match(strPattern, line)
            if match_ret:
                matched_line = line
                break
        return matched_line

    @staticmethod
    def GenerateRegexFromLine(strLine = str()):
        strRegex = str()
        strLineSplit = strLine.split()
        if strLineSplit[0] == 'LINE_START':
            strRegex = '^' + strLineSplit[1]
        else:
            strRegex = strLine
        return strRegex

    @staticmethod
    def GetGrammerBlocks(filehandle):
        grammer_list = []
        traversal_status = False
        # false -> No Active block
        # true -> Going through a block

        block = []
        for line in filehandle:
            if(not utils.IsACommentedLine(line)):
                start_ret = re.match("^START", line)

                if(start_ret):
                    traversal_status = True

                if(traversal_status == True):
                    block.append(line)

                    end_ret = re.match("^END", line)
                    if(end_ret):
                        traversal_status = False
                        grammer_list.append(list(block))
                        del block[:]

        return grammer_list

