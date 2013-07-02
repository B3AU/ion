


n1 = sum_node()
n2 = gauss_node()

a = in_node()
b = out_node()

out1,out2,out3 = n(in1,in2,in3) #like a function

#connecting nodes

#network allows different configuration of functions
network.add(n1)
network.addEdge(n1.o1,n2.i1)

#or without network object, but use new instantiations
n1.out+n2.in #__ge__(self, other)
# >> override?

#break connection
n1.out / n2.in

#or with a function which connects two io's
connect(n1.o1,n2.i2)

#long version
n1.connect_to(n1_out,other_in)




#init ionode from other nodes
#checks reachability (and calculates computation order)
n3 = node(n1.i1,n2.i2,n3.o2)
n3 = node([n1.i1,n2.i2],[n3.o2]) #node(in_list,out_list)

print n3(2,3)

#construct node from function?
n = node(math.fabs)



#EXECUTION
#use as function
out = n1(1,2,3) #should this propagate?

#send data to ion
n1.i1 << 3
    n1 << 1,2,3

#buffered ins, multiple outs

s = IOnode(in)
node(None,out)


#simulate function when calling
__call__(self, *args, **kwargs)  #obj(arg1, arg2, ...) is a shorthand for obj.__call__(arg1, arg2, ...).

greenlet
https://bitbucket.org/fzzzy/python-actors
http://www.andescotia.com/examples/bnmvbccvnnmm
dataflow

scala actors?
