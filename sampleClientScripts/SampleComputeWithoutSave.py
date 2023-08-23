from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")
bolt = model.getBoltPropertyByName("Bolt 2")

# To observe the functionality of compute, place a breakpoint in ScriptingInterface.cpp at the top of the compute function.
# The block below is hit on the first pass as the file has been modified. 
# On the second pass, this block will be skipped as the file is up to date. A save will not occur and only a compute will occur.

# From ScriptingInterface.cpp:
# if (document->IsModified()) 
# {
# document->DoFileSave();
# } 

for i in range(10):
	bolt.FullyBonded.setBoltDiameter(23 + i)
	model.compute()
	model.compute()