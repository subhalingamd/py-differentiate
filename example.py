from Differentiate import Expression

EXPR=["((((x^2.0)+4.0)/x)^((x*(2.0*m))-24.0))","((x*2.0)*(((x^2.0)+6.0)/m))","(((x^3.0)+(5.0*x))^((sin x)^2.0))"]
WRT=["x","m"]

for wrt in WRT:
	for expr in EXPR:
		print("Input :\n"+expr)
		e=Expression(expr)
		f=e.differentiate(wrt=wrt)
		print("Output : (w.r.t. "+wrt+")")
		res = f.toString(echo=True)
		print()
	print()

