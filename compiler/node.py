type_value=["int","string"]
from symboltable import FuncTable as ft
from symboltable import SymbolTable,FuncTable
global func_table

func_table = FuncTable()

class Node:
    def __init__(self):
        self.value = None
        self.children = []

    def evaluate(self, table):
        pass

class BinOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, table):
        # Avaliando os nós filhos uma única vez e armazenando os resultados
        left_result = self.children[0].evaluate(table)
        right_result = self.children[1].evaluate(table)

        left_value, left_type = left_result[0], left_result[1]
        right_value, right_type = right_result[0], right_result[1]
        

        # Operações Aritméticas
        if self.value in ['+', '-', '*', '/']:
            if left_type != type_value[0] or right_type != type_value[0]:
                raise ValueError("Erro: operações aritméticas requerem inteiros")
            if self.value == '+':
                return (left_value + right_value, type_value[0])
            elif self.value == '-':
                return (left_value - right_value, type_value[0])
            elif self.value == '*':
                return (left_value * right_value, type_value[0])
            elif self.value == '/':
                return (left_value // right_value, type_value[0])  # Divisão inteira

        # Operações Lógicas
        elif self.value in ['|', '&']:
            if left_type != type_value[0] or right_type != type_value[0]:
                raise ValueError("Erro: operações lógicas requerem inteiros")
            if self.value == '|':
                return (int(left_value or right_value), type_value[0])
            elif self.value == '&':
                return (int(left_value and right_value), type_value[0])

       # Operações de Comparação
        elif self.value in ['>', '<', '=']:
            if left_type != right_type:
                raise ValueError("Erro: tipos diferentes na comparação")
            if left_type not in type_value:
                raise ValueError(f"Erro: tipo '{left_type}' não suportado para comparação")
            if self.value == '>':
                return (int(left_value > right_value), type_value[0])
            elif self.value == '<':
                return (int(left_value < right_value), type_value[0])
            elif self.value == '=':
                return (int(left_value == right_value), type_value[0])

        # Concatenação
        elif self.value == '.':
            return (f'{str(left_value)}{str(right_value)}', type_value[1])
        else:
            raise ValueError(f"Operador desconhecido: {self.value}")

        
class UnOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, table):
        left_value=self.children[0].evaluate(table)[0]
        
        if self.value == '+':
            return (left_value,type_value[0])
        elif self.value == '-':
            return (-left_value,type_value[0])
        elif self.value=='!':
            return (not left_value,type_value[0])

class IntVal(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, table):
        return (self.value,type_value[0])
class StrVal(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, table):
        return (self.value,type_value[1])
class NoOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, table):
        pass

class AssignmentOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, table):
        result = self.children[1].evaluate(table)
        left_value = self.children[0].value
        right_value, _type = result[0], result[1]

        return table.setter(left_value, right_value, _type)
class PrintOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, table):
        left_value = self.children[0].evaluate(table)[0]
        print(left_value)


class IdentifierOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, table):
        return table.getter(self.value)

class BlockOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, table):
        for node in self.children:
            ret_val=node.evaluate(table)
            if ret_val:
                return ret_val
            
class ScanfOp(Node):
    def __init__(self, value, children, expected_type=None):
        self.value = value
        self.children = children
        self.expected_type = expected_type

    def evaluate(self, table):
        
        return (int(input()), type_value[0])


class ForOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
    def evaluate(self, table):
        self.children[0].evaluate(table)
        while(self.children[1].evaluate(table)[0]):
            self.children[3].evaluate(table)
            self.children[2].evaluate(table)

class IfOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
    def evaluate(self, table):
        if self.children[0].evaluate(table):
            self.children[1].evaluate(table)
        elif(len(self.children)>2):
            self.children[2].evaluate(table)
class VarDec(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, table):
        var_name = self.children[0].value
        
        if len(self.children) > 1:
            result = self.children[1].evaluate(table)
            val, _type = result[0], result[1]
            
            table.setter(var_name, val, _type)
        else:
            table.create(var_name, None, self.value)  # Modificamos esta linha para criar a variável sem um valor inicial.
class FuncDec(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, table):
        function_name = self.children[0].value
        
        function_value = self  # Certifique-se de que esta linha está correta

        if len(self.children) != 3:
            raise Exception("Error in function declaration")
        func_table.setter(function_name, (self.value,function_value))


class ReturnOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, table):
        return self.children[0].evaluate(table)

class FuncCall(Node):

    def __init__(self, value, children):
        self.value = value
        self.children = children  

    def evaluate(self, table):
       
        
        func_obj:FuncDec = func_table.getter(self.value)  
        if len(self.children) != len(func_obj[1].children[1]):
            raise Exception("Number of arguments from function declaration and function call differ")
        local_st=SymbolTable()
       
        for var_dec, var_value in zip(func_obj[1].children[1], self.children):
            var_dec.evaluate(local_st)
                                     # Eval dos vardec (coloca na nova st) [arg = VarDec]
            local_st.setter(var_dec.children[0].value, var_value.evaluate(table))  # Eval no escopo global
        return func_obj[1].children[2].evaluate(local_st)
        
       