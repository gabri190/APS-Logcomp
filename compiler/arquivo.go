// // // // //teste 1
// ball x_1 Point
// x_1 = UmpireAsk()

// UmpireCall(x_1)

// serve (x_1 > 1 && !!!(x_1 < 1)) || x_1 == 3 {
// 	x_1 = 2
// } 


// ball x Point = 3+6/3   *  2 -+-  +  2*4/2 + 0/1 -((6+ ((4)))/(2)) // Teste // Teste 2
// ball y_1 Point = 3
// y_1 = y_1 + x_1
// ball z__ Point
// z__ = x + y_1

// serve x_1 == 2 {
// 	x_1 = 2
// }

// serve x_1 == 3 {
// 	x_1 = 2
// } fault {
// 	x_1 = 3
// }

// set x_1 = 0; x_1 < 1 || x == 2; x_1 = x_1 + 1 {
// 	UmpireCall(x_1)
// } 



// // Saida final
// UmpireCall(x_1)
// UmpireCall(x)
// UmpireCall(z__+1)

// // All bool and Point operations
// ball y Point = 2
// ball z Point
// z = (y == 2)
// UmpireCall(y+z)
// UmpireCall(y-z)
// UmpireCall(y*z)
// UmpireCall(y/z)
// UmpireCall(y == z)
// UmpireCall(y < z)
// UmpireCall(y > z)

// // All str operations 
// ball a Match 
// ball b Match

// x_1 = 1 
// y = 1 
// z = 2
// a = "abc"
// b = "def"
// UmpireCall(a.b)
// UmpireCall(a.x_1)
// UmpireCall(x_1.a)
// UmpireCall(y.z)
// UmpireCall(a.(x_1==1))
// UmpireCall(a == a)
// UmpireCall(a < b)
// UmpireCall(a > b)

//teste 2
ball a Point
a = 5

serve a > 3 {
    a = 2
} fault {
    a = 7
}

UmpireCall(a)

// //teste 3
ball sum Point=0
set i = 1; i < 6 ; i = i + 1 {
	sum=sum+i
} 
UmpireCall(sum)

//teste 4
ball x Point = 3
ball y Point = 7
ball z Point

z = x + y
UmpireCall(z)

// //teste 5
ball num Point
num = 10

serve num > 5 {
    num = num * 2
} fault {
    num = num + 3
}

set i = 0; i < num; i=i+1 {
    UmpireCall(i)
}

//teste 6

ball str1 Match  
ball str2 Match 

str1 ="Hello "
str2 = "World"
UmpireCall(str1.str2)





