# Differentiate fully parenthesised binary expressions
# 	By Subhalingam D

##	 NUMBERS SHOULD BE ENTERED WITH ATLEAST ONE DECIMAL ZERO.
#### 	E.G. 2019.0 instead of 2019

##	ONLY BINARY OPERATORS ALLOWED WITH COMPLETE PARENTHESIS
####    E.G. '0.0-x' instead of '-x'

class Expression:

	def __init__(self,S,Nd = None):
		if (Nd):
			self.expr = Nd
		else:
			(e,n) = self.parse(S)
			self.expr = e

	class Node:
		def __init__(self,d):
			self.left = None
			self.right = None
			self.data = d
		
		# Convert into string
		def toString(self):
			if (self.left and self.right):
				left = self.left.toString()
				right = self.right.toString()
				opr = self.data
				return "(" + left + opr + right + ")"
			else:
				return self.data

	# Print the expression tree as it is if allow_unary_minus=False
	# Remove 0.0 before - if allow_unary_minus=True
	#   Other extra identities are removed while making the tree itself
	def toString(self,allow_unary_minus=True,echo=False):
		s = self.expr.toString()
		if echo:
			if allow_unary_minus:
				i=0
				while i < len(s):
					if s[i:i+5]=="(0.0-":
						print(s[i],end="")
						s=s[:i+1]+s[i+4:]
						i+=1
					
					print(s[i],end="")
					i+=1
				print(end="\n")
			else:
				print(s)
				
		else:
			if (allow_unary_minus):
				i=0
				while i < len(s):
					if s[i:i+5]=="(0.0-":
						s=s[:i+1]+s[i+4:]
						i+=1
					
					i+=1
				
		return s
		
	# Parsing
	#	if S[0]=='(', there is subexpression
	#	if S[0] isdigit() then the subexpression is digit
	#	if S[0] isalpha() then some character
	#	else Exception("Invalid input")
	def parse(self,S):
		l = len(S)
		if (S[0] == "("):
			(left,n) =  self.parse(S[1:l-2])
			opr = S[n+1]
			(right,m) = self.parse(S[n+2:l-1])
			expr = self.Node(opr)
			expr.left = left
			expr.right = right
			return (expr,n+m+3)
		elif S[0].isdigit():
			i = 0
			while ((i < l) and (S[i].isdigit() or (S[i] == "."))):
				i = i+1
			num = S[0:i]
			expr = self.Node(num)
			return (expr,i)
		elif S[0].isalpha():
			i = 0
			while ((i < l) and S[i].isalpha()):
				i = i+1
			var = S[0:i]
			expr = self.Node(var)
			return (expr,i)
		else:
			raise Exception("Invalid input")

	# if expr.data[0] isdigit() then True else False
	def constant(self):
		if self.expr.data[0].isdigit():
			return True
		else:
			return False

	# if expr.data[0] isalpha() then True else False
	def variable(self):
		if self.expr.data[0].isalpha():
			return True
		else:
			return False

	# if expr.data = x then True (same variable found wrt which to differentiate) else False
	def samevariable(self,x):
		if (self.expr.data == x):
			return True
		else:
			return False


	# For the following functions: (To check operators)
	# if expr.data=op, then True else  False

	# for sum, op='+'
	def sum(self):
		if (self.expr.data == '+'):
			return True
		else:
			return False

	# for difference, op='-'
	def diff(self):
		if (self.expr.data == '-'):
			return True
		else:
			return False

	# for multiplication, op='*'
	def prod(self):
		if (self.expr.data == '*'):
			return True
		else:
			return False	

	# for division, op='/'
	def div(self):
		if (self.expr.data == '/'):
			return True
		else:
			return False

	# for power, op='^'
	def exp(self):
		if (self.expr.data == '^'):
			return True
		else:
			return False



	# For the following functions: (To check functions)
	# if expr.left.data=fn, then True else  False

	# for natural log, fn='ln'	
	def log_e(self):
		if (self.expr.left.data=="ln"):
			return True
		else:
			return False

	# for sine, fn='sin'	
	def sin(self):
		if (self.expr.left.data=="sin"):
			return True
		else:
			return False

	# for cosine, fn='cos'	
	def cos(self):
		if (self.expr.left.data=="cos"):
			return True
		else:
			return False

	# for tangent, fn='tan'	
	def tan(self):
		if (self.expr.left.data=="tan"):
			return True
		else:
			return False

	# for secant, fn='sec'	
	def sec(self):
		if (self.expr.left.data=="sec"):
			return True
		else:
			return False

	# for cosecant, fn='cosec'	
	def cosec(self):
		if (self.expr.left.data=="cosec"):
			return True
		else:
			return False

	# for cotangent, fn='cot'	
	def cot(self):
		if (self.expr.left.data=="cot"):
			return True
		else:
			return False	




	# To get left and eight expressions
	def leftExpression(self):
		left = self.expr.left
		return Expression("",left)

	def rightExpression(self):
		right = self.expr.right
		return Expression("",right)



	# The following functions make the expression tree for +,-,*,/,^,ln & trigonometric functions
	# Details on identities in Documentation attached

	def makesum(self,e1,e2):
		if e1.expr.toString()=="0.0":
			return Expression("",self.Node(e2.expr.toString()))
		elif e2.expr.toString()=="0.0":
			return Expression("",self.Node(e1.expr.toString()))
		else:
			e = self.Node("+")	
			e.left = e1.expr
			e.right = e2.expr
			return Expression("",e)

	def makediff(self,e1,e2):
		if e2.expr.toString()=="0.0":
			return Expression("",self.Node(e1.expr.toString()))
		else:
			e = self.Node("-")	
			e.left = e1.expr
			e.right = e2.expr
			return Expression("",e)

	def makeprod(self,e1,e2):
		if e1.expr.toString()=="0.0" or e2.expr.toString()=="0.0":
			return Expression("",self.Node("0.0"))
		elif e1.expr.toString()=="1.0":
			return Expression("",self.Node(e2.expr.toString()))
		elif e2.expr.toString()=="1.0":
			return Expression("",self.Node(e1.expr.toString()))
		else:
			e = self.Node("*")	
			e.left = e1.expr
			e.right = e2.expr
			return Expression("",e)

	def makediv(self,e1,e2):
		if e1.expr.toString()=="0.0":
			return Expression("",self.Node("0.0"))
		elif e2.expr.toString()=="1.0":
			return Expression("",self.Node(e1.expr.toString())) 
		else:
			e = self.Node("/")	
			e.left = e1.expr
			e.right = e2.expr
			return Expression("",e)

	def makeexp(self,e1,e2):
		if e1.expr.toString()=="0.0":
			return Expression("",self.Node("0.0"))
		elif e1.expr.toString()=="1.0":
			return Expression("",self.Node("1.0"))
		elif e1.expr.toString()=="0.0":
			return Expression("",self.Node("1.0"))
		elif e2.expr.toString()=="1.0":
			return Expression("",self.Node(e1.expr.toString()))
		else:
			e = self.Node("^")	
			e.left = e1.expr
			e.right = e2.expr
			return Expression("",e)

	def makeln(self,e1):
		if e1.expr.toString()=="1.0" or e1.expr.toString()=="1":
			return Expression("",self.Node("0.0"))
		else:
			e = self.Node(" ")
			e.left = Expression("ln").expr
			e.right = e1.expr
			return Expression("",e) 

	def maketrig(self,e1,f,zero_val="0.0"):
		if e1.expr.toString()=="0.0" or e1.expr.toString()=="0":
			if zero_val=="False":
				raise Exception("Function doesn't here here! -.-")
			else:
				return Expression("",self.Node(zero_val))
		else:
			e = self.Node(" ")
			e.left = Expression(f).expr
			e.right = e1.expr
			return Expression("",e) 


	# Main Function to calculate derivative (Check Documentation for invariants)

	def differentiate(self,wrt="x"):
		if self.constant():
			return Expression("0.0")
		if self.variable():
			if self.samevariable(wrt):
				return Expression("1.0")
			else:
				return Expression("0.0")
		elif self.sum():
				e1 = self.leftExpression()
				e2 = self.rightExpression()
				return self.makesum(e1.differentiate(wrt),e2.differentiate(wrt))
		elif self.diff():
				e1 = self.leftExpression()
				e2 = self.rightExpression()
				return self.makediff(e1.differentiate(wrt),e2.differentiate(wrt))  
		elif self.prod():				                                                  
				e1 = self.leftExpression()
				e2 = self.rightExpression()
				return self.makesum(self.makeprod(e1.differentiate(wrt),e2),self.makeprod(e1,e2.differentiate(wrt))) 
		elif self.div():				                                                  
				e1 = self.leftExpression()
				e2 = self.rightExpression()
				return self.makediv(self.makediff(self.makeprod(e1.differentiate(wrt),e2),self.makeprod(e1,e2.differentiate(wrt))),self.makeexp(e2,Expression("2.0"))) 
		elif self.log_e():
				e2 = self.rightExpression()
				return self.makediv(e2.differentiate(wrt),e2)
		elif self.exp():				                                                  
				e1 = self.leftExpression()
				e2 = self.rightExpression()
				if e2.constant():
					return self.makeprod(self.makeprod(e2,self.makeexp(e1,Expression(str(float(e2.expr.toString())-1.0)))),e1.differentiate(wrt))
				else:
					return self.makeprod(self.makeexp(e1,e2),self.makesum(self.makeprod(e2.differentiate(wrt),self.makeln(e1)),self.makeprod(e2,self.makeln(e1).differentiate(wrt))))

		elif self.sin():
				e2 = self.rightExpression()
				return self.makeprod(self.maketrig(e2,"cos","1.0"),e2.differentiate(wrt))
		elif self.cos():
				e2 = self.rightExpression()
				return self.makeprod(self.makediff(Expression("0.0"),self.maketrig(e2,"sin")),e2.differentiate(wrt))
		elif self.tan():
				e2 = self.rightExpression()
				return self.makeprod(self.makeexp(self.maketrig(e2,"sec","1.0"),Expression("2.0")),e2.differentiate(wrt))
		elif self.sec():
				e2 = self.rightExpression()
				return self.makeprod(self.makeprod(self.maketrig(e2,"sec","1.0"),self.maketrig(e2,"tan")),e2.differentiate(wrt))
		elif self.cosec():
				e2 = self.rightExpression()
				return self.makeprod(self.makeprod(self.makediff(Expression("0.0"),self.maketrig(e2,"cosec","False")),self.maketrig(e2,"cot","False")),e2.differentiate(wrt))
		elif self.cot():
				e2 = self.rightExpression()
				return self.makeprod(self.makediff(Expression("0.0"),self.makeexp(self.maketrig(e2,"cosec","False"),Expression("2.0"))),e2.differentiate(wrt))

		else:
			raise Exception("Don't Know What To Do! :/")