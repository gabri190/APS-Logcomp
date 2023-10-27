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

- Ace  Representa um valor booleano, podendo ser in (true) ou out (false).
- Match Representa uma cadeia de caracteres.
- Point  Representa um número inteiro.
- Game  Representa um número de ponto flutuante.

### Equivalência Go e TennisScript
Println -> UmpireCall
var -> ball
Scanln -> UmpireAsk
string -> Match
int -> Point
bool -> Ace 
true-> in 
false -> out
float -> Game
if -> serve
else -> fault
for -> set


## Tarefa 1


### EBNF 


#### TennisScript EBNF

program ::= statement* ;

statement ::= declaration | assignment | umpire_call | umpire_ask | control_flow | expr ';' ;

declaration ::= 'ball' ID ':' type_value '=' expr ';' ;

assignment ::= ID '=' expr ';' ;

umpire_call ::= 'UmpireCall' '(' expr ')' ';' ;

umpire_ask ::= 'UmpireAsk' '(' ID ')' ';' ;

control_flow ::= serve_statement | set_loop ;

serve_statement ::= 'Serve' '(' expr ')' block ('Fault' block)? ;

set_loop ::= 'Set' '(' expr ';' expr ';' expr ')' block ;

block ::= '{' statement* '}' ;

expr ::= comparison (logical_op comparison)* ;

comparison ::= term (comparison_op term)* ;

term ::= factor (('Serve' | 'Return' | 'Rally') factor)* ;

factor ::= '(' expr ')' | ID | NUMBER | STRING ;

logical_op ::= '||' | '&&' ;

comparison_op ::= '==' | '!=' | '>' | '<' ;

type_value ::= 'Match' | 'Point' ;

ID ::= [a-zA-Z_][a-zA-Z0-9_]* ; (* Identificador *)

NUMBER ::= [0-9]+ ; (* Números inteiros *)

STRING ::= '"' .? '"' ; (* Strings, supondo que não haja escape para aspas duplas *)
