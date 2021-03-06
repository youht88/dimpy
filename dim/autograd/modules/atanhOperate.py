import dim
from ..operate import Operate
from ..constant import Constant

class AtanhOperate(Operate):
  def __init__(self,left,right,args=None,name=None):
    super(AtanhOperate,self).__init__(left,right,"atanh",args,name)
  
  def partGrad(self,partial,prevOp):
    if (partial.type!="Variable"): raise Exception("partial参数必须是Variable类型")
    if (self.catch and self._grads.get(partial.name,None)): return self._grads[partial.name]
    if (prevOp is None): prevOp=Constant(dim.ones(self.eval().shape))


    raise Exception("not impleted!")

    self._grads[partial.name]=rst
    return rst
  
  def expression(self):
    if (self.catch and self._expressionStr): return self._expressionStr
    rst = "atanh("+self.left.expression()+")"
    self._expressionStr = rst
    return rst
  
  def eval(self):
    if (self.catch and self._data is not None): return self._data
    rst= dim.atanh(self.left.eval())
    self._data = rst
    return rst
  
  @staticmethod
  def wrapper(left,right,args=None,name=None):
    return AtanhOperate(left,right,args,name)
