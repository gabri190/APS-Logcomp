class SymbolTable:
    def __init__(self):
        self.dic_var = {}

    def getter(self, var):
        if var in self.dic_var:
            return self.dic_var[var]
        else:
            raise NameError(f"Erro: variável não existente {var}")

    def setter(self, var, val, _type):
        if var in self.dic_var and self.dic_var[var][1] != _type:
            raise ValueError(f"Erro: Tipo de variável '{var}' não compatível.")
        self.dic_var[var] = (val, _type)

    def create(self, var, val=None, _type=None):
        if var in self.dic_var:
            raise ValueError(f"Variável '{var}' já existe.")
        else:
            self.dic_var[var] = (val, _type)
class FuncTable:
    table = {}

    def getter(self, func_key):
        return self.table[func_key]
    
    def setter(self, func_key, func_value):
        self.table[func_key] = func_value