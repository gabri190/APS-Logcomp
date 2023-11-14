%{
#include <stdio.h>
#include <stdlib.h>
%}

%token SERVE FAULT SET BALL UMPIRE_CALL UMPIRE_ASK MATCH POINT OR AND EQ NEQ GT LT
%token ID NUMBER STRING

%%

program : statement_list ;

statement_list : statement
               | statement_list statement ;

statement : declaration
          | assignment
          | umpire_call
          | umpire_ask
          | control_flow
          | expr ;

declaration : BALL ID ':' type_value '=' expr ';' { /* Implemente a lógica para lidar com declarações */ } ;

assignment : ID '=' expr ';' { /* Implemente a lógica para lidar com atribuições */ } ;

umpire_call : UMPIRE_CALL '(' expr ')' ';' { /* Implemente a lógica para lidar com chamadas de Umpire */ } ;

umpire_ask : UMPIRE_ASK '(' ID ')' ';' { /* Implemente a lógica para lidar com perguntas ao Umpire */ } ;

control_flow : serve_statement
             | set_loop ;

serve_statement : SERVE '(' expr ')' block FAULT block { /* Implemente a lógica para lidar com estruturas 'serve' e 'fault' */ } ;

set_loop : SET '(' expr ';' expr ';' expr ')' block { /* Implemente a lógica para lidar com loops 'set' */ } ;

block : '{' statement_list '}' ;

expr : comparison OR comparison ;

comparison : term EQ term | NEQ term | GT term | LT term { /* Implemente a lógica para lidar com comparações */ } ;

term : factor AND factor { /* Implemente a lógica para lidar com expressões lógicas 'and' */ } ;

factor : '{' expr '}' | ID | NUMBER | STRING ;

type_value : MATCH | POINT ;

%%

int main() {
    yyparse();
    return 0;
}
