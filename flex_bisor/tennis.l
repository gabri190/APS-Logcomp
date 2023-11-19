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
"Rally"         { return RALLY; }
"Set"           { return SET; }
"Match"         { return MATCH; }
"Point"         { return POINT; }
"Game"          { return GAME; }
"Ace"           { return ACE; }
"in"            { return IN; }
"out"           { return OUT; }
"Volley"        { return VOLLEY; }
"Equal"         { return EQ; }
"NotEqual"      { return NEQ; }
">"             { return GT; }
"<"             { return LT; }
"{"             { return LCOLCHETE; }
"}"             { return RCOLCHETE; }
"("             { return LPAREN; }
")"             { return RPAREN; }
"=="            { return EQ; }
"!="            { return NEQ; }
">="            { return GT; }
"<="            { return LT; }
"&&"            { return AND; }
"||"            { return OR; }
[ \t\n]         ; // Ignorar espaços em branco e novas linhas
.              { /* Capturar outros caracteres */ return yytext[0]; }

%%

