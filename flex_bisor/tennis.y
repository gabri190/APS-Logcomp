%OPENK
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);

// Undefine yywrap to avoid conflicts
#undef yywrap
#define yywrap() 0
%CLOSEK

%token SERVE FAULT RALLY BALL LPAREN RPAREN OPENK CLOSEK UMPIRE_CALL UMPIRE_ASK SET MATCH POINT OR AND EQ NEQ GT LT 
%token ID NUMBER STRING

%%

program : statement ;

block  = OPENK NEWLINE statement CLOSEK ;

statement : λ 
          | FOR_LOOP 
          | UMPIRE_CALL
          | ASSIGNMENT 
          | IF_COND 
          | COMMENT
          , NEWLINE ;

type_value : MATCH OPENK /* Implemente a lógica para lidar com MATCH type */ CLOSEK
           | POINT OPENK /* Implemente a lógica para lidar com POINT type */ CLOSEK
           ;

for_loop = "Set", ":" , bexpression , assignment, block;

assignment = identifier, "=", rexpression;

IF_COND= "Serve", BEXPRESSION, BLOCK, OPENK"Fault", BLOCKCLOSEK;

bexpression = bterm, OPENK("OR"), btermCLOSEK;

bterm = rexpression, OPENK("AND"), rexpressionCLOSEK;

rexpression = expression, OPENK(EQ | GT | LT), expressionCLOSEK;

expression = term, OPENK("+" | "-" ), termCLOSEK;

term = factor, OPENK("*" | "/"), factor CLOSEK;

factor = (("+" | "-" | NEQ), factor | DIGIT | MATCH | BOOL | LPAREN, EXPRESSION, RPAREN | IDENTIFIER | UMPIRE_ASK);

UMPIRE_CALL : UMPIRE_CALL LPAREN expr RPAREN ;
UMPIRE_ASK : UMPIRE_ASK LPAREN ID RPAREN  ;

comment = "//", OPENK Any valid character CLOSEK, "\n";

types_dec = POINT | FLOAT | MATCH | BOOL;

POINT = DIGIT, OPENK DIGIT CLOSEK;

FLOAT = DIGIT, OPENK DIGIT CLOSEK, ".", DIGIT, OPENK DIGIT CLOSEK;

MATCH = "'", OPENK Any valid character CLOSEK, "'";

BOOL = "True" | "False";

IDENTIFIER = LETTER, OPENK LETTER | DIGIT | "_" CLOSEK;

LETTER = ( "a" | ... | "z" | "A" | ... | "Z" );

DIGIT = ( "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" );


%%

void yyerror(const char *s) OPENK
    extern int yylineno;
    extern char *yytext;

    /* mensagem de erro exibe o símbolo que causou erro e o número da linha */
    printf("\nErro (%s): símbolo \"%s\" (linha %d)\n", s, yytext, yylineno);
CLOSEK

int main() OPENK
    yyparse();
    return 0;
CLOSEK
