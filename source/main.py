import Monitor
import Generator
import Coder_DVB
import Coder_V34
import Encoder_DVB
import Encoder_V34

data = [1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1]

Monitor.monitor_func() 					#prints "Hello!"
Generator.generator_func()			#print hello 	
Coder_DVB.coder_DVB_func()		#printf
Coder_V34.coder_V34_func(*data)	    	#printf
Encoder_DVB.encoder_DVB_func()	#printf
Encoder_V34.encoder_V34_func()	#printf