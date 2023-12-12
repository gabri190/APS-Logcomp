%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tennis.tab.h"
char* yyval;
%}
%option yylineno
%option noyywrap


%%
"ball"          { return BALL; }
"UmpireCall"    { return UMPIRE_CALL; }
"UmpireAsk"     { return UMPIRE_ASK; }
"Serve"         { return SERVE; }
"Fault"         { return FAULT; }
"Set"           { return SET; }
"Match"         { return MATCH; }
"Point"         { return POINT; }
"Equal"         { return EQ; }
">"             { return GT; }
"<"             { return LT; }
"{"             { return OPENK; }
"}"             { return CLOSEK; }
"("             { return LPAREN; }
")"             { return RPAREN; }
"=="            { return EQ; }
">"            { return GT; }
"<"            { return LT; }
"&&"            { return AND; }
"||"            { return OR; }
[ \t\n]         ; // Ignorar espaços em branco e novas linhas
.              { /* Capturar outros caracteres */ return yytext[0]; }

%%

