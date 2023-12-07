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
- Println -> UmpireCall
- var -> ball
- Scanln -> UmpireAsk
- string -> Match
- int -> Point
- if -> serve
- else -> fault
- for -> set

## Tarefa 1


### EBNF 


#### TennisScript EBNF
```shell
program ::= statement* ;

statement ::= variable_declaration | assignment | function_call | function_declaration | tennis_return_statement | umpire_call | umpire_ask | control_flow | expr ;

variable_declaration ::= 'ball' ID ':' tennis_type '=' expr ;

assignment ::= ID '=' expr ';' ;

function_call ::= ID '(' expr ')' ;

function_declaration ::= 'Func' ID '(' params ')' block ;

tennis_return_statement ::= 'TennisReturn' expr ';' ;

params ::= ID (',' ID)* ;

umpire_call ::= 'UmpireCall' '(' expr ')' ;

umpire_ask ::= 'UmpireAsk' '(' ID ')' ;

control_flow ::= serve_statement | rally_loop ;

serve_statement ::= 'Serve' '(' expr ')' block ('Fault' block)? ;

rally_loop ::= 'Rally' '(' expr ')' block ;

block ::= '{' statement* '}' ;

expr ::= comparison (tennis_logical_op comparison)* ;

comparison ::= term (tennis_comparison_op term)* ;

term ::= factor (('Serve' | 'TennisReturn' | 'Rally') factor)* ;

factor ::= '(' expr ')' | ID | NUMBER | STRING ;

tennis_logical_op ::= 'Ace' | 'Volley' ;

tennis_comparison_op ::= 'Equal' | 'NotEqual' | 'Advantage' | 'Disadvantage' ;

tennis_type ::= 'Match' | 'Point' | 'Game' | 'Ace' ;

ID ::= [a-zA-Z_][a-zA-Z0-9_]* ; (* Identificador *)

NUMBER ::= [0-9]+ ; (* Números inteiros *)

STRING ::= '"' [^"]* '"' ; (* Strings, sem escape para aspas duplas *)

```

### Observarções:

Foi utilizado o compilador da disciplina e a partir dai houve adaptação para as características da linguagem e os testes realizados.
A seguir serão colocados exemplos de estruturas com a linguagem TennisScript.

### Exemplos
Todos esses exemplos estão encaixados na extensão .tsc
#### Declaração variaveis

```shell
# var_dec.tsc

ball x int = 3
ball y int = 7
ball z int

z = x + y
UmpireCall(z)
```
Saída Esperada: 10

#### Condicionais

```shell
# cond.tsc

ball a int
a = 5

serve a > 3 {
    a = 2
} fault {
    a = 7
}

UmpireCall(a)
```
Saída Esperada: 2 

#### Loop

```shell
# loop.tsc

ball sum int=0
set i = 1; i < 6 ; i = i + 1 {
sum=sum+i
} 
UmpireCall(sum)

```
Saída Esperada: 15

#### Strings

```shell
# str.tsc

ball str1 string  
ball str2 string 

str1 ="Hello "
str2 = "World"
UmpireCall(str1.str2)

```
Saída Esperada: Hello Word

#### Mix de estruturas

```shell
# mix.tsc

ball num int
num = 10
serve num > 5 {
num = num * 2
} fault {
    num = num + 3
}

set i = 0; i < num; i=i+1 {
    UmpireCall(i)
}
```
Saída Esperada: 
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19







