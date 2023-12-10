##  TennisScript - Uma Linguagem Inspirada no Tênis

TennisScript é uma linguagem de programação única que traz o mundo do tênis para a codificação. Se você é um entusiasta do tênis e adora programação, esta linguagem foi feita para você. Abaixo, descrevemos algumas das principais características sintáticas e semânticas que diferenciam o TennisScript de linguagens mais tradicionais

### Declaração de Variáveis:

Usamos o termo ball para declarar uma variável.

``` go
ball x Point = 3

```
### Estruturas Condicionais:
Usamos serve para o equivalente a "if" e fault para "else".

``` go
serve score > 3 {
    score = 2
} fault {
    score = 7
}

```
### Loops:
Usamos set para "for".

``` go
set (ball i = 0; i < 3; i++) {
    // Execute o loop três vezes
}
```
### Tipos de Dados:

- Match : Representa uma cadeia de caracteres.
- Point :  Representa um número inteiro.

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
PROGRAM = { STATEMENT };

BLOCK = { "{", "\n", STATEMENT, "}" };

STATEMENT = ( λ | FOR_LOOP | UMPIRE_CALL| ASSIGNMENT | IF_COND | COMMENT ), "\n";


TYPE = "Point" | "double" | "Match" | "bool";

FOR_LOOP = "Set", ":" , BEXPRESSION , ASSIGNMENT, BLOCK;

ASSIGNMENT = IDENTIFIER, "=", REXPRESSION;

IF_COND= "Serve", BEXPRESSION, BLOCK, {"Fault", BLOCK};

BEXPRESSION = BTERM, {("OR"), BTERM};

BTERM = REXPRESSION, {("AND"), REXPRESSION};

REXPRESSION = EXPRESSION, {("==" | ">" | "<"), EXPRESSION};

EXPRESSION = TERM, {("+" | "-" ), TERM};

TERM = FACTOR, {("*" | "/"), FACTOR };

FACTOR = (("+" | "-" | "!"), FACTOR | DIGIT | MATCH | BOOL | "(", EXPRESSION, ")" | IDENTIFIER | UMPIRE_ASK);

UMPIRE_CALL = "UmpireCall", "(",  BEXPRESSION , ")";

UMPIRE_ASK = "UmpireAsk", "(", ")"; //Comentarios : (type tem que estar em int no caso Point e antes ser declarado com o identifier )

COMMENT = "//", { Any valid character }, "\n";

TYPES_DEC = POINT | FLOAT | MATCH | BOOL;

POINT = DIGIT, { DIGIT };

FLOAT = DIGIT, { DIGIT }, ".", DIGIT, { DIGIT };

MATCH = "'", { Any valid character }, "'";

BOOL = "True" | "False";

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

LETTER = ( "a" | ... | "z" | "A" | ... | "Z" );

DIGIT = ( "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" );

Any valid character = Qualquer caractere válido, incluindo letras, números e caracteres especiais.



```
### Identificadores e tipos

``` shell
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
STRING = """, {LETTER | DIGIT}, """ ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
TYPE = ("Point", "Match");
```

### Observações:

Foi utilizado o compilador da disciplina e a partir dai houve adaptação para as características da linguagem e os testes realizados.
A seguir serão colocados exemplos de estruturas com a linguagem TennisScript.

### Compilação e saídas

Para compilar você pode ir até o diretorio "compiler" e entrar no diretório "tests" digitando o seguinte comando a seguir:

```shell
# No Diretório da APS
cd compiler\tests
```
Agora execute esse comando
```shell
python ..\main.py arquivo.tsc

```
Onde o "arquivo.tsc" pode ser substituido pelos arquivos que estão dentro da pasta tests e que serão apresentados como exemplo a seguir.

### Exemplos
Todos esses exemplos estão encaixados na extensão .tsc

#### input

```shell

ball x_1 Point
x_1 = UmpireAsk()

```

#### Declaração variaveis

```shell
# var_dec.tsc

ball x Point = 3
ball y Point = 7
ball z Point

z = x + y
UmpireCall(z)
```
Saída Esperada: 10

#### Condicionais

```shell
# cond.tsc

ball a Point
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

ball sum Point=0
set i = 1; i < 6 ; i = i + 1 {
sum=sum+i
} 
UmpireCall(sum)

```
Saída Esperada: 15

#### Strings

```shell
# str.tsc

ball str1 Match  
ball str2 Match 

str1 ="Hello "
str2 = "World"
UmpireCall(str1.str2)

```
Saída Esperada: Hello Word

#### Mix de estruturas

```shell
# mix.tsc

ball num Point
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







