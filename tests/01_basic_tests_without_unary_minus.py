from Differentiate import Expression

def test_var():
	assert Expression("(0.0-x)").differentiate(wrt="x").toString(allow_unary_minus=False) == "(0.0-1.0)"

def test_cot():
	assert Expression("(cot x)").differentiate(wrt="x").toString(allow_unary_minus=False) == "(0.0-((cosec x)^2.0))"

