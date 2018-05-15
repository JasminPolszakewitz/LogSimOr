__version__ = "1.0"							
__author__ = "Jasmin Polszakewitz"


class AndGate:																			
	def __init__(self):																	
		self.__Input0 = False
		self.__Input1 = False
		self.__Output = False
		self.__Name = "YaOrGate"
		
	def getInput0(self):
		return self.__Input0
		
	def setInput0(self, value):
		isinstance(value, bool)
		self.__Input0 = value
		
	def getInput1(self):
		return.__Input1
		
	def setInput1(self, value):
		isinstance(value, bool)
		self.__Input1 = value
		
	def getOutput(self):
		return self.__Output
		
	def getName(self):
		return self.__Name
		
	
	Input0 = property(__getInput0, __setInput0)
	Input1 = property(__getInput1, __setInput1)
	Output = property(__getOutput, None) 
	Name = property (__getName, None)
	
		
	def show(self):
		print(first_last)
		print(format_string.format("Name", self.Name))
		print(format_string.format("Type", type(self).__name__))
		print(format_string.format("Input0", "True" if (self.Input0) else "False"))	
		print(format_string.format("Input1", "True" if (self.Input1) else "False"))
		print(format_string.format("Output", "True" if (self.Output) else "False"))	
		
	def execute(self):					
		if self.Input0 == True
			self.Output == True
		elif self.Input1 == True 
			self.Output == True
		else:
			self.Output == False
