import inspect

class ion():



    class inputCollector():



        class inlet():
            def __init__(self,parent,argname):
                self.p = parent
                self.argname = argname
            def __lshift__(self,i):
                self.p.values[self.argname]=i
                self.p._check_input()


        def __init__(self,parent,in_args):
            self.args = in_args
            self.parent = parent
            self.values = dict.fromkeys(in_args)
            for a in in_args:
                a_inlet = self.inlet(self,a)
                setattr(self,a,a_inlet)

        def _check_input(self):
            if not None in self.values.values():
                arg_values= tuple([self.values[a] for a in self.args])
                self.parent.f(*arg_values)




    def __init__(self,f):
        """
        construct ion from function
        """
        self.f = f


        #init inlets
        args =  inspect.getargspec(self.f).args
        self.i = self.inputCollector(self,args)#namespace


        #init outlets





def myF(var1,var2):
    print var1
    print var2

a = ion(myF)
print 'a.i.var1 << "hello world"'
a.i.var1 << "hello world"

print 'a.i.var2 << "hello world"'
a.i.var2 << "hello world2"

