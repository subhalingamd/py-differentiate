from Differentiate import Expression

def test_00():
	assert Expression("(sin (2.0*x))").differentiate(wrt="x").toString() in ("(2.0*(cos (2.0*x)))","((cos (2.0*x))*2.0)")

def test_01():
	assert Expression("(ln (sin x))").differentiate(wrt="x").toString() in ("((cos x)*(1.0/(sin x))","((1.0/(sin x)*(cos x))","((cos x)/(sin x))","(cot x)")