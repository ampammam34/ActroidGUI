#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file ActroidGUI.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist
import testFrame

frames = []


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
actroidgui_spec = ["implementation_id", "ActroidGUI", 
		 "type_name",         "ActroidGUI", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "VenderName", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class ActroidGUI
# @brief ModuleDescription
# 
# 
class ActroidGUI(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_current_position = RTC.TimedPose3D(RTC.Time(0,0),0)
		"""
		"""
		self._current_positionIn = OpenRTM_aist.InPort("current_position", self._d_current_position)
		self._d_current_jointangles = RTC.TimedDoubleSeq(RTC.Time(0,0),[])
		"""
		"""
		self._current_jointanglesIn = OpenRTM_aist.InPort("current_jointangles", self._d_current_jointangles)
		self._d_target_position = RTC.TimedPose3D(RTC.Time(0,0),0)
		"""
		"""
		self._target_positionOut = OpenRTM_aist.OutPort("target_position", self._d_target_position)
		self._d_target_jointangles = RTC.TimedDoubleSeq(RTC.Time(0,0),[])
		"""
		"""
		self._target_jointanglesOut = OpenRTM_aist.OutPort("target_jointangles", self._d_target_jointangles)
		self._d_gripper = RTC.TimedBoolean(RTC.Time(0,0),0)
		"""
		"""
		self._gripperOut = OpenRTM_aist.OutPort("gripper", self._d_gripper)


		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		self.addInPort("current_position",self._current_positionIn)
		self.addInPort("current_jointangles",self._current_jointanglesIn)
		
		# Set OutPort buffers
		self.addOutPort("target_position",self._target_positionOut)
		self.addOutPort("target_jointangles",self._target_jointanglesOut)
		self.addOutPort("gripper",self._gripperOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The activated action (Active state entry action)
	#	# former rtc_active_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	# 
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onActivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The deactivated action (Active state exit action)
	#	# former rtc_active_exit()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
                #print 'onExecute start'
                data_array = []
                data_array2 = []
                try:
                        global frames
                        n = 0
                        x = 0.0174 #532925 #[deg]にこの値をかけたら[rad]に変換できる
                        
                        for num in range(7, 22):
                                value = frames[num].getvalue()
                                data_array.append(value*x) #[deg]から[rad]に変換
                        self._d_target_jointangles.data = data_array #これは文字列(ここで*xしたらlengthがx倍されるだけ)
                        print self._d_target_jointangles
                        self._target_jointanglesOut.write()
                
                        if self._current_jointanglesIn.isNew():
                                indata = self._current_jointanglesIn.read()
                                print self._current_jointangles
                                print "Receive %d datas" % len(indata.data)
                                for v in indata.data:
                                        #print "Data is %d" % (v)
                                        frames[n].setvalue(v)
                                        n +=1

                                #for n in range(0, 24):
                                #        frames[n].setvalue(frames[n].getvalue())

                        return RTC.RTC_OK
                
                except Exception, e:
                        print 'Exception : ', e
                        pass
	
		return RTC.RTC_OK
                
	
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def ActroidGUIInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=actroidgui_spec)
    manager.registerFactory(profile,
                            ActroidGUI,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    ActroidGUIInit(manager)

    # Create a component
    comp = manager.createComponent("ActroidGUI")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

        global frames
        root, frames = testFrame.GUI.__init__(self)

        for num in range(0, 13):
                print "scale value is ", str(frames[num].getvalue())
        
	root.mainloop()

if __name__ == "__main__":
	main()

