##  TennisScript - Uma Linguagem Inspirada no Tênis

TennisScript é uma linguagem de programação única que traz o mundo do tênis para a codificação. Se você é um entusiasta do tênis e adora programação, esta linguagem foi feita para você. Abaixo, descrevemos algumas das principais características sintáticas e semânticas que diferenciam o TennisScript de linguagens mais tradicionais

### Declaração de Variáveis:

Usamos o termo ball para declarar uma variável.

``` go
ball score = 15;

```
### Estruturas Condicionais:
Usamos serve para o equivalente a "if" e fault para "else".

``` go
serve (score == 15) {
    // Código a ser executado se o placar for 15
} fault {
    // Código a ser executado caso contrário
}

```
### Loops:
Usamos rally para "while" e set para "for".

``` go
rally (score < 40) {
    // Continue o loop enquanto o placar for menor que 40
}

set (ball i = 0; i < 3; i++) {
    // Execute o loop três vezes
}
```
### Tipos de Dados:

Para tipos de dados, usamos single (inteiros), double (flutuantes), string (cadeias de caracteres) e os booleanos são representados como in (verdadeiro) e out (falso).

## Tarefa 1


### EBNF 


#### TennisScript EBNF


program     ::= statement* ;

statement   ::= var_decl 
              | conditional 
              | loop 
              | assignment 
              | expr ';' ;

var_decl    ::= 'ball' ID '=' expr ';' ;

assignment  ::= ID '=' expr ';' ;

conditional ::= 'serve' '(' expr ')' block fault_block? ;

block       ::= '{' statement* '}' ;

fault_block ::= 'fault' block ;

loop        ::= while_loop | for_loop ;

while_loop  ::= 'rally' '(' expr ')' block ;

for_loop    ::= 'set' '(' var_decl_or_assign expr ';' expr ')' block ;

var_decl_or_assign ::= var_decl | assignment ;

expr        ::= term (('+' | '-') term)* ;

term        ::= factor (('*' | '/') factor)* ;

factor      ::= '(' expr ')' 
              | ID 
              | NUMBER 
              | STRING 
              | boolean ;

boolean     ::= 'in' | 'out' ;

ID          ::= [a-zA-Z_][a-zA-Z0-9_]* ;  (* Identificador *)

NUMBER      ::= [0-9]+ ('.' [0-9]+)? ;    (* Números inteiros e flutuantes *)

STRING      ::= '"' .*? '"' ;              (* Strings, supondo que não haja escape para aspas duplas *)

