%{
#include "tennis.tab.h"  // Inclua o arquivo de cabeçalho gerado pelo Bison
%}

%%
"Serve"          { return SERVE; }
"Fault"          { return FAULT; }
"Set"            { return SET; }
"ball"           { return BALL; }
"UmpireCall"     { return UMPIRE_CALL; }
"UmpireAsk"      { return UMPIRE_ASK; }
"Match"          { return MATCH; }
"Point"          { return POINT; }
"||"             { return OR; }
"&&"             { return AND; }
"=="             { return EQ; }
"!="             { return NEQ; }
">"              { return GT; }
"<"              { return LT; }
[ \t\n]          ; // Ignorar espaços em branco e novas linhas
.               { /* Capturar outros caracteres */ return yytext[0]; }

%%

int yywrap() {
    return 1;
}
