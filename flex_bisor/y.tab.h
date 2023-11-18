/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    SERVE = 258,                   /* SERVE  */
    FAULT = 259,                   /* FAULT  */
    RALLY = 260,                   /* RALLY  */
    BALL = 261,                    /* BALL  */
    UMPIRE_CALL = 262,             /* UMPIRE_CALL  */
    UMPIRE_ASK = 263,              /* UMPIRE_ASK  */
    MATCH = 264,                   /* MATCH  */
    POINT = 265,                   /* POINT  */
    OR = 266,                      /* OR  */
    AND = 267,                     /* AND  */
    EQ = 268,                      /* EQ  */
    NEQ = 269,                     /* NEQ  */
    GT = 270,                      /* GT  */
    LT = 271,                      /* LT  */
    ID = 272,                      /* ID  */
    NUMBER = 273,                  /* NUMBER  */
    STRING = 274                   /* STRING  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif
/* Token kinds.  */
#define YYEMPTY -2
#define YYEOF 0
#define YYerror 256
#define YYUNDEF 257
#define SERVE 258
#define FAULT 259
#define RALLY 260
#define BALL 261
#define UMPIRE_CALL 262
#define UMPIRE_ASK 263
#define MATCH 264
#define POINT 265
#define OR 266
#define AND 267
#define EQ 268
#define NEQ 269
#define GT 270
#define LT 271
#define ID 272
#define NUMBER 273
#define STRING 274

/* Value type.  */


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
