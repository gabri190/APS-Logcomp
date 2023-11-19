%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);

// Undefine yywrap to avoid conflicts
#undef yywrap
#define yywrap() 0
%}

%token SERVE FAULT RALLY BALL LPAREN RPAREN LCOLCHETE RCOLCHETE UMPIRE_CALL UMPIRE_ASK GAME ACE IN OUT VOLLEY SET MATCH POINT OR AND EQ NEQ GT LT
%token ID NUMBER STRING

%%

program : statement ;

statement : declaration
          | assignment
          | umpire_call
          | umpire_ask
          | control_flow
          | expr
          ;

declaration : BALL ID ':' type_value '=' expr ';' { /* Implemente a lógica para lidar com declarações */ } ;

assignment : ID '=' expr ';' { /* Implemente a lógica para lidar com atribuições */ } ;

umpire_call : UMPIRE_CALL LPAREN expr RPAREN ';' { /* Implemente a lógica para lidar com chamadas de Umpire */ } ;

umpire_ask : UMPIRE_ASK LPAREN ID RPAREN ';' { /* Implemente a lógica para lidar com perguntas ao Umpire */ } ;

control_flow : serve_statement
             | rally_loop
             ;

serve_statement : SERVE LPAREN expr RPAREN block FAULT block { /* Implemente a lógica para lidar com estruturas 'serve' e 'fault' */ } ;

rally_loop : RALLY LPAREN expr RPAREN block { /* Implemente a lógica para lidar com loops 'rally' */ } ;

block : LCOLCHETE statement RCOLCHETE { /* Implemente a lógica para lidar com blocos */ } ;

expr : comparison OR comparison { /* Implemente a lógica para lidar com expressões 'or' */ } ;

comparison : term EQ term | term NEQ term | term GT term | term LT term | term AND term { /* Implemente a lógica para lidar com comparações e 'and' */ } ;

term : factor AND factor { /* Implemente a lógica para lidar com expressões lógicas 'and' */ } ;

factor : LPAREN expr RPAREN { /* Implemente a lógica para lidar com blocos aninhados */ }
       | ID { /* Implemente a lógica para lidar com identificadores */ }
       | NUMBER { /* Implemente a lógica para lidar com números */ }
       | STRING { /* Implemente a lógica para lidar com strings */ }
       ;


type_value : MATCH { /* Implemente a lógica para lidar com MATCH type */ }
           | POINT { /* Implemente a lógica para lidar com POINT type */ }
           ;

%%

void yyerror(const char *s) {
    extern int yylineno;
    extern char *yytext;

    /* mensagem de erro exibe o símbolo que causou erro e o número da linha */
    printf("\nErro (%s): símbolo \"%s\" (linha %d)\n", s, yytext, yylineno);
}

int main() {
    yyparse();
    return 0;
}
