# Copyright 2016 Carlos Gutierrez

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import ply.yacc as yacc
from php_lexer import tokens

VERBOSE = 1

def p_start(p):
    'start : top_statement_list'

def p_top_statement_list(p):
    '''top_statement_list : OPENTAG top_statement_list top_statement CLOSETAG top_statement_list
                            | top_statement
                            | empty'''
    pass

def p_top_statement(p):
    '''top_statement : statement
                     | function_declaration_statement
                     | class_declaration_statement
                     | empty'''
    pass

def p_top_statement_constant(p):
    'top_statement : CONST constant_declarations SEMI'
    pass

def p_constant_declarations(p):
	'''constant_declarations : constant_declarations COMMA constant_declaration
							 | constant_declaration'''
	pass

def p_constant_declaration(p):
    'constant_declaration : IDVAR EQUAL static_scalar'
    pass

def p_inner_statement_list(p):
    '''inner_statement_list : inner_statement_list inner_statement
                            | empty'''
    pass

def p_inner_statement(p):
    '''inner_statement : statement
                       | function_declaration_statement
                       | class_declaration_statement'''
    pass

def p_statement_if(p):
    'statement : IF LPAREN expr RPAREN LBLOCK statement RBLOCK elseif_list else_single'
                 #| IF LPAREN expr RPAREN COLON inner_statement_list new_elseif_list new_else_single ENDIF SEMI'''
    pass

def p_statement_while(p):
    'statement : WHILE LPAREN expr RPAREN while_statement'
    pass

def p_statement_do_while(p):
    'statement : DO statement WHILE LPAREN expr RPAREN SEMI'
    pass

def p_statement_for(p):
    'statement : FOR LPAREN for_expr SEMI for_expr SEMI for_expr RPAREN for_statement'
    pass

def p_statement_break(p):
    '''statement : BREAK SEMI
                 | BREAK expr SEMI'''
    pass

def p_statement_continue(p):
    '''statement : CONTINUE SEMI
                 | CONTINUE expr SEMI'''
    pass

def p_statement_return(p):
    '''statement : RETURN SEMI
                 | RETURN expr SEMI'''
    pass

def p_statement_global(p):
    'statement : GLOBAL global_var_list SEMI'
    pass

def p_statement_static(p):
    'statement : STATIC static_var_list SEMI'
    pass

def p_statement_echo(p):
    'statement : ECHO echo_expr_list SEMI'
    pass

def p_statement_expr(p):
    'statement : expr SEMI'
    pass

def p_statement_empty(p):
    'statement : SEMI'
    pass

def p_elseif_list(p):
    '''elseif_list : empty
                   | elseif_list ELSEIF LPAREN expr RPAREN LBLOCK statement RBLOCK
                   | elseif_list ELSEIF LPAREN expr RPAREN statement'''
    pass

def p_else_single(p):
    '''else_single : empty
                   | ELSE statement
                   | ELSE LBLOCK statement RBLOCK'''
    pass

def p_while_statement(p):
    'while_statement : statement'
                     #  | COLON inner_statement_list ENDWHILE SEMI'''
    pass

def p_for_expr(p):
    '''for_expr : empty
                | non_empty_for_expr'''
    pass

def p_non_empty_for_expr(p):
    '''non_empty_for_expr : non_empty_for_expr COMMA expr
                          | expr'''
    pass

def p_for_statement(p):
    'for_statement : statement'
                    # | COLON inner_statement_list ENDFOR SEMI'''
    pass

def p_global_var_list(p):
    '''global_var_list : global_var_list COMMA global_var
                       | global_var'''
    pass

def p_global_var(p):
    '''global_var : IDVAR
                  | variable'''
                 # | DOLLAR LBLOCK expr RBLOCK'''
    pass

def p_static_var_list(p):
    '''static_var_list : static_var_list COMMA static_var
                       | static_var'''
    pass

def p_static_var(p):
    '''static_var : IDVAR EQUAL static_scalar
                  | IDVAR'''
    pass

def p_echo_expr_list(p):
    '''echo_expr_list : echo_expr_list COMMA expr
                      | expr'''
    pass

def p_function_declaration_statement(p):
    'function_declaration_statement : FUNCTION ID LPAREN parameter_list RPAREN LBLOCK inner_statement_list RBLOCK'
    pass

def p_class_declaration_statement(p):
    'class_declaration_statement : class_entry_type ID LBLOCK class_statement_list RBLOCK'
    pass

