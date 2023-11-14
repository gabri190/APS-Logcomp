import os
from node import *
from tokenizer import *
from filter import PrePro
from symboltable import SymbolTable

class Parser:
    tokenizer:Tokenizer
    
    @staticmethod
    def parseFactor():
        tokens = Parser.tokenizer
        if tokens.next.type == 'INT':
            result = IntVal(tokens.next.value, [])
            tokens.selectNext()
            return result
        elif tokens.next.type == 'STRING':
            result = StrVal(tokens.next.value, [])
            tokens.selectNext()
            return result
        elif tokens.next.type in ('PLUS', 'MINUS', 'NOT'):
            operator = tokens.next.type
            tokens.selectNext()
            factor = Parser.parseFactor()
            if operator == 'PLUS':
                return UnOp('+', [factor])
            elif operator == 'MINUS':
                return UnOp('-', [factor])
            elif operator == 'NOT':
                return UnOp('!', [factor])
        elif tokens.next.type == 'LPAREN':
            tokens.selectNext()
            result = Parser.boolexpression()
            if tokens.next.type != 'RPAREN':
                raise ValueError("Esperado fechamento de parênteses")
            tokens.selectNext()
            return result
        elif tokens.next.type == 'Scanln':
            tokens.selectNext()
            if tokens.next.type != 'LPAREN':
                raise ValueError(f"erro Lparen {tokens.next.type}")
            tokens.selectNext()
            if tokens.next.type != 'RPAREN':
                raise ValueError(f"Esperado ')' após 'Scanln'")
            tokens.selectNext()
            return ScanfOp("Scanln", [])
        elif tokens.next.type == 'IDENTIFIER':
            identifier_name = IdentifierOp(tokens.next.value, [])
            tokens.selectNext()
            
            if tokens.next.type == 'LPAREN':
                call_node = FuncCall(identifier_name.value, [])
                tokens.selectNext()
                
                if tokens.next.type != 'RPAREN':
                    while tokens.next.type != 'RPAREN':
                        arg = Parser.boolexpression()
                        call_node.children.append(arg)
                        if tokens.next.type != 'RPAREN':
                            if tokens.next.type != 'COMMA':
                                raise ValueError(f"FuncCall expected ',' or ')' and got {tokens.next.type}")
                            tokens.selectNext()
                
                tokens.selectNext()  # Consumir o token 'RPAREN'
                result = call_node
            else:
                result = identifier_name
        else:
            raise ValueError(f"Unexpected token {tokens.next.type}")

        return result

    @staticmethod
    def boolexpression():
        tokens=Parser.tokenizer
        result=Parser.boolTerm()
        while tokens.next.type in ('OR'):
            operator=tokens.next.type
            tokens.selectNext()
            bterm=Parser.boolTerm()
            if operator =='OR':
                result=BinOp('|',[result,bterm])
        return result

    @staticmethod
    def boolTerm():
        tokens=Parser.tokenizer
        result=Parser.relExpression()
        while tokens.next.type in ('AND'):
            operator=tokens.next.type
            tokens.selectNext()
            rexpression=Parser.relExpression()
            if operator =='AND':
                result=BinOp('&',[result,rexpression])
        return result
    
    @staticmethod
    def relExpression():
        tokens=Parser.tokenizer
        result = Parser.parseExpression()
        while tokens.next.type in ('EQUAL', 'GREATER','LESS'):
            operator = tokens.next.type
            tokens.selectNext()
            expression = Parser.parseExpression()
            if operator == 'EQUAL':
                result = BinOp('=', [result, expression])
            elif operator=='GREATER':
                result = BinOp('>', [result, expression])
            elif operator=='LESS':
                result=BinOp('<', [result, expression])
        return result


    @staticmethod
    def parseTerm():
        tokens=Parser.tokenizer
        result = Parser.parseFactor()
        while tokens.next.type in ('MULTI', 'DIV'):
            operator = tokens.next.type
            tokens.selectNext()
            factor = Parser.parseFactor()
            if operator == 'MULTI':
                result = BinOp('*', [result, factor])
            else:
                result = BinOp('/', [result, factor])
        return result

    @staticmethod
    def parseExpression():
        tokens=Parser.tokenizer
        result = Parser.parseTerm()

        while tokens.next.type in ('PLUS', 'MINUS','CONCAT'):
            operator = tokens.next.type
            tokens.selectNext()
            term = Parser.parseTerm()
            if operator == 'PLUS':
                result = BinOp('+', [result, term])
            elif operator == 'MINUS':
                result = BinOp('-', [result, term])
            elif operator == 'CONCAT':
                result = BinOp('.', [result, term])

        return result

    @staticmethod
        
    def parseAssignment():
        tokens = Parser.tokenizer
        
        if tokens.next.type == 'IDENTIFIER':
            ident = IdentifierOp(tokens.next.type,[])
            tokens.selectNext()
            if tokens.next.type == "ASSIGN":
                tokens.selectNext()
                val = Parser.boolexpression()
                result = AssignmentOp(None, [ident, val])
            
            elif tokens.next.type == "LPAREN":
                call_node = FuncCall(ident.value, [])
                tokens.selectNext()
                if tokens.next.type != "RPAREN":
                    while True:
                        ret_val = Parser.boolexpression()
                        call_node.children.append(ret_val)
                        if tokens.next.type == "RPAREN":
                            break
                        if tokens.next.type != "COMMA":
                            raise Exception("Arguments must be separated by commas")
                        tokens.selectNext()
                result = call_node
                tokens.selectNext()
            else:
                raise Exception ("Identifier error")
        
        return result

    @staticmethod
    def parseBlock():
        tokens = Parser.tokenizer
        statements=[]
        if tokens.next.type != 'OPENK':
            raise ValueError(f"erro openk {tokens.next.type}")
        tokens.selectNext()
        
        if tokens.next.type != 'NEWLINE':
            raise ValueError(f"erro newline {tokens.next.type}")
        tokens.selectNext()
        
        while tokens.next.type != 'CLOSEK':
            statement = Parser.parseStatement()
            statements.append(statement)
        tokens.selectNext()
        
        return BlockOp(None, statements)

        
    @staticmethod
    def parseProgram():
        tokens = Parser.tokenizer
        statements = []
        while tokens.next.type != 'EOF':
            statements.append(Parser.parseDeclaration())
        return BlockOp("Block", statements)

    @staticmethod
    def parseDeclaration():
        tokens = Parser.tokenizer
        while tokens.next.type == 'NEWLINE':
            tokens.selectNext()
        if tokens.next.type != 'func':
            raise ValueError(f"Esperado 'func' como palavra-chave, recebido '{tokens.next.type}'")
        tokens.selectNext()

        if tokens.next.type != 'IDENTIFIER':
            raise ValueError(f"Esperado identificador para o nome da função, recebido '{tokens.next.type}'")
        func_name = tokens.next.value
        tokens.selectNext()

        if tokens.next.type != 'LPAREN':
            raise ValueError(f"Esperado '(' após o nome da função, recebido '{tokens.next.type}'")
        tokens.selectNext()

        args = []
        while tokens.next.type != 'RPAREN':
            if tokens.next.type != 'IDENTIFIER':
                raise ValueError(f"Esperado nome do parâmetro, recebido '{tokens.next.type}'")
            param_name = tokens.next.value
            tokens.selectNext()

            if tokens.next.type != 'type_value':
                raise ValueError(f"Esperado tipo do parâmetro após '{param_name}', recebido '{tokens.next.type}'")
            param_type = tokens.next.value
            tokens.selectNext()

            args.append((param_name, param_type))

            if tokens.next.type == 'COMMA':
                tokens.selectNext()

        tokens.selectNext()  

        if tokens.next.type != 'type_value':
            raise ValueError(f"Esperado tipo de retorno para a função '{func_name}', recebido '{tokens.next.type}'")
        return_type = tokens.next.value
        tokens.selectNext()

        body = Parser.parseBlock()

        if tokens.next.type != 'NEWLINE':
            raise ValueError(f"Esperado uma nova linha após o bloco da função, recebido '{tokens.next.type}'")
        tokens.selectNext()

        return FuncDec(return_type, [IdentifierOp(func_name, []), args, body])

    @staticmethod
    def parseStatement():
        tokens=Parser.tokenizer
        statement=NoOp(0,[])
        
        if tokens.next.type == 'IDENTIFIER':
            statement = Parser.parseAssignment()
        
        elif tokens.next.type == 'Println':
            tokens.selectNext()
            if tokens.next.type != 'LPAREN':
                raise ValueError("erro LPAREN")
            tokens.selectNext()
            expression = Parser.boolexpression()
            if tokens.next.type != 'RPAREN':
                raise ValueError(f"Esperado {tokens.next.type} após PRINT statement")
            tokens.selectNext()
            statement= PrintOp("Println", [expression])
        
        elif tokens.next.type == 'if':
            tokens.selectNext()
            cond=Parser.boolexpression()
            blk=Parser.parseBlock()
            if tokens.next.type=='else':
                tokens.selectNext()
                statement= IfOp("else",[cond,blk,Parser.parseBlock()])
            else:
                statement= IfOp("if",[cond,blk])
            
        elif tokens.next.type=='for':
            tokens.selectNext()
            assign=Parser.parseAssignment()
            if tokens.next.type!='ENDC':
                raise ValueError(f"erro endc {tokens.next.type}")
            tokens.selectNext()
            expression=Parser.boolexpression()
            if tokens.next.type!='ENDC':
                raise ValueError(f"erro endc {tokens.next.type}")
            tokens.selectNext()
            statement= ForOp("value",[assign,expression,
                                Parser.parseAssignment(),
                                Parser.parseBlock()])     
        
        elif tokens.next.type=='var':
            tokens.selectNext()
            if tokens.next.type!="IDENTIFIER":
                raise ValueError(f"erro iden, {tokens.next.type}")
            identificador=IdentifierOp(tokens.next.value,[])
            tokens.selectNext()
            
            if tokens.next.type !='type_value':
                raise ValueError(f"erro type, {tokens.next.type}")
            type_val=tokens.next.value
            tokens.selectNext()
            
            if tokens.next.type=='ASSIGN':
                tokens.selectNext()
                statement= VarDec(type_val,[identificador,Parser.boolexpression()])
            else:
                statement= VarDec(type_val,[identificador])   
        
        elif tokens.next.type=='return':
            tokens.selectNext()
            expression=Parser.boolexpression()
            statement=ReturnOp(None,[expression])
           
        if tokens.next.type != "NEWLINE" :
            raise ValueError(f"erro newline,{tokens.next.type}")
        tokens.selectNext()
        
        return statement
        
    @staticmethod
    def run(code):
        filtered_code = PrePro.filter(code)
        Parser.tokenizer = Tokenizer(filtered_code)
        root = Parser.parseProgram()
        table = SymbolTable()
        result = root.evaluate(table)
        return result