from Differentiate import Expression

def test_constant():
	assert Expression("2008.0").differentiate(wrt="x").toString() == "0.0"

def test_diffvar():
	assert Expression("m").differentiate(wrt="x").toString() == "0.0"

def test_variable():
	assert Expression("x").differentiate(wrt="x").toString() == "1.0"

def test_add():
	assert Expression("(x+x)").differentiate(wrt="x").toString() == "(1.0+1.0)"

def test_subtract():
	assert Expression("(x-x)").differentiate(wrt="x").toString() == "(1.0-1.0)"

def test_multiply():
	assert Expression("(x*x)").differentiate(wrt="x").toString() == "(x+x)"

def test_multiply():
	assert Expression("(x/x)").differentiate(wrt="x").toString() == "((x-x)/(x^2.0))"

def test_sin():
	assert Expression("(sin x)").differentiate(wrt="x").toString() == "(cos x)"

def test_cos():
	assert Expression("(cos x)").differentiate(wrt="x").toString() == "(-(sin x))"

def test_tan():
	assert Expression("(tan x)").differentiate(wrt="x").toString() == "((sec x)^2.0)"

def test_sec():
	assert Expression("(sec x)").differentiate(wrt="x").toString() == "((sec x)*(tan x))"

def test_cosec():
	assert Expression("(cosec x)").differentiate(wrt="x").toString() in ("((-(cosec x))*(cot x))","(-((cosec x)*(cot x)))")

def test_cot():
	assert Expression("(cot x)").differentiate(wrt="x").toString() == "(-((cosec x)^2.0))"

def test_ln():
	assert Expression("(ln x)").differentiate(wrt="x").toString() == "(1.0/x)"

def test_pow():
	assert Expression("(x^2.0)").differentiate(wrt="x").toString() == "(2.0*x)"

