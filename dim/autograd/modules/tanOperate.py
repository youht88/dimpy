import dim
from ..operate import Operate
from ..constant import Constant

class TanOperate(Operate):
  def __init__(self,left,right,args=None,name=None):
    super(TanOperate,self).__init__(left,right,"tan",args,name)
  
  def partGrad(self,partial,prevOp):
    if (partial.type!="Variable"): raise Exception("partial参数必须是Variable类型")
    if (self.catch and self._grads.get(partial.name,None)): return self._grads[partial.name]
    if (prevOp is None): prevOp=Constant(dim.ones(self.eval().shape))

    part1 = dim.autograd.CosOperate.wrapper(self.left,None)
    part2 = dim.autograd.PowOperate.wrapper(part1,2)
    part3 = dim.autograd.DivOperate.Wrapper(Constant(1),part2)
    part4 = dim.autograd.MulOperate.wrapper(part3,prevOp)
    rst = self.left.partGrad(partial,part4)
    self._grads[partial.name]=rst
    return rst
  
  def expression(self):
    if (self.catch and self._expressionStr): return self._expressionStr
    rst = "tan("+self.left.expression()+")"
    self._expressionStr = rst
    return rst
  
  def eval(self):
    if (self.catch and self._data is not None): return self._data
    rst= dim.tan(self.left.eval())
    self._data = rst
    return rst
  
  @staticmethod
  def wrapper(self,left,right,args=None,name=None):
    return TanOperate(left,right,args,name)
