%{
#include "tennis.tab.h"  // Inclua o arquivo de cabeçalho gerado pelo Bison
%}

%%
"ball"          { return BALL; }
"Func"          { return FUNC; }
"Return"        { return TENNIS_RETURN; }
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
"Equal"         { return EQUAL; }
"NotEqual"      { return NOT_EQUAL; }
"Advantage"     { return ADVANTAGE; }
"Disadvantage"  { return DISADVANTAGE; }
"{"             { return '{'; }
"}"             { return '}'; }
"("             { return '('; }
")"             { return ')'; }
"=="            { return EQ; }
"!"            { return NEQ; }
">"             { return GT; }
"<"             { return LT; }
[ \t\n]         ; // Ignorar espaços em branco e novas linhas
.              { /* Capturar outros caracteres */ return yytext[0]; }

%%

int yywrap() {
    return 1;
}
