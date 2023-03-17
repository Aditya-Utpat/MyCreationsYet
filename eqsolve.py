import re
a= input('Enter Equation:')
class equation:
    class terms:
        def __init__(self,sign,cof):
            if sign == None:
                sign = '+'
            self.sign = sign
            self.cof = cof
            if len(re.findall('[A-Za-z]+',self.cof)) > 0:
                self.var = re.findall('[A-Za-z]+',self.cof)[0]
                self.cof = self.cof.replace(self.var,'')
            else:
                self.var = None
            if
            if '('in self.cof:
                self.binomial = True
                print("Cannot parse binomials")
                quit()
        def simple_binomial(bin):
            pass
    def __init__(self,eq):
        eq = eq.replace(' ','')
        self.LHS = eq.split('=')[0]
        self.RHS = eq.split('=')[1]
        self.var = re.findall('[A-Za-z]+',eq)[0]
        self.LHSterms = []
        sin = None
        par = 0
        lt = 0
        n = 0
        self.LHS = self.LHS + '+'
        for i in self.LHS:
            if par >0 and i != ')':
                n+=1
                continue
            elif i == ')':
                par -= 1
            elif (i == '+')or (i =='-'):
                if n==0 :
                    continue
                self.LHSterms.append(self.terms(sin,self.LHS[lt:n]))
                lt = n+1
                sin = i

            elif i == '(':
                par+=1
            n+=1
        self.LHS = self.LHS[0:-1]
        self.RHSterms = []
        sin = None
        par = 0
        lt = 0
        n = 0
        self.RHS = self.RHS + '+'
        for i in self.RHS:
            if par >0 and i != ')':
                n+=1
                continue
            elif i == ')':
                par -= 1
            elif (i == '+')or (i =='-'):
                if n==0 :
                    continue
                self.RHSterms.append(self.terms(sin,self.RHS[lt:n]))
                lt = n+1
                sin = i

            elif i == '(':
                par+=1
            n+=1
        self.RHS = self.RHS[0:-1]


    def solve(self):
        n = 0
        for a in self.RHSterms:
            if a.var != None:
                if a.sign == '+':
                    a.sign = '-'
                else:
                    a.sign = '+'
                self.RHSterms.remove(a)
                self.LHSterms.append(a)

        for a in self.LHSterms:
            if a.var == None:
                if a.sign == '+':
                    a.sign = '-'
                else:
                    a.sign = '+'
                self.LHSterms.remove(a)
                self.RHSterms.append(a)
        print(self.RHSterms[0].cof)
        print(self.LHSterms[0].cof)
        a = ''
        for b in self.LHSterms:
            a= a+b.sign +b.cof
        self.LHSterms = eval(a)
        a = ''
        for b in self.RHSterms:
            a= a+b.sign+ b.cof
        self.RHSterms = eval(a)
        #print(self.RHSterms)
        #print(self.LHSterms)
        print(self.var,'=',self.RHSterms/self.LHSterms)


eqt = equation(a)
eqt.solve()
