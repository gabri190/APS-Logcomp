%OPENK
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);

// Undefine yywrap to avoid conflicts
#undef yywrap
#define yywrap() 0
%CLOSEK

%token SERVE FAULT RALLY BALL LPAREN RPAREN OPENK CLOSEK UMPIRE_CALL UMPIRE_ASK SET MATCH POINT BOOL FLOAT OR AND EQ NEQ GT LT 
%token IDENTIFIER NUMBER STRING

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

type_value : MATCH 
           | POINT 
           ;

FOR_LOOP = "Set", ":" , bexpression , ASSIGNMENT, block;

ASSIGNMENT = identifier, "=", rexpression;

IF_COND= "Serve", BEXPRESSION, BLOCK, OPENK "Fault", BLOCK CLOSEK;

bexpression = bterm, OPENK ("OR"), bterm CLOSEK;

bterm = rexpression, OPENK ("AND"), rexpression CLOSEK;

rexpression = expression, OPENK (EQ | GT | LT), expression CLOSEK;

expression = term, OPENK ("+" | "-" ), term CLOSEK;

term = factor, OPENK ("*" | "/"), factor CLOSEK;

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