def p_class_entry_type(p):
    'class_entry_type : CLASS'
                     #   | ABSTRACT CLASS
                     #   | FINAL CLASS'''
    pass

def p_class_statement_list(p):
    '''class_statement_list : class_statement_list class_statement
                            | empty'''
    pass

def p_class_statement(p):
    '''class_statement : FUNCTION ID LPAREN parameter_list RPAREN method_body
                       | class_variable_declaration SEMI
                       | class_constant_declaration SEMI'''
    pass

def p_class_variable_declaration(p):
    '''class_variable_declaration : class_variable_declaration COMMA IDVAR EQUAL static_scalar
                                  | IDVAR EQUAL static_scalar'''
    pass

def p_class_constant_declaration(p):
    '''class_constant_declaration : class_constant_declaration COMMA STRING EQUAL static_scalar
                                  | CONST IDVAR EQUAL static_scalar'''
    pass


def p_method_body(p):
    '''method_body : LBLOCK inner_statement_list RBLOCK
                   | SEMI'''
    pass

def p_parameter_list(p):
    '''parameter_list : parameter_list COMMA parameter
                      | parameter'''
    pass

def p_parameter(p):
    'parameter : IDVAR'
    pass

def p_expr_variable(p):
    'expr : variable'
    pass

def p_expr_assign(p):
    '''expr : variable EQUAL expr
            | variable EQUAL AND expr'''

def p_variable(p):
    '''variable : IDVAR
                | function_call'''
    pass

def p_function_call(p):
    'function_call : ID LPAREN function_call_parameter_list RPAREN'
    pass

def p_expr_scalar(p):
    'expr : scalar'
    pass

def p_scalar(p):
    'scalar : static_scalar'


def p_function_call_parameter_list(p):
    '''function_call_parameter_list : function_call_parameter_list COMMA function_call_parameter
                                    | function_call_parameter'''
    pass

def p_function_call_parameter_list_empty(p):
    'function_call_parameter_list : empty'
    pass

def p_function_call_parameter(p):
    'function_call_parameter : expr'
    pass

def p_expr_function(p):
    'expr : FUNCTION LPAREN parameter_list RPAREN'
    pass

def p_expr_assign_op(p):
    '''expr : variable PLUSEQUAL expr
            | variable MINUSEQUAL expr
            | variable LESSEQUAL expr
            | variable GREATEREQUAL expr'''
    pass

def p_expr_binary_op(p):
    '''expr : expr AND expr
            | expr ISEQUAL expr
            | expr OR expr
            | expr XOR expr
            | expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr'''
    pass

def p_expr_unary_op(p):
    '''expr : PLUS expr
            | MINUS expr
            | GREATER expr
            | LESS expr'''
    pass

def p_expr_print(p):
    'expr : PRINT expr'
    pass

def p_expr_group(p):
    'expr : LPAREN expr RPAREN'
    pass

def p_static_scalar(p):
    '''static_scalar : common_scalar
                     | STRING'''
                     #| QUOTES TEXT QUOTES'''
    pass

def p_common_scalar_number(p):
    'common_scalar : NUM'
    pass

def p_common_scalar_variable(p):
    'common_scalar : IDVAR'
    pass

def p_empty(p):
    'empty : '
    pass

def p_error(p):
    if VERBOSE:
        if p is not None:
            print chr(27)+"[1;31m"+"\t ERROR: Syntax error - Unexpected token" + chr(27)+"[0m"
            print "\t\tLine: "+str(p.lexer.lineno)+"\t=> "+str(p.value)
        else:
            print chr(27)+"[1;31m"+"\t ERROR: Syntax error"+chr(27)+"[0m"
            print "\t\tLine:  "+str(php_lexer.lexer.lineno)

    else:
        raise Exception('syntax', 'error')


parser = yacc.yacc()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        #print (scriptdata)

        print chr(27)+"[0;36m"+"INICIA ANALISIS SINTACTICO"+chr(27)+"[0m"
        parser.parse(scriptdata, tracking=False)
        #print("Hola bebe, no tienes errores sintacticos")
        print chr(27)+"[0;36m"+"TERMINA ANALISIS SINTACTICO"+chr(27)+"[0m"

    else:
        print chr(27)+"[0;31m"+"Pase el archivo de script PHP como parametro:"
        print chr(27)+"[0;36m"+"\t$ python php_parser.py"+chr(27)+"[1;31m"+" <filename>.php"+chr(27)+"[0m"
