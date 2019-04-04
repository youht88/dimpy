import dim
from ..operate import Operate
from ..constant import Constant

class AtanOperate(Operate):
  def __init__(self,left,right,args=None,name=None):
    super(AtanOperate,self).__init__(left,right,"atan",args,name)
  
  def partGrad(self,partial,prevOp):
    if (partial.type!="Variable"): raise Exception("partial参数必须是Variable类型")
    if (self.catch and self._grads.get(partial.name,None)): return self._grads[partial.name]
    if (prevOp is None): prevOp=Constant(dim.ones(self.eval().shape))

    part1 = dim.autograd.PowOperate.wrapper(self.left,2)
    part2 = dim.autograd.AddOperate.wrapper(Constant(1),part1)
    part3 = dim.autograd.DivOperate.wrapper(Constant(1),part2)
    part4 = dim.autograd.MulOperate.wrapper(part3,prevOp)
    rst = self.left.partGrad(partial,part4)
    self._grads[partial.name]=rst
    return rst
  
  def expression(self):
    if (self.catch and self._expressionStr): return self._expressionStr
    rst = "atan("+self.left.expression()+")"
    self._expressionStr = rst
    return rst

  def eval(self):
    if (self.catch and self._data is not None): return self._data
    rst= dim.atan(self.left.eval())
    self._data = rst
    return rst
  
  @staticmethod
  def wrapper(left,right,args=None,name=None):
    return AtanOperate(left,right,args,name)