%{
#include <stdio.h>
#include <stdlib.h>
%}

%token SERVE FAULT RALLY BALL UMPIRE_CALL UMPIRE_ASK MATCH POINT OR AND EQ NEQ GT LT
%token ID NUMBER STRING

%type <expr> expr
%type <block> block
%type <stmt_list> statement_list

%start program

%%

program : statement_list ;

statement_list : /* vazia */ { $$ = NULL; }
               | statement_list statement { /* lógica para lidar com a lista de declarações */ }
               ;

statement : declaration
          | assignment
          | func_call
          | umpire_call
          | umpire_ask
          | control_flow
          | expr
          ;

declaration : BALL ID ':' type_value '=' expr ';' { /* Implemente a lógica para lidar com declarações */ } ;

assignment : ID '=' expr ';' { /* Implemente a lógica para lidar com atribuições */ } ;

umpire_call : UMPIRE_CALL '(' expr ')' ';' { /* Implemente a lógica para lidar com chamadas de Umpire */ } ;

umpire_ask : UMPIRE_ASK '(' ID ')' ';' { /* Implemente a lógica para lidar com perguntas ao Umpire */ } ;

control_flow : serve_statement
             | rally_loop
             | set_loop
             ;

serve_statement : SERVE '(' expr ')' block FAULT block { /* Implemente a lógica para lidar com estruturas 'serve' e 'fault' */ } ;

rally_loop : RALLY '(' expr ')' block { /* Implemente a lógica para lidar com loops 'rally' */ } ;

set_loop : RALLY '(' expr ';' expr ';' expr ')' block { /* Implemente a lógica para lidar com loops 'rally' */ } ;

block : '{' statement_list '}' { /* Implemente a lógica para lidar com blocos */ } ;

expr : comparison OR comparison { /* Implemente a lógica para lidar com expressões 'or' */ } ;

comparison : term EQ term | NEQ term | GT term | LT term { /* Implemente a lógica para lidar com comparações */ } ;

term : factor AND factor { /* Implemente a lógica para lidar com expressões lógicas 'and' */ } ;

factor : '{' expr '}' { /* Implemente a lógica para lidar com blocos aninhados */ }
       | ID { /* Implemente a lógica para lidar com identificadores */ }
       | NUMBER { /* Implemente a lógica para lidar com números */ }
       | STRING { /* Implemente a lógica para lidar com strings */ }
       | func_call { /* Implemente a lógica para lidar com chamadas de função */ };

func_call : ID '(' expr ')' { /* Implemente a lógica para lidar com chamadas de função */ };

type_value : MATCH | POINT { /* Implemente a lógica para lidar com tipos de valores */ };

%%
