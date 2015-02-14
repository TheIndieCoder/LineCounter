import sys
sys.path.insert(0, '.\grammar')

import grammar_reader

if __name__ == '__main__':
    cpp_grmreader = grammar_reader.grammar_reader(".\cpp_basic.grm")
    cpp_grmreader.Read()
    pass