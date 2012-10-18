#=================================================================================================================================================
#=================================================================================================================================================
#    JAMMSoft Crash Test Dummy Interface
#=================================================================================================================================================
#=================================================================================================================================================
# 
# DESCRIPTION:
#    This interface works as a set of tools that helps to control the rig.
#    With this tool the animator will be able to carry out actions such as:
#        - Seamless IK-FK Switch
#        - Mirror/Flip poses
#        - Pin Controls one to another
#        - Seamless Global Follow Switch
#        - Dynamic Pivot Control
#
# 
# AUTHOR:
#     Jose Antonio Martin Martin - JoseAntonioMartinMartin@gmail.com
#                                  http://www.joseantoniomartinmartin.com
#     Copyright 2010 Jose Antonio Martin Martin - All Rights Reserved.
# 
# CHANGELOG:
#    0.1 - 09/10/2010 - Basic interface and functionality.
#    0.2 - 09/20/2010 - More functionality.
#    0.3 - 09/30/2010 - Minor bug fixes.
#    1.0 - 10/10/2010 - First version.
#    1.0.1 - 12/08/2010 - First version. Minor bug fixes with Maya 2011.
# ====================================================================================================================



import maya.cmds as cmds
import maya.mel as mel



#=================================================================================================================================================
#=================================================================================================================================================
#    VARIABLES 
#=================================================================================================================================================
#=================================================================================================================================================

baseDirectory = mel.eval('getenv MAYA_APP_DIR')
mayaVersion = cmds.about(v=True).replace(' ', '-')
finalDirectory = baseDirectory + '/' + mayaVersion + '/' + 'scripts/'
imgDir = finalDirectory

crashDummyImage = 'crashTestDummyBackground.jpg'
poseDummyImage = 'poseDummyBackground.jpg'

crashDummyMirrorImage = 'crashTestDummyBackground_Mirror.jpg'
poseDummyMirrorImage = 'poseDummyBackground_Mirror.jpg'



#IK-FK JOINTS NAMES ==============================================================================================================================
#=================================================================================================================================================

#LEFT ARM JOINTS
jntShoulderLeft = 'sknShoulder000Left'
jntElbowPosLeft = 'sknElbowStretchy000Left'
jntElbowRotLeft = 'sknElbow000Left'
jntWristPosLeft = 'sknWristStretchy000Left'
jntWristRotLeft = 'sknWrist000Left'

#RIGHT ARM JOINTS
jntShoulderRight = 'sknShoulder000Right'
jntElbowPosRight = 'sknElbowStretchy000Right'
jntElbowRotRight = 'sknElbow000Right'
jntWristPosRight = 'sknWristStretchy000Right'
jntWristRotRight = 'sknWrist000Right'

#LEFT LEG JOINTS
jntHipLeft = 'sknHip000Left'
jntKneePosLeft = 'sknKneeStretchy000Left'
jntKneeRotLeft = 'sknKnee000Left'
jntAnklePosLeft = 'sknAnkleStretchy000Left'
jntAnkleRotLeft = 'sknAnkle000Left'
jntToeLeft = 'sknToe000Left'

#RIGHT LEG JOINTS
jntHipRight = 'sknHip000Right'
jntKneePosRight = 'sknKneeStretchy000Right'
jntKneeRotRight = 'sknKnee000Right'
jntAnklePosRight = 'sknAnkleStretchy000Right'
jntAnkleRotRight = 'sknAnkle000Right'
jntToeRight = 'sknToe000Right'



#IK-FK CONTROLS NAMES ============================================================================================================================
#=================================================================================================================================================

#LEFT ARM IK
ctlIkArmPositionLeft = 'ctlArmIkPosition000Left'
ctlIkArmPoleVectorLeft = 'ctlArmPoleVector000Left'
ctlIkArmLeft = 'ctlIkArm000Left'

#LEFT ARM FK
ctlFkShoulderLeft = 'ctlFkShoulder000Left'
ctlFkElbowLeft = 'ctlFkElbow000Left'
ctlFkWristLeft = 'ctlFkWrist000Left'

#LEFT ARM IK-FK
ikFkArmLeft = 'ctlIKFKArm000Left'

#RIGHT ARM IK
ctlIkArmPositionRight = 'ctlArmIkPosition000Right'
ctlIkArmPoleVectorRight = 'ctlArmPoleVector000Right'
ctlIkArmRight = 'ctlIkArm000Right'

#RIGHT ARM FK
ctlFkShoulderRight = 'ctlFkShoulder000Right'
ctlFkElbowRight = 'ctlFkElbow000Right'
ctlFkWristRight = 'ctlFkWrist000Right'

#RIGHT ARM IK-FK
ikFkArmRight = 'ctlIKFKArm000Right'

#LEFT LEG IK
ctlIkLegPositionLeft = 'ctlLegIkPosition000Left'
ctlIkLegPoleVectorLeft = 'ctlLegPoleVector000Left'
ctlIkLegLeft = 'ctlIkLeg000Left'

#LEFT LEG FK
ctlFkHipLeft = 'ctlFkHip000Left'
ctlFkKneeLeft = 'ctlFkKnee000Left'
ctlFkAnkleLeft = 'ctlFkAnkle000Left'
ctlFkToeLeft = 'ctlFkToe000Left'

#LEFT LEG IK-FK
ikFkLegLeft = 'ctlIKFKLeg000Left'

#RIGHT LEG IK
ctlIkLegPositionRight = 'ctlLegIkPosition000Right'
ctlIkLegPoleVectorRight = 'ctlLegPoleVector000Right'
ctlIkLegRight = 'ctlIkLeg000Right'

#RIGHT LEG FK
ctlFkHipRight = 'ctlFkHip000Right'
ctlFkKneeRight = 'ctlFkKnee000Right'
ctlFkAnkleRight = 'ctlFkAnkle000Right'
ctlFkToeRight = 'ctlFkToe000Right'

#RIGHT LEG IK-FK
ikFkLegRight = 'ctlIKFKLeg000Right'



#BEND CONTROLS NAMES =============================================================================================================================
#=================================================================================================================================================

leftArmBend = 'ctlBendArm000Left'
leftMidArmBend = 'ctlBendMidArm000Left'
leftForeArmBend = 'ctlBendForearm000Left'

rightArmBend = 'ctlBendArm000Right'
rightMidArmBend = 'ctlBendMidArm000Right'
rightForeArmBend = 'ctlBendForearm000Right'

leftHipBend = 'ctlBendHip000Left'
leftMidLegBend = 'ctlBendMidLeg000Left'
leftLegBend = 'ctlBendLeg000Left'

rightHipBend = 'ctlBendHip000Right'
rightMidLegBend = 'ctlBendMidLeg000Right'
rightLegBend = 'ctlBendLeg000Right'



#HIERARCHICAL CONTROLS LIST ======================================================================================================================
#=================================================================================================================================================

listAllControls = ['ctlMain000Middle', 'ctlRoot000Middle', 'ctlHip000Middle', 'ctlFkHip000Left', 'ctlFkKnee000Left', 
'ctlFkAnkle000Left', 'ctlFkToe000Left', 'ctlFkHip000Right', 'ctlFkKnee000Right', 'ctlFkAnkle000Right', 'ctlFkToe000Right', 
'ctlSpine000Middle', 'ctlSpine001Middle', 'ctlFkNeck000Middle', 'ctlFkHead000Middle', 'ctlEyeBrow000Left', 
'ctlRibbonEyeBrowDriver000Left', 'ctlRibbonEyeBrowDriver001Left', 'ctlRibbonEyeBrowDriver002Left', 
'ctlEyeBrow000Right', 'ctlRibbonEyeBrowDriver000Right', 'ctlRibbonEyeBrowDriver001Right', 'ctlRibbonEyeBrowDriver002Right', 
'ctlStretchSquashHead000Middle', 'ctlMouthLipSync000Middle', 'ctlMouthEmotion000Left', 'ctlMouthEmotion000Right', 
'ctlFkCollarbone000Left', 'ctlFkShoulder000Left', 'ctlFkElbow000Left', 'ctlFkWrist000Left', 'ctlFkCollarbone000Right', 
'ctlFkShoulder000Right', 'ctlFkElbow000Right', 'ctlFkWrist000Right', 'ctlIKFKArm000Left', 'ctlIKFKArm000Right',
'ctlIKFKLeg000Left', 'ctlIKFKLeg000Right', 'ctlArmIkPosition000Left', 'ctlIkArm000Left', 'ctlArmPoleVector000Left', 
'ctlArmIkPosition000Right', 'ctlIkArm000Right', 'ctlArmPoleVector000Right', 'ctlHandControl000Left', 'ctlIndexCarpal000Left', 
'ctlIndex000Left', 'ctlIndex001Left', 'ctlIndex002Left', 'ctlMiddleCarpal000Left', 'ctlMiddle000Left', 'ctlMiddle001Left', 
'ctlMiddle002Left', 'ctlRingCarpal000Left', 'ctlRing000Left', 'ctlRing001Left', 'ctlRing002Left', 'ctlPinkyCarpal000Left', 
'ctlPinky000Left', 'ctlPinky001Left', 'ctlPinky002Left', 'ctlThumbCarpal000Left', 'ctlThumb000Left', 'ctlThumb001Left', 
'ctlThumb002Left', 'ctlIndexFinger000Left', 'ctlMiddleFinger000Left', 'ctlRingFinger000Left', 'ctlPinkyFinger000Left', 
'ctlThumbFinger000Left', 'ctlHandControl000Right', 'ctlIndexCarpal000Right', 'ctlIndex000Right', 'ctlIndex001Right', 
'ctlIndex002Right', 'ctlMiddleCarpal000Right', 'ctlMiddle000Right', 'ctlMiddle001Right', 'ctlMiddle002Right', 'ctlRingCarpal000Right', 
'ctlRing000Right', 'ctlRing001Right', 'ctlRing002Right', 'ctlPinkyCarpal000Right', 'ctlPinky000Right', 'ctlPinky001Right', 
'ctlPinky002Right', 'ctlThumbCarpal000Right', 'ctlThumb000Right', 'ctlThumb001Right', 'ctlThumb002Right', 'ctlIndexFinger000Right', 
'ctlMiddleFinger000Right', 'ctlRingFinger000Right', 'ctlPinkyFinger000Right', 'ctlThumbFinger000Right','ctlEye000Middle', 
'ctlEye000Left', 'ctlEye000Right', 'ctlLegIkPosition000Left', 'ctlIkLeg000Left', 'ctlLegPoleVector000Left', 'ctlLegIkPosition000Right', 
'ctlIkLeg000Right', 'ctlLegPoleVector000Right', 'ctlBendArm000Left', 'ctlBendMidArm000Left', 'ctlBendForearm000Left', 
'ctlBendArm000Right', 'ctlBendMidArm000Right', 'ctlBendForearm000Right','ctlBendHip000Left', 'ctlBendMidLeg000Left', 
'ctlBendLeg000Left', 'ctlBendHip000Right', 'ctlBendMidLeg000Right', 'ctlBendLeg000Right']



#OTHERS CONTROLS NAMES ===========================================================================================================================
#=================================================================================================================================================

rootControlName = 'ctlRoot000Middle'
mainControlName = 'ctlMain000Middle'

animationControlsSet = 'AnimationControls'

grpResetPoseLeftArm = 'grpIkArmResetPose000Left'
grpResetPoseRightArm = 'grpIkArmResetPose000Right'
grpResetPoseLeftLeg = 'grpIkLegResetPose000Left'
grpResetPoseRightLeg = 'grpIkLegResetPose000Right'

grpResetPosePoleVectorLeftArm = 'grpIkArmResetPosePoleVector000Left'
grpResetPosePoleVectorRightArm = 'grpIkArmResetPosePoleVector000Right'
grpResetPosePoleVectorLeftLeg = 'grpIkLegResetPosePoleVector000Left'
grpResetPosePoleVectorRightLeg = 'grpIkLegResetPosePoleVector000Right'



#NAMESPACE =======================================================================================================================================
#=================================================================================================================================================
lstNamespaces = None
lstNamespaces = cmds.namespaceInfo(lon=True)
lstNamespaces.remove('UI')
lstNamespaces.remove('shared')



#EXTRA PIN AND DYNAMIC PIVOT CONTROLS SHAPES =====================================================================================================
#=================================================================================================================================================

extraPinControlShape = [[0.0, 0.99425700000000006, 0.0022410449999999997], [-0.25109999999999999, 0.55200000000000005, 0.0], [-0.078932100000000005, 0.55252500000000004, 0.0], [-0.078932100000000005, 0.078932100000000005, 0.0], [-0.55252500000000004, 0.078932100000000005, 0.0], [-0.55200000000000005, 0.25109999999999999, 0.0], [-0.99425700000000006, 0.0022409999999999999, 0.0], [-0.55200000000000005, 0.0, 0.25109999999999999], [-0.55252500000000004, 0.0, 0.078932100000000005], [-0.078932100000000005, 0.0, 0.078932100000000005], [-0.078932100000000005, 0.0, 0.55252500000000004], [-0.25109999999999999, 0.0, 0.55200000000000005], [-0.0022410449999999997, 0.0, 0.99425700000000006], [0.0, 0.25109999999999999, 0.55200000000000005], [0.0, 0.078932100000000005, 0.55252500000000004], [0.0, 0.079554299999999994, 0.078932100000000005], [0.0, 0.55252500000000004, 0.078932100000000005], [0.0, 0.55200000000000005, 0.25109999999999999], [0.0, 0.99425700000000006, 0.0022410449999999997], [0.0, 0.55200000000000005, -0.2457], [0.0, 0.55252500000000004, -0.078932100000000005], [0.0, 0.08699670000000001, -0.078932100000000005], [0.0, 0.078932100000000005, -0.55252500000000004], [0.0, 0.25109999999999999, -0.55200000000000005], [0.0, 0.0022409999999999999, -0.99425700000000006], [0.0, -0.2457, -0.55200000000000005], [0.0, -0.078932100000000005, -0.55252500000000004], [0.0, -0.078932100000000005, -0.078932100000000005], [0.0, -0.55252500000000004, -0.078932100000000005], [0.0, -0.55200000000000005, -0.2457], [0.0, -0.99425700000000006, 0.0022409580000000004], [0.0, -0.55200000000000005, 0.25109999999999999], [0.0, -0.55252500000000004, 0.078932100000000005], [0.0, -0.078932100000000005, 0.078932100000000005], [0.0, -0.078932100000000005, 0.55252500000000004], [0.0, -0.2457, 0.55200000000000005], [-0.0022410449999999997, 0.0, 0.99425700000000006], [0.2457, 0.0, 0.55200000000000005], [0.078932100000000005, 0.0, 0.55252500000000004], [0.078932100000000005, 0.0, 0.078932100000000005], [0.55252500000000004, 0.0, 0.078932100000000005], [0.55200000000000005, 0.0, 0.25109999999999999], [0.99425700000000006, 0.0, 0.0022409999999999999], [0.55200000000000005, 0.0, -0.2457], [0.55252500000000004, 0.0, -0.078932100000000005], [0.078932100000000005, 0.0, -0.078932100000000005], [0.078932100000000005, 0.0, -0.55252500000000004], [0.2457, 0.0, -0.55200000000000005], [0.0, 0.0022409999999999999, -0.99425700000000006], [-0.25109999999999999, 0.0, -0.55200000000000005], [-0.078932100000000005, 0.0, -0.55252500000000004], [-0.078932100000000005, 0.0, -0.078932100000000005], [-0.55252500000000004, 0.0, -0.078932100000000005], [-0.55200000000000005, 0.0, -0.2457], [-0.99425700000000006, 0.0022409999999999999, 0.0], [-0.55200000000000005, -0.2457, 0.0], [-0.55252500000000004, -0.078932100000000005, 0.0], [-0.078932100000000005, -0.078932100000000005, 0.0], [-0.078932100000000005, -0.55252500000000004, 0.0], [-0.25109999999999999, -0.55200000000000005, 0.0], [-0.0022409580000000004, -0.99425700000000006, 0.0], [0.2457, -0.55200000000000005, 0.0], [0.078932100000000005, -0.55252500000000004, 0.0], [0.078932100000000005, -0.078932100000000005, 0.0], [0.55252500000000004, -0.078932100000000005, 0.0], [0.55200000000000005, -0.2457, 0.0], [0.99425700000000006, 0.0, 0.0022409999999999999], [0.55200000000000005, 0.25109999999999999, 0.0], [0.55252500000000004, 0.078932100000000005, 0.0], [0.078932100000000005, 0.078932100000000005, 0.0], [0.078932100000000005, 0.55252500000000004, 0.0], [0.2457, 0.55200000000000005, 0.0], [0.0, 0.99425700000000006, 0.0022410449999999997]]

dynamicPivotControlShape = [[0.0, 0.0, 0.98999999999999999], [0.0, 0.17191185000000003, 0.97495860000000001], [0.0, 0.33859980000000006, 0.93029640000000002], [0.0, 0.495, 0.85736639999999997], [0.0, 0.63635880000000011, 0.75838289999999997], [0.0, 0.75838289999999997, 0.63635880000000011], [0.0, 0.85736639999999997, 0.495], [0.0, 0.93029640000000002, 0.33859980000000006], [0.0, 0.97495860000000001, 0.17191185000000003], [0.0, 0.98999999999999999, 0.0], [0.0, 0.97495860000000001, -0.17191185000000003], [0.0, 0.93029640000000002, -0.33859980000000006], [0.0, 0.85736639999999997, -0.495], [0.0, 0.75838289999999997, -0.63635880000000011], [0.0, 0.63635880000000011, -0.75838289999999997], [0.0, 0.495, -0.85736639999999997], [0.0, 0.33859980000000006, -0.93029640000000002], [0.0, 0.17191185000000003, -0.97495860000000001], [0.0, 0.0, -0.98999999999999999], [0.17191185000000003, 0.0, -0.97495860000000001], [0.33859980000000006, 0.0, -0.93029640000000002], [0.495, 0.0, -0.85736639999999997], [0.63635880000000011, 0.0, -0.75838289999999997], [0.75838289999999997, 0.0, -0.63635880000000011], [0.85736639999999997, 0.0, -0.495], [0.93029640000000002, 0.0, -0.33859980000000006], [0.97495860000000001, 0.0, -0.17191185000000003], [0.98999999999999999, 0.0, 0.0], [0.97495860000000001, 0.0, 0.17191185000000003], [0.93029640000000002, 0.0, 0.33859980000000006], [0.85736639999999997, 0.0, 0.495], [0.75838289999999997, 0.0, 0.63635880000000011], [0.63635880000000011, 0.0, 0.75838289999999997], [0.495, 0.0, 0.85736639999999997], [0.33859980000000006, 0.0, 0.93029640000000002], [0.17191185000000003, 0.0, 0.97495860000000001], [0.0, 0.0, 0.98999999999999999], [0.0, -0.17191185000000003, 0.97495860000000001], [0.0, -0.33859980000000006, 0.93029640000000002], [0.0, -0.495, 0.85736639999999997], [0.0, -0.63635880000000011, 0.75838289999999997], [0.0, -0.75838289999999997, 0.63635880000000011], [0.0, -0.85736639999999997, 0.495], [0.0, -0.93029640000000002, 0.33859980000000006], [0.0, -0.97495860000000001, 0.17191185000000003], [0.0, -0.98999999999999999, 0.0], [0.0, -0.97495860000000001, -0.17191185000000003], [0.0, -0.93029640000000002, -0.33859980000000006], [0.0, -0.85736639999999997, -0.495], [0.0, -0.75838289999999997, -0.63635880000000011], [0.0, -0.63635880000000011, -0.75838289999999997], [0.0, -0.495, -0.85736639999999997], [0.0, -0.33859980000000006, -0.93029640000000002], [0.0, -0.17191185000000003, -0.97495860000000001], [0.0, 0.0, -0.98999999999999999], [-0.17191185000000003, 0.0, -0.97495860000000001], [-0.33859980000000006, 0.0, -0.93029640000000002], [-0.495, 0.0, -0.85736639999999997], [-0.63635880000000011, 0.0, -0.75838289999999997], [-0.75838289999999997, 0.0, -0.63635880000000011], [-0.85736639999999997, 0.0, -0.495], [-0.93029640000000002, 0.0, -0.33859980000000006], [-0.97495860000000001, 0.0, -0.17191185000000003], [-0.98999999999999999, 0.0, 0.0], [-0.97495860000000001, 0.17191185000000003, 0.0], [-0.93029640000000002, 0.33859980000000006, 0.0], [-0.85736639999999997, 0.495, 0.0], [-0.75838289999999997, 0.63635880000000011, 0.0], [-0.63635880000000011, 0.75838289999999997, 0.0], [-0.495, 0.85736639999999997, 0.0], [-0.33859980000000006, 0.93029640000000002, 0.0], [-0.17191185000000003, 0.97495860000000001, 0.0], [0.0, 0.98999999999999999, 0.0], [0.17191185000000003, 0.97495860000000001, 0.0], [0.33859980000000006, 0.93029640000000002, 0.0], [0.495, 0.85736639999999997, 0.0], [0.63635880000000011, 0.75838289999999997, 0.0], [0.75838289999999997, 0.63635880000000011, 0.0], [0.85736639999999997, 0.495, 0.0], [0.93029640000000002, 0.33859980000000006, 0.0], [0.97495860000000001, 0.17191185000000003, 0.0], [0.98999999999999999, 0.0, 0.0], [0.97495860000000001, -0.17191185000000003, 0.0], [0.93029640000000002, -0.33859980000000006, 0.0], [0.85736639999999997, -0.495, 0.0], [0.75838289999999997, -0.63635880000000011, 0.0], [0.63635880000000011, -0.75838289999999997, 0.0], [0.495, -0.85736639999999997, 0.0], [0.33859980000000006, -0.93029640000000002, 0.0], [0.17191185000000003, -0.97495860000000001, 0.0], [0.0, -0.98999999999999999, 0.0], [-0.17191185000000003, -0.97495860000000001, 0.0], [-0.33859980000000006, -0.93029640000000002, 0.0], [-0.495, -0.85736639999999997, 0.0], [-0.63635880000000011, -0.75838289999999997, 0.0], [-0.75838289999999997, -0.63635880000000011, 0.0], [-0.85736639999999997, -0.495, 0.0], [-0.93029640000000002, -0.33859980000000006, 0.0], [-0.97495860000000001, -0.17191185000000003, 0.0], [-0.98999999999999999, 0.0, 0.0], [-0.97495860000000001, 0.0, 0.17191185000000003], [-0.93029640000000002, 0.0, 0.33859980000000006], [-0.85736639999999997, 0.0, 0.495], [-0.75838289999999997, 0.0, 0.63635880000000011], [-0.63635880000000011, 0.0, 0.75838289999999997], [-0.495, 0.0, 0.85736639999999997], [-0.33859980000000006, 0.0, 0.93029640000000002], [-0.17191185000000003, 0.0, 0.97495860000000001], [0.0, 0.0, 0.98999999999999999]]

#=================================================================================================================================================
#=================================================================================================================================================
#    end of - VARIABLES 
#=================================================================================================================================================
#=================================================================================================================================================



#=================================================================================================================================================
#=================================================================================================================================================
#    GUI LAYOUT
#=================================================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    crashTestDummyInterface()
#
# DESCRIPTION:
#    Interface Function.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def crashTestDummyInterface():

    lstNamespaces = None
    lstNamespaces = cmds.namespaceInfo(lon=True)
    lstNamespaces.remove('UI')
    lstNamespaces.remove('shared')

    if cmds.window('crashTestDummyWindow', ex=True) == True:
        cmds.deleteUI('crashTestDummyWindow')

    version = 'v 1.0'
    date = '10/10/2010'

    cmds.window('crashTestDummyWindow', w=640, h=530, t=('Crash Test Dummy Rig UI - ' + version))

    cmds.formLayout('mainForm')

    cmds.optionMenuGrp('ddlNamespace', label='Namespace:', columnWidth2=(70, 150))
    if lstNamespaces:
        if len(lstNamespaces) > 0:
            for eachNamespace in lstNamespaces:
                cmds.menuItem(label=str(eachNamespace))
        else:
            cmds.menuItem(label=':')
    else:
        cmds.menuItem(label=':')

    cmds.optionMenuGrp('ddlNamespace', e=True, cc=ddlChangeEvent)

    cmds.tabLayout('tabs')

    if (cmds.about(v=True) == '2011' or cmds.about(v=True) == '2011 x64'):
        cmds.formLayout('mainForm', e=True, attachForm=[
                                ('tabs', 'left', 0), 
                                ('tabs', 'top', 20),
                                ('tabs', 'right', 0), 
                                ('tabs', 'bottom', 0),

                                ('ddlNamespace', 'top', 0),
                                ('ddlNamespace', 'left', 475)
                                ])
    else:
        cmds.formLayout('mainForm', e=True, attachForm=[
                                ('tabs', 'left', 0), 
                                ('tabs', 'top', 0),
                                ('tabs', 'right', 0), 
                                ('tabs', 'bottom', 0),

                                ('ddlNamespace', 'top', 0),
                                ('ddlNamespace', 'left', 470)
                                ])


    #TAB 1
    cmds.formLayout('matchIkFk')

    if (cmds.about(v=True) == '2011' or cmds.about(v=True) == '2011 x64'):
        currNamespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
        if currNamespace.startswith('crashDummy'):
            cmds.image('backgroundImage', image=(imgDir + crashDummyImage), w=640, h=480)
        elif currNamespace.startswith('poseDummy'):
            cmds.image('backgroundImage', image=(imgDir + poseDummyImage), w=640, h=480)
        else:
            cmds.image('backgroundImage', image=(imgDir + crashDummyImage), w=640, h=480)

    cmds.button('btnLeftArmIkToFk', l='IK to FK', w=75, h=75, c=leftArmIkToFkUI)
    cmds.button('btnLeftArmFkToIk', l='FK to IK', w=75, h=75, c=leftArmFkToIkUI)

    cmds.button('btnRightArmIkToFk', l='IK to FK', w=75, h=75, c=rightArmIkToFkUI)
    cmds.button('btnRightArmFkToIk', l='FK to IK', w=75, h=75, c=rightArmFkToIkUI)

    cmds.button('btnLeftLegIkToFk', l='IK to FK', w=75, h=75, c=leftLegIkToFkUI)
    cmds.button('btnLeftLegFkToIk', l='FK to IK', w=75, h=75, c=leftLegFkToIkUI)

    cmds.button('btnRightLegIkToFk', l='IK to FK', w=75, h=75, c=rightLegIkToFkUI)
    cmds.button('btnRightLegFkToIk', l='FK to IK', w=75, h=75, c=rightLegFkToIkUI)



    cmds.button('btnSelectLeftArm', l='select left arm', w=85, h=20, c=selectLeftArmControlsUI, vis=False)    
    cmds.button('btnKeyLeftArm', l='key left arm', w=85, h=20, c=keyLeftArmControlsUI, vis=False)

    cmds.button('btnSelectRightArm', l='select right arm', w=85, h=20, c=selectRightArmControlsUI, vis=False)    
    cmds.button('btnKeyRightArm', l='key right arm', w=85, h=20, c=keyRightArmControlsUI, vis=False)

    cmds.button('btnSelectLeftLeg', l='select left leg', w=75, h=20, c=selectLeftLegControlsUI, vis=False)    
    cmds.button('btnKeyLeftLeg', l='key left leg', w=75, h=20, c=keyLeftLegControlsUI, vis=False)

    cmds.button('btnSelectRightLeg', l='select right leg', w=75, h=20, c=selectRightLegControlsUI, vis=False)    
    cmds.button('btnKeyRightLeg', l='key right leg', w=75, h=20, c=keyRightLegControlsUI, vis=False)



    cmds.button('btnSelectLeftArmBends', l='select L bend', w=85, h=20, c=selectLeftArmBendsUI, vis=False)    
    cmds.button('btnKeyLeftArmBends', l='key L bend', w=85, h=20, c=keyLeftArmBendsUI, vis=False)

    cmds.button('btnSelectRightArmBends', l='select R bend', w=85, h=20, c=selectRightArmBendsUI, vis=False)    
    cmds.button('btnKeyRightArmBends', l='key R bend', w=85, h=20, c=keyRightArmBendsUI, vis=False)

    cmds.button('btnSelectLeftLegBends', l='select L bend', w=75, h=20, c=selectLeftLegBendsUI, vis=False)    
    cmds.button('btnKeyLeftLegBends', l='key L bend', w=75, h=20, c=keyLeftLegBendsUI, vis=False)

    cmds.button('btnSelectRightLegBends', l='select R bend', w=75, h=20, c=selectRightLegBendsUI, vis=False)    
    cmds.button('btnKeyRightLegBends', l='key R bend', w=75, h=20, c=keyRightLegBendsUI, vis=False)



    cmds.button('btnSelectAll', l='SELECT ALL CONTROLS', w=150, h=30, c=selectAllUI)
    cmds.button('btnDeselectAll', l='DESELECT ALL', w=150, h=30, c=deselectAllUI)
    cmds.button('btnKeyAll', l='KEY ALL CONTROLS', w=150, h=30, c=keyAllUI)
    cmds.button('btnKeySelected', l='KEY SELECTED', w=150, h=30, c=keySelectedUI)

    cmds.button('btnResetAll', l='RESET ALL', w=150, h=30, c=resetAllUI)
    cmds.button('btnResetPose', l='RESET T-POSE', w=150, h=30, c=resetPoseUI)
    cmds.button('btnResetSelected', l='RESET SELECTED', w=150, h=30, c=resetSelectedUI)

    if (cmds.about(li=True) or cmds.about(l64=True)) or (cmds.about(win=True) and cmds.about(v=True) != '2011' and cmds.about(v=True) != '2011 x64'):
        currNamespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
        if currNamespace.startswith('crashDummy'):
            cmds.image('backgroundImage', image=(imgDir + crashDummyImage), w=640, h=480)
        elif currNamespace.startswith('poseDummy'):
            cmds.image('backgroundImage', image=(imgDir + poseDummyImage), w=640, h=480)
        else:
            cmds.image('backgroundImage', image=(imgDir + crashDummyImage), w=640, h=480)

    cmds.formLayout('matchIkFk', e=True, attachForm=[
                            ('backgroundImage', 'top', 0),


                            ('btnLeftArmIkToFk', 'top', 130),
                            ('btnLeftArmIkToFk', 'left', 365),

                            ('btnLeftArmFkToIk', 'top', 130),
                            ('btnLeftArmFkToIk', 'left', 445),


                            ('btnRightArmIkToFk', 'top', 130),
                            ('btnRightArmIkToFk', 'left', 200),

                            ('btnRightArmFkToIk', 'top', 130),
                            ('btnRightArmFkToIk', 'left', 120),


                            ('btnLeftLegIkToFk', 'top', 320),
                            ('btnLeftLegIkToFk', 'left', 365),

                            ('btnLeftLegFkToIk', 'top', 400),
                            ('btnLeftLegFkToIk', 'left', 365),


                            ('btnRightLegIkToFk', 'top', 320),
                            ('btnRightLegIkToFk', 'left', 200),

                            ('btnRightLegFkToIk', 'top', 400),
                            ('btnRightLegFkToIk', 'left', 200),




                            ('btnSelectLeftArm', 'top', 35),
                            ('btnSelectLeftArm', 'left', 365),

                            ('btnKeyLeftArm', 'top', 60),
                            ('btnKeyLeftArm', 'left', 365),


                            ('btnSelectRightArm', 'top', 35),
                            ('btnSelectRightArm', 'left', 190),

                            ('btnKeyRightArm', 'top', 60),
                            ('btnKeyRightArm', 'left', 190),


                            ('btnSelectLeftLeg', 'top', 215),
                            ('btnSelectLeftLeg', 'left', 365),

                            ('btnKeyLeftLeg', 'top', 240),
                            ('btnKeyLeftLeg', 'left', 365),


                            ('btnSelectRightLeg', 'top', 215),
                            ('btnSelectRightLeg', 'left', 200),

                            ('btnKeyRightLeg', 'top', 240),
                            ('btnKeyRightLeg', 'left', 200),



                            ('btnSelectLeftArmBends', 'top', 35),
                            ('btnSelectLeftArmBends', 'left', 465),

                            ('btnKeyLeftArmBends', 'top', 60),
                            ('btnKeyLeftArmBends', 'left', 465),


                            ('btnSelectRightArmBends', 'top', 35),
                            ('btnSelectRightArmBends', 'left', 90),

                            ('btnKeyRightArmBends', 'top', 60),
                            ('btnKeyRightArmBends', 'left', 90),


                            ('btnSelectLeftLegBends', 'top', 270),
                            ('btnSelectLeftLegBends', 'left', 365),

                            ('btnKeyLeftLegBends', 'top', 295),
                            ('btnKeyLeftLegBends', 'left', 365),


                            ('btnSelectRightLegBends', 'top', 270),
                            ('btnSelectRightLegBends', 'left', 200),

                            ('btnKeyRightLegBends', 'top', 295),
                            ('btnKeyRightLegBends', 'left', 200),




                            ('btnSelectAll', 'top', 230),
                            ('btnSelectAll', 'left', 20),

                            ('btnDeselectAll', 'top', 270),
                            ('btnDeselectAll', 'left', 20),

                            ('btnKeyAll', 'top', 320),
                            ('btnKeyAll', 'left', 20),

                            ('btnKeySelected', 'top', 360),
                            ('btnKeySelected', 'left', 20),

                            ('btnResetAll', 'top', 230),
                            ('btnResetAll', 'left', 465),

                            ('btnResetPose', 'top', 270),
                            ('btnResetPose', 'left', 465),

                            ('btnResetSelected', 'top', 310),
                            ('btnResetSelected', 'left', 465)
                            ])

    cmds.setParent('..')



    #TAB 2
    cmds.formLayout('mirrorPose')

    if (cmds.about(v=True) == '2011' or cmds.about(v=True) == '2011 x64'):
        currNamespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
        if currNamespace.startswith('crashDummy'):
            cmds.image('backgroundImageMirror', image=(imgDir + crashDummyMirrorImage), w=640, h=480)
        elif currNamespace.startswith('poseDummy'):
            cmds.image('backgroundImageMirror', image=(imgDir + poseDummyMirrorImage), w=640, h=480)
        else:
            cmds.image('backgroundImageMirror', image=(imgDir + crashDummyMirrorImage), w=640, h=480)

    cmds.radioButtonGrp('rbgMirrorOptions', l='', nrb=2, la2=('World Space', 'Root Relative'), sl=1, cw3=(1,100,100))
    cmds.radioButtonGrp('rbgMirrorSelectOptions', l='', nrb=2, la2=('All', 'Selected'), sl=1, cw3=(1,100,100))

    cmds.button('btnMirrorLeftToRight', l='<< MIRROR LEFT TO RIGHT', w=200, h=30, c=mirrorLeftToRightUI)
    cmds.button('btnFlipLeftToRight', l='<< FLIP LEFT TO RIGHT', w=200, h=30, c=flipLeftToRightUI)

    cmds.button('btnMirrorRightToLeft', l='MIRROR RIGHT TO LEFT >>', w=200, h=30, c=mirrorRightToLeftUI)
    cmds.button('btnFlipRightToLeft', l='FLIP RIGHT TO LEFT >>', w=200, h=30, c=flipRightToLeftUI)

    cmds.button('btnSelectAll', l='SELECT ALL CONTROLS', w=150, h=30, c=selectAllUI)
    cmds.button('btnDeselectAll', l='DESELECT ALL', w=150, h=30, c=deselectAllUI)
    cmds.button('btnKeyAll', l='KEY ALL CONTROLS', w=150, h=30, c=keyAllUI)
    cmds.button('btnKeySelected', l='KEY SELECTED', w=150, h=30, c=keySelectedUI)

    cmds.button('btnResetAll', l='RESET ALL', w=150, h=30, c=resetAllUI)
    cmds.button('btnResetPose', l='RESET T-POSE', w=150, h=30, c=resetPoseUI)
    cmds.button('btnResetSelected', l='RESET SELECTED', w=150, h=30, c=resetSelectedUI)

    if (cmds.about(li=True) or cmds.about(l64=True)) or (cmds.about(win=True) and cmds.about(v=True) != '2011' and cmds.about(v=True) != '2011 x64'):
        currNamespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
        if currNamespace.startswith('crashDummy'):
            cmds.image('backgroundImageMirror', image=(imgDir + crashDummyMirrorImage), w=640, h=480)
        elif currNamespace.startswith('poseDummy'):
            cmds.image('backgroundImageMirror', image=(imgDir + poseDummyMirrorImage), w=640, h=480)
        else:
            cmds.image('backgroundImageMirror', image=(imgDir + crashDummyMirrorImage), w=640, h=480)

    cmds.formLayout('mirrorPose', e=True, attachForm=[
                            ('backgroundImageMirror', 'top', 0),



                            ('rbgMirrorOptions', 'top', 30),
                            ('rbgMirrorOptions', 'left', 375),

                            ('rbgMirrorSelectOptions', 'top', 50),
                            ('rbgMirrorSelectOptions', 'left', 375),



                            ('btnMirrorLeftToRight', 'top', 130),
                            ('btnMirrorLeftToRight', 'left', 390),

                            ('btnFlipLeftToRight', 'top', 165),
                            ('btnFlipLeftToRight', 'left', 390),

                            ('btnMirrorRightToLeft', 'top', 130),
                            ('btnMirrorRightToLeft', 'left', 50),

                            ('btnFlipRightToLeft', 'top', 165),
                            ('btnFlipRightToLeft', 'left', 50),



                            ('btnSelectAll', 'top', 230),
                            ('btnSelectAll', 'left', 20),

                            ('btnDeselectAll', 'top', 270),
                            ('btnDeselectAll', 'left', 20),

                            ('btnKeyAll', 'top', 320),
                            ('btnKeyAll', 'left', 20),

                            ('btnKeySelected', 'top', 360),
                            ('btnKeySelected', 'left', 20),

                            ('btnResetAll', 'top', 230),
                            ('btnResetAll', 'left', 465),

                            ('btnResetPose', 'top', 270),
                            ('btnResetPose', 'left', 465),

                            ('btnResetSelected', 'top', 310),
                            ('btnResetSelected', 'left', 465)
                            ])

    cmds.setParent('..')



    #TAB 3
    cmds.formLayout('pin')

    cmds.text('txtDoPin', l='- First, select the DRIVER CONTROL, then shift-select the DRIVEN CONTROL.', w=620, align='center')
    cmds.button('btnDoPin', l='PIN CONTROLS', w=120, h=35, c=doPinUI)

    cmds.separator('sepPin1', style='double', h=5)

    cmds.text('txtDeletePin', l='- Select the driven control. CAUTION. Will lose any driven animation in the control.', w=620, align='center')
    cmds.button('btnDeletePin', l='Delete Pin', w=70, h=25, c=deletePinUI)

    cmds.separator('sepPin2', style='double', h=5)
    cmds.separator('sepPin3', style='double', h=5)

    cmds.text('txtBakeAndDelete', l='BAKE AND DELETE PIN', w=620, align='center')
    cmds.text('txtBakeAndDeleteInfo', l='- Select the driven control. Will read the driven animation, bake it and delete the pin.', w=620, align='center')
    cmds.radioButtonGrp('rbgTimeInfo', l='Time Frame: ', nrb=2, la2=('From Timeline', 'Custom'), sl=1, cw3=(100,100,100), cl3=('left', 'left', 'left'), cc1=hideFieldsUI, cc2=showFieldsUI)

    cmds.intFieldGrp('intStartFrame', l='Start Frame: ', numberOfFields=1, v1=cmds.playbackOptions(q=True, ast=True), cw2=(70,100), cl2=('left', 'left'), vis=False)
    cmds.intFieldGrp('intEndFrame', l='End Frame: ', numberOfFields=1, v1=cmds.playbackOptions(q=True, aet=True), cw2=(70,100), cl2=('left', 'left'), vis=False)

    cmds.button('btnDoBake', l='BAKE AND DELETE PIN', w=150, h=35, c=bakeAndDeletePinUI)

    cmds.separator('sepPin4', style='double', h=5)
    cmds.separator('sepPin5', style='double', h=5)

    cmds.button('btnLoadExtraControl', l='Load EXTRA PIN Control', w=150, h=40, c=createExtraPinControlUI)

    cmds.button('btnDeleteExtraControl', l='Delete SELECTED Extra PIN Control', w=185, h=20, c=deleteExtraPinControlUI)

    cmds.button('btnDeleteAllExtraControl', l='Delete ALL Extra PIN Controls', w=185, h=20, c=deleteAllExtraPinControlsUI)

    cmds.formLayout('pin', e=True, attachForm=[
                            ('txtDoPin', 'top', 10),
                            ('txtDoPin', 'left', 10),

                            ('btnDoPin', 'top', 30),
                            ('btnDoPin', 'left', 260),

                            ('sepPin1', 'top', 75),
                            ('sepPin1', 'left', 5),
                            ('sepPin1', 'right', 5),

                            ('txtDeletePin', 'top', 90),
                            ('txtDeletePin', 'left', 10),

                            ('btnDeletePin', 'top', 110),
                            ('btnDeletePin', 'left', 285),

                            ('sepPin2', 'top', 145),
                            ('sepPin2', 'left', 5),
                            ('sepPin2', 'right', 5),

                            ('sepPin3', 'top', 155),
                            ('sepPin3', 'left', 5),
                            ('sepPin3', 'right', 5),

                            ('txtBakeAndDelete', 'top', 175),
                            ('txtBakeAndDelete', 'left', 10),

                            ('txtBakeAndDeleteInfo', 'top', 200),
                            ('txtBakeAndDeleteInfo', 'left', 10),

                            ('rbgTimeInfo', 'top', 250),
                            ('rbgTimeInfo', 'left', 10),

                            ('intStartFrame', 'top', 280),
                            ('intStartFrame', 'left', 210),

                            ('intEndFrame', 'top', 310),
                            ('intEndFrame', 'left', 210),

                            ('btnDoBake', 'top', 345),
                            ('btnDoBake', 'left', 245),

                            ('sepPin4', 'top', 410),
                            ('sepPin4', 'left', 5),
                            ('sepPin4', 'right', 5),

                            ('sepPin5', 'top', 420),
                            ('sepPin5', 'left', 5),
                            ('sepPin5', 'right', 5),

                            ('btnLoadExtraControl', 'top', 440),
                            ('btnLoadExtraControl', 'left', 25),

                            ('btnDeleteExtraControl', 'top', 450),
                            ('btnDeleteExtraControl', 'left', 225),

                            ('btnDeleteAllExtraControl', 'top', 450),
                            ('btnDeleteAllExtraControl', 'left', 430),

                            ])

    cmds.setParent('..')



    #TAB 4
    cmds.formLayout('globalAndFollow')

    cmds.text('txtTitle', l='- SEAMLESS GLOBAL AND FOLLOW SWITCH -', w=620, align='center')
    cmds.text('txtExplanation', l='- Will switch the value of the Global or Follow attribute of the selected controls', w=620, align='center')
    cmds.text('txtExplanation2', l='but maintaining the current position of the object driven by the control.', w=620, align='center')
    cmds.button('btnSwitchGlobal', l='SWITCH GLOBAL / FOLLOW VALUE', w=240, h=40, c=seamlessGlobalOrFollowSwitchUI)

    cmds.formLayout('globalAndFollow', e=True, attachForm=[
                            ('txtTitle', 'top', 50),
                            ('txtTitle', 'left', 10),

                            ('txtExplanation', 'top', 90),
                            ('txtExplanation', 'left', 10),

                            ('txtExplanation2', 'top', 110),
                            ('txtExplanation2', 'left', 10),

                            ('btnSwitchGlobal', 'top', 160),
                            ('btnSwitchGlobal', 'left', 200),

                            ])

    cmds.setParent('..')



    #TAB 5
    cmds.formLayout('dynPivot')

    cmds.text('txtTitlePivot', l='- DYNAMIC PIVOT -', w=620, align='center')
    cmds.text('txtExplanationPivot', l='- Will create an object to control the pivot of the Main control.', w=620, align='center')
    cmds.text('txtExplanationPivot2', l='This control is also animatable and can also be pinned under other controls.', w=620, align='center')
    cmds.button('btnDynPivot', l='CREATE DYNAMIC PIVOT', w=240, h=40, c=createDynamicMainPivotUI)

    cmds.separator('sepPivot1', style='double', h=5)
    cmds.separator('sepPivot2', style='double', h=5)

    cmds.text('txtBakeAndDeletePivot', l='BAKE AND DELETE DYNAMIC PIVOT', w=620, align='center')
    cmds.text('txtBakeAndDeleteInfoPivot', l='-Will read the animation, delete the Dynamic Pivot and then set the animation to the Main Control.', w=620, align='center')
    cmds.radioButtonGrp('rbgTimeInfoPivot', l='Time Frame: ', nrb=2, la2=('From Timeline', 'Custom'), sl=1, cw3=(100,100,100), cl3=('left', 'left', 'left'), cc1=hideFieldsPivotUI, cc2=showFieldsPivotUI)
    cmds.intFieldGrp('intStartFramePivot', l='Start Frame: ', numberOfFields=1, v1=cmds.playbackOptions(q=True, ast=True), cw2=(70,100), cl2=('left', 'left'), vis=False)
    cmds.intFieldGrp('intEndFramePivot', l='End Frame: ', numberOfFields=1, v1=cmds.playbackOptions(q=True, aet=True), cw2=(70,100), cl2=('left', 'left'), vis=False)
    cmds.button('btnDoBakePivot', l='BAKE AND DELETE DYNAMIC PIVOT', w=200, h=35, c=bakeAndDeleteDynamicMainPivotUI)

    cmds.formLayout('dynPivot', e=True, attachForm=[
                            ('txtTitlePivot', 'top', 50),
                            ('txtTitlePivot', 'left', 10),

                            ('txtExplanationPivot', 'top', 90),
                            ('txtExplanationPivot', 'left', 10),

                            ('txtExplanationPivot2', 'top', 110),
                            ('txtExplanationPivot2', 'left', 10),

                            ('btnDynPivot', 'top', 160),
                            ('btnDynPivot', 'left', 200),

                            ('sepPivot1', 'top', 215),
                            ('sepPivot1', 'left', 5),
                            ('sepPivot1', 'right', 5),

                            ('sepPivot2', 'top', 225),
                            ('sepPivot2', 'left', 5),
                            ('sepPivot2', 'right', 5),

                            ('txtBakeAndDeletePivot', 'top', 245),
                            ('txtBakeAndDeletePivot', 'left', 10),

                            ('txtBakeAndDeleteInfoPivot', 'top', 270),
                            ('txtBakeAndDeleteInfoPivot', 'left', 10),

                            ('rbgTimeInfoPivot', 'top', 320),
                            ('rbgTimeInfoPivot', 'left', 10),

                            ('intStartFramePivot', 'top', 350),
                            ('intStartFramePivot', 'left', 210),

                            ('intEndFramePivot', 'top', 380),
                            ('intEndFramePivot', 'left', 210),

                            ('btnDoBakePivot', 'top', 415),
                            ('btnDoBakePivot', 'left', 220),

                            ])

    cmds.setParent('..')



    cmds.tabLayout('tabs', edit=True, tabLabel=(('matchIkFk', 'Match IK-FK'), ('mirrorPose', 'Mirror/Flip Pose'), ('pin', 'Pin Controls'), ('globalAndFollow', 'Global/Follow Switch'), ('dynPivot', 'Dynamic Pivot')))

    cmds.showWindow('crashTestDummyWindow')    

    if cmds.about(v=True) != '2011' and cmds.about(v=True) != '2011 x64':
        cmds.window('crashTestDummyWindow', e=True, w=650, h=550, sizeable=False, titleBar=True)

    initialState()

#=================================================================================================================================================
#=================================================================================================================================================
#    end of - GUI LAYOUT
#=================================================================================================================================================
#=================================================================================================================================================



#=================================================================================================================================================
#=================================================================================================================================================
#    GUI METHODS
#=================================================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    initialState()
#
# DESCRIPTION:
#    Sets the initial state of some variables and interface object based on the loaded rig.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def initialState():
    currNamespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if currNamespace != '':
        currNamespace += ':'
#NAMESPACE =======================================================================================================================================
#=================================================================================================================================================
    if cmds.objExists(currNamespace + ikFkArmLeft + '.ikFkSwitch'):
        if cmds.getAttr(currNamespace + ikFkArmLeft + '.ikFkSwitch') == 0:
            cmds.button('btnLeftArmIkToFk', e=True, vis=True)
            cmds.button('btnLeftArmFkToIk', e=True, vis=False)
        elif cmds.getAttr(currNamespace + ikFkArmLeft + '.ikFkSwitch') == 10:
            cmds.button('btnLeftArmIkToFk', e=True, vis=False)
            cmds.button('btnLeftArmFkToIk', e=True, vis=True)

    if cmds.objExists(currNamespace + ikFkArmRight + '.ikFkSwitch'):
        if cmds.getAttr(currNamespace + ikFkArmRight + '.ikFkSwitch') == 0:
            cmds.button('btnRightArmIkToFk', e=True, vis=True)
            cmds.button('btnRightArmFkToIk', e=True, vis=False)
        elif cmds.getAttr(currNamespace + ikFkArmRight + '.ikFkSwitch') == 10:
            cmds.button('btnRightArmIkToFk', e=True, vis=False)
            cmds.button('btnRightArmFkToIk', e=True, vis=True)

    if cmds.objExists(currNamespace + ikFkLegLeft + '.ikFkSwitch'):
        if cmds.getAttr(currNamespace + ikFkLegLeft + '.ikFkSwitch') == 0:
            cmds.button('btnLeftLegIkToFk', e=True, vis=True)
            cmds.button('btnLeftLegFkToIk', e=True, vis=False)
        elif cmds.getAttr(currNamespace + ikFkLegLeft + '.ikFkSwitch') == 10:
            cmds.button('btnLeftLegIkToFk', e=True, vis=False)
            cmds.button('btnLeftLegFkToIk', e=True, vis=True)

    if cmds.objExists(currNamespace + ikFkLegRight + '.ikFkSwitch'):
        if cmds.getAttr(currNamespace + ikFkLegRight + '.ikFkSwitch') == 0:
            cmds.button('btnRightLegIkToFk', e=True, vis=True)
            cmds.button('btnRightLegFkToIk', e=True, vis=False)
        elif cmds.getAttr(currNamespace + ikFkLegRight + '.ikFkSwitch') == 10:
            cmds.button('btnRightLegIkToFk', e=True, vis=False)
            cmds.button('btnRightLegFkToIk', e=True, vis=True)

    if currNamespace.startswith('crashDummy'):
        cmds.image('backgroundImage', e=True, image=(imgDir + crashDummyImage), w=640, h=480)
        cmds.image('backgroundImageMirror', e=True, image=(imgDir + crashDummyMirrorImage), w=640, h=480)
    elif currNamespace.startswith('poseDummy'):
        cmds.image('backgroundImage', e=True, image=(imgDir + poseDummyImage), w=640, h=480)
        cmds.image('backgroundImageMirror', e=True, image=(imgDir + poseDummyMirrorImage), w=640, h=480)
    else:
        cmds.image('backgroundImage', e=True, image=(imgDir + crashDummyImage), w=640, h=480)
        cmds.image('backgroundImageMirror', e=True, image=(imgDir + crashDummyMirrorImage), w=640, h=480)

#=================================================================================================================================================
#=================================================================================================================================================
#    end of - GUI METHODS
#=================================================================================================================================================
#=================================================================================================================================================



#=================================================================================================================================================
#=================================================================================================================================================
#    GUI EVENTS
#=================================================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    ddlChangeEvent(* args)
#
# DESCRIPTION:
#    Event triggered everytime the namespace selected from the list is changed.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def ddlChangeEvent(* args):
    initialState()



#MATCH IK-FK =====================================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    leftArmIkToFkUI(* args)
#
# DESCRIPTION:
#    'Left Match IK-FK Arm' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def leftArmIkToFkUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    matchIkToFkLeftArm(namespace, insertKey=True)
    cmds.button('btnLeftArmIkToFk', e=True, vis=False)
    cmds.button('btnLeftArmFkToIk', e=True, vis=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    leftArmFkToIkUI(* args)
#
# DESCRIPTION:
#    'Left Match FK-IK Arm' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def leftArmFkToIkUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    matchFkToIkLeftArm(namespace, insertKey=True)
    cmds.button('btnLeftArmIkToFk', e=True, vis=True)
    cmds.button('btnLeftArmFkToIk', e=True, vis=False)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    rightArmIkToFkUI(* args)
#
# DESCRIPTION:
#    'Right Match IK-FK Arm' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def rightArmIkToFkUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    matchIkToFkRightArm(namespace, insertKey=True)
    cmds.button('btnRightArmIkToFk', e=True, vis=False)
    cmds.button('btnRightArmFkToIk', e=True, vis=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    rightArmFkToIkUI(* args)
#
# DESCRIPTION:
#    'Right Match FK-IK Arm' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def rightArmFkToIkUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    matchFkToIkRightArm(namespace, insertKey=True)
    cmds.button('btnRightArmIkToFk', e=True, vis=True)
    cmds.button('btnRightArmFkToIk', e=True, vis=False)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    leftLegIkToFkUI(* args)
#
# DESCRIPTION:
#    'Left Match IK-FK Leg' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def leftLegIkToFkUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    matchIkToFkLeftLeg(namespace, insertKey=True)
    cmds.button('btnLeftLegIkToFk', e=True, vis=False)
    cmds.button('btnLeftLegFkToIk', e=True, vis=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    leftLegFkToIkUI(* args)
#
# DESCRIPTION:
#    'Left Match FK-IK Leg' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def leftLegFkToIkUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    matchFkToIkLeftLeg(namespace, insertKey=True)
    cmds.button('btnLeftLegIkToFk', e=True, vis=True)
    cmds.button('btnLeftLegFkToIk', e=True, vis=False)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    rightLegIkToFkUI(* args)
#
# DESCRIPTION:
#    'Right Match IK-FK Leg' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def rightLegIkToFkUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    matchIkToFkRightLeg(namespace, insertKey=True)
    cmds.button('btnRightLegIkToFk', e=True, vis=False)
    cmds.button('btnRightLegFkToIk', e=True, vis=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    rightLegFkToIkUI(* args)
#
# DESCRIPTION:
#    'Right Match FK-IK Leg' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def rightLegFkToIkUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    matchFkToIkRightLeg(namespace, insertKey=True)
    cmds.button('btnRightLegIkToFk', e=True, vis=True)
    cmds.button('btnRightLegFkToIk', e=True, vis=False)
    cmds.undoInfo(cck=True)



#SELECT AND KEY METHODS ==========================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    selectAllUI(* args)
#
# DESCRIPTION:
#    'Select All Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def selectAllUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    allItems = cmds.sets((namespace + animationControlsSet), q=True)
    cmds.select(allItems, r=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    deselectAllUI(* args)
#
# DESCRIPTION:
#    'Deselect All Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def deselectAllUI(* args):
    cmds.select(cl=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    keyAllUI(* args)
#
# DESCRIPTION:
#    'Key All Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def keyAllUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    allItems = cmds.sets((namespace + animationControlsSet), q=True)
    cmds.setKeyframe(allItems, breakdown=0, controlPoints=0, shape=0, hierarchy='none')
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    keySelectedUI(* args)
#
# DESCRIPTION:
#    'Key Selected Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def keySelectedUI(* args):
    cmds.undoInfo(ock=True)
    selectedItems = cmds.ls(sl=True)
    if selectedItems:
        cmds.setKeyframe(selectedItems, breakdown=0, controlPoints=0, shape=0, hierarchy='none')
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    resetAllUI(* args)
#
# DESCRIPTION:
#    'Reset All Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def resetAllUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    resetAll(namespace)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    resetPoseUI(* args)
#
# DESCRIPTION:
#    'Reset T-Pose' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def resetPoseUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    resetPose(namespace)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    resetSelectedUI(* args)
#
# DESCRIPTION:
#    'Reset Selected' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def resetSelectedUI(* args):
    cmds.undoInfo(ock=True)
    selectedItems = cmds.ls(sl=True)
    if selectedItems:
        namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
        if namespace != ':':
            namespace += ':'
        elif namespace == ':':
            namespace = ''
        resetSelected(namespace, selectedItems)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    selectLeftArmControlsUI(* args)
#
# DESCRIPTION:
#    'Select Left Arm Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def selectLeftArmControlsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.select([namespace + ctlIkArmPositionLeft, namespace + ctlIkArmPoleVectorLeft, namespace + ctlIkArmLeft, namespace + ctlFkShoulderLeft, namespace + ctlFkElbowLeft, namespace + ctlFkWristLeft, namespace + ikFkArmLeft], r=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    selectRightArmControlsUI(* args)
#
# DESCRIPTION:
#    'Select Right Arm Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def selectRightArmControlsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.select([namespace + ctlIkArmPositionRight, namespace + ctlIkArmPoleVectorRight, namespace + ctlIkArmRight, namespace + ctlFkShoulderRight, namespace + ctlFkElbowRight, namespace + ctlFkWristRight, namespace + ikFkArmRight], r=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    selectLeftLegControlsUI(* args)
#
# DESCRIPTION:
#    'Select Left Leg Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def selectLeftLegControlsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.select([namespace + ctlIkLegPositionLeft, namespace + ctlIkLegPoleVectorLeft, namespace + ctlIkLegLeft, namespace + ctlFkHipLeft, namespace + ctlFkKneeLeft, namespace + ctlFkAnkleLeft, namespace + ctlFkToeLeft, namespace + ikFkLegLeft], r=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    selectRightLegControlsUI(* args)
#
# DESCRIPTION:
#    'Select Right Leg Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def selectRightLegControlsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.select([namespace + ctlIkLegPositionRight, namespace + ctlIkLegPoleVectorRight, namespace + ctlIkLegRight, namespace + ctlFkHipRight, namespace + ctlFkKneeRight, namespace + ctlFkAnkleRight, namespace + ctlFkToeRight, namespace + ikFkLegRight], r=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    keyLeftArmControlsUI(* args)
#
# DESCRIPTION:
#    'Key Left Arm Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def keyLeftArmControlsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.setKeyframe([namespace + ctlIkArmPositionLeft, namespace + ctlIkArmPoleVectorLeft, namespace + ctlIkArmLeft, namespace + ctlFkShoulderLeft, namespace + ctlFkElbowLeft, namespace + ctlFkWristLeft, namespace + ikFkArmLeft], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    keyRightArmControlsUI(* args)
#
# DESCRIPTION:
#    'Key Right Arm Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def keyRightArmControlsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.setKeyframe([namespace + ctlIkArmPositionRight, namespace + ctlIkArmPoleVectorRight, namespace + ctlIkArmRight, namespace + ctlFkShoulderRight, namespace + ctlFkElbowRight, namespace + ctlFkWristRight, namespace + ikFkArmRight], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    keyLeftLegControlsUI(* args)
#
# DESCRIPTION:
#    'Key Left Leg Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def keyLeftLegControlsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.setKeyframe([namespace + ctlIkLegPositionLeft, namespace + ctlIkLegPoleVectorLeft, namespace + ctlIkLegLeft, namespace + ctlFkHipLeft, namespace + ctlFkKneeLeft, namespace + ctlFkAnkleLeft, namespace + ctlFkToeLeft, namespace + ikFkLegLeft], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    keyRightLegControlsUI(* args)
#
# DESCRIPTION:
#    'Key Right Leg Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def keyRightLegControlsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.setKeyframe([namespace + ctlIkLegPositionRight, namespace + ctlIkLegPoleVectorRight, namespace + ctlIkLegRight, namespace + ctlFkHipRight, namespace + ctlFkKneeRight, namespace + ctlFkAnkleRight, namespace + ctlFkToeRight, namespace + ikFkLegRight], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    selectLeftArmBendsUI(* args)
#
# DESCRIPTION:
#    'Select Left Arm Bend Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def selectLeftArmBendsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.select([namespace + leftArmBend, namespace + leftMidArmBend, namespace + leftForeArmBend], r=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    selectRightArmBendsUI(* args)
#
# DESCRIPTION:
#    'Select Left Leg Bend Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def selectRightArmBendsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.select([namespace + rightArmBend, namespace + rightMidArmBend, namespace + rightForeArmBend], r=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    selectLeftLegBendsUI(* args)
#
# DESCRIPTION:
#    'Select Left Leg Bend Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def selectLeftLegBendsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.select([namespace + leftHipBend, namespace + leftMidLegBend, namespace + leftLegBend], r=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    selectRightLegBendsUI(* args)
#
# DESCRIPTION:
#    'Select Right Arm Bend Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def selectRightLegBendsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.select([namespace + rightHipBend, namespace + rightMidLegBend, namespace + rightLegBend], r=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    keyLeftArmBendsUI(* args)
#
# DESCRIPTION:
#    'Key Left Arm Bend Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def keyLeftArmBendsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.setKeyframe([namespace + leftArmBend, namespace + leftMidArmBend, namespace + leftForeArmBend], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    keyRightArmBendsUI(* args)
#
# DESCRIPTION:
#    'Key Right Arm Bend Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def keyRightArmBendsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.setKeyframe([namespace + rightArmBend, namespace + rightMidArmBend, namespace + rightForeArmBend], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    keyLeftLegBendsUI(* args)
#
# DESCRIPTION:
#    'Key Left Leg Bend Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def keyLeftLegBendsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.setKeyframe([namespace + leftHipBend, namespace + leftMidLegBend, namespace + leftLegBend], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    keyRightLegBendsUI(* args)
#
# DESCRIPTION:
#    'Key Right Leg Bend Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def keyRightLegBendsUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    cmds.setKeyframe([namespace + rightHipBend, namespace + rightMidLegBend, namespace + rightLegBend], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
    cmds.undoInfo(cck=True)



#MIRROR/FLIP CONTROLS ============================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    mirrorLeftToRightUI(* args)
#
# DESCRIPTION:
#    'Mirror Left To Right' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def mirrorLeftToRightUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''

    worldSpace = True
    if cmds.radioButtonGrp('rbgMirrorOptions', q=True, sl=True) == 2:
        worldSpace = False

    allSelected = True
    objSelected = None
    if cmds.radioButtonGrp('rbgMirrorSelectOptions', q=True, sl=True) == 2:
        allSelected = False
        objSelected = cmds.ls(sl=True)

    if allSelected:
        if worldSpace:
            mirrorAllLeftToRightWorldSpace(namespace)
        else:
            mirrorAllLeftToRightRootRelative(namespace)
    else:
        if objSelected:
            if worldSpace:
                mirrorSelectedLeftToRightWorldSpace(namespace, objSelected)
            else:
                mirrorSelectedLeftToRightRootRelative(namespace, objSelected)
        else:
            print('USE: Select at least one control.')

    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    flipLeftToRightUI(* args)
#
# DESCRIPTION:
#    'Flip Left To Right' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def flipLeftToRightUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''

    worldSpace = True
    if cmds.radioButtonGrp('rbgMirrorOptions', q=True, sl=True) == 2:
        worldSpace = False

    allSelected = True
    objSelected = None
    if cmds.radioButtonGrp('rbgMirrorSelectOptions', q=True, sl=True) == 2:
        allSelected = False
        objSelected = cmds.ls(sl=True)

    if allSelected:
        if worldSpace:
            flipAllWorldSpace(namespace)
        else:
            flipAllRootRelative(namespace)
    else:
        if objSelected:
            if worldSpace:
                flipSelectedWorldSpace(namespace, objSelected)
            else:
                flipSelectedRootRelative(namespace, objSelected)
        else:
            print('USE: Select at least one control.')

    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    mirrorRightToLeftUI(* args)
#
# DESCRIPTION:
#    'Mirror Right To Left' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def mirrorRightToLeftUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''

    worldSpace = True
    if cmds.radioButtonGrp('rbgMirrorOptions', q=True, sl=True) == 2:
        worldSpace = False

    allSelected = True
    objSelected = None
    if cmds.radioButtonGrp('rbgMirrorSelectOptions', q=True, sl=True) == 2:
        allSelected = False
        objSelected = cmds.ls(sl=True)

    if allSelected:
        if worldSpace:
            mirrorAllRightToLeftWorldSpace(namespace)
        else:
            mirrorAllRightToLeftRootRelative(namespace)
    else:
        if objSelected:
            if worldSpace:
                mirrorSelectedRightToLeftWorldSpace(namespace, objSelected)
            else:
                mirrorSelectedRightToLeftRootRelative(namespace, objSelected)
        else:
            print('USE: Select at least one control.')

    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    flipRightToLeftUI(* args)
#
# DESCRIPTION:
#    'Flip Right To Left' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def flipRightToLeftUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''

    worldSpace = True
    if cmds.radioButtonGrp('rbgMirrorOptions', q=True, sl=True) == 2:
        worldSpace = False

    allSelected = True
    objSelected = None
    if cmds.radioButtonGrp('rbgMirrorSelectOptions', q=True, sl=True) == 2:
        allSelected = False
        objSelected = cmds.ls(sl=True)

    if allSelected:
        if worldSpace:
            flipAllWorldSpace(namespace)
        else:
            flipAllRootRelative(namespace)
    else:
        if objSelected:
            if worldSpace:
                flipSelectedWorldSpace(namespace, objSelected)
            else:
                flipSelectedRootRelative(namespace, objSelected)
        else:
            print('USE: Select at least one control.')

    cmds.undoInfo(cck=True)



#PIN CONTROLS ============================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    hideFieldsUI(* args)
#
# DESCRIPTION:
#    Hide 'Start Frame' and 'End Frame' fields for the 'Bake Pin Animation' option.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def hideFieldsUI(* args):
    cmds.undoInfo(ock=True)
    cmds.intFieldGrp('intStartFrame', e=True, vis=False)
    cmds.intFieldGrp('intEndFrame', e=True, vis=False)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    showFieldsUI(* args)
#
# DESCRIPTION:
#    Show 'Start Frame' and 'End Frame' fields for the 'Bake Pin Animation' option.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def showFieldsUI(* args):
    cmds.undoInfo(ock=True)
    cmds.intFieldGrp('intStartFrame', e=True, vis=True)
    cmds.intFieldGrp('intEndFrame', e=True, vis=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    doPinUI(* args)
#
# DESCRIPTION:
#    'Pin Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def doPinUI(* args):
    cmds.undoInfo(ock=True)
    ctlSelected = cmds.ls(sl=True)
    if not ctlSelected:
        showMessage('USE: - First, select the DRIVER CONTROL, then shift-select the DRIVEN CONTROL.')
    elif len(ctlSelected) != 2:
        showMessage('USE: - First, select the DRIVER CONTROL, then shift-select the DRIVEN CONTROL.')    
    elif ctlSelected[0].find('ctl') == -1 or ctlSelected[1].find('ctl') == -1:
        showMessage('USE: - First, select the DRIVER CONTROL, then shift-select the DRIVEN CONTROL.')    
    else:    
        doPin(ctlSelected[0], ctlSelected[1])
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    doPinUI(* args)
#
# DESCRIPTION:
#    'Delete Pin' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def deletePinUI(* args):
    cmds.undoInfo(ock=True)
    ctlSelected = cmds.ls(sl=True)
    if not ctlSelected:
        showMessage('USE: - Select the Control/s to UNPIN.')
    else:
        deletePin(ctlSelected)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    bakeAndDeletePinUI(* args)
#
# DESCRIPTION:
#    'Bake Animation and Delete Pin' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def bakeAndDeletePinUI(* args):
    cmds.undoInfo(ock=True)
    ctlSelected = cmds.ls(sl=True)
    if not ctlSelected:
        showMessage('USE: - Select the Control/s to BAKE the ANIMATION and UNPIN.')
    else:
        if cmds.radioButtonGrp('rbgTimeInfo', q=True, sl=True) == 1: #Timeline
            bakeAndDeletePin(ctlSelected)
        elif cmds.radioButtonGrp('rbgTimeInfo', q=True, sl=True) == 2: #Custom
            startFrame = cmds.intFieldGrp('intStartFrame', q=True, v1=True)
            endFrame = cmds.intFieldGrp('intEndFrame', q=True, v1=True)
            bakeAndDeletePin(ctlSelected, startFrame, endFrame)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    createExtraPinControlUI(* args)
#
# DESCRIPTION:
#    'Create Extra Pin Control' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def createExtraPinControlUI(* args):
    cmds.undoInfo(ock=True)
    createPinControl()
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    deleteExtraPinControlUI(* args)
#
# DESCRIPTION:
#    'Delete Selected Extra Pin Control/s' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def deleteExtraPinControlUI(* args):
    cmds.undoInfo(ock=True)
    ctlSelected = cmds.ls(sl=True)
    if not ctlSelected:
        showMessage('USE: - Select the PIN Control/s to DELETE.')
    else:
        removeSelectedPinControl(ctlSelected)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    deleteAllExtraPinControlsUI(* args)
#
# DESCRIPTION:
#    'Delete All Extra Pin Controls' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def deleteAllExtraPinControlsUI(* args):
    cmds.undoInfo(ock=True)
    removeAllPinControl()
    cmds.undoInfo(cck=True)



#SEAMLESS GLOBAL SWITCH ==========================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    seamlessGlobalOrFollowSwitchUI(* args)
#
# DESCRIPTION:
#    'Switch Global/Follow Value' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def seamlessGlobalOrFollowSwitchUI(* args):
    cmds.undoInfo(ock=True)
    ctlSelected = cmds.ls(sl=True)
    if not ctlSelected:
        showMessage('USE: - Select at least one control with a Global or a Follow attribute.')
    else:
        seamlessGlobalOrFollowSwitch(ctlSelected)
    cmds.undoInfo(cck=True)



#DYNAMIC PIVOT ===================================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    hideFieldsPivotUI(* args)
#
# DESCRIPTION:
#    Hide 'Start Frame' and 'End Frame' fields for the 'Bake Dynamic Pivot' option.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def hideFieldsPivotUI(* args):
    cmds.undoInfo(ock=True)
    cmds.intFieldGrp('intStartFramePivot', e=True, vis=False)
    cmds.intFieldGrp('intEndFramePivot', e=True, vis=False)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    showFieldsPivotUI(* args)
#
# DESCRIPTION:
#    Show 'Start Frame' and 'End Frame' fields for the 'Bake Dynamic Pivot' option.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def showFieldsPivotUI(* args):
    cmds.undoInfo(ock=True)
    cmds.intFieldGrp('intStartFramePivot', e=True, vis=True)
    cmds.intFieldGrp('intEndFramePivot', e=True, vis=True)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    createDynamicMainPivotUI(* args)
#
# DESCRIPTION:
#    'Create Dynamic Pivot' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def createDynamicMainPivotUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    createDynamicMainPivot(namespace)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    bakeAndDeleteDynamicMainPivotUI(* args)
#
# DESCRIPTION:
#    'Bake Animation and Delete Dynamic Pivot' Button Clicked.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def bakeAndDeleteDynamicMainPivotUI(* args):
    cmds.undoInfo(ock=True)
    namespace = cmds.optionMenuGrp('ddlNamespace', q=True, v=True)
    if namespace != ':':
        namespace += ':'
    elif namespace == ':':
        namespace = ''
    if cmds.radioButtonGrp('rbgTimeInfoPivot', q=True, sl=True) == 1: #Timeline
        bakeAndDeleteDynamicMainPivot(namespace)
    elif cmds.radioButtonGrp('rbgTimeInfoPivot', q=True, sl=True) == 2: #Custom
        startFrame = cmds.intFieldGrp('intStartFramePivot', q=True, v1=True)
        endFrame = cmds.intFieldGrp('intEndFramePivot', q=True, v1=True)
        bakeAndDeleteDynamicMainPivot(namespace, startFrame, endFrame)
    cmds.undoInfo(cck=True)

#=================================================================================================================================================
#=================================================================================================================================================
#    end of - GUI EVENTS
#=================================================================================================================================================
#=================================================================================================================================================



#=================================================================================================================================================
#=================================================================================================================================================
#    LOGIC
#=================================================================================================================================================
#=================================================================================================================================================

#MATCH IK-FK =====================================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    matchIkToFkLeftArm(namespace = ':', insertKey=True)
#
# DESCRIPTION:
#    Seamless IK to FK Switch for the Left Arm.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    insertKey - True or False. Sets or not an animation key when the switch is done.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def matchIkToFkLeftArm(namespace = ':', insertKey=True):
    if cmds.getAttr((namespace  + ikFkArmLeft + '.ikFkSwitch')) == 10:
        showMessage('INFO: Left Arm is already FK.')
    else:
        posShoulder = cmds.xform((namespace + jntShoulderLeft), q=True, t=True, ws=True)
        posElbow = cmds.xform((namespace + jntElbowPosLeft), q=True, t=True, ws=True)
        posWrist = cmds.xform((namespace + jntWristPosLeft), q=True, t=True, ws=True)
        rotShoulder = cmds.xform((namespace + jntShoulderLeft), q=True, ro=True, ws=True)
        rotElbow = cmds.xform((namespace + jntElbowRotLeft), q=True, ro=True, ws=True)
        rotWrist = cmds.xform((namespace + jntWristRotLeft), q=True, ro=True, ws=True)

        prevStatusAutoKey = 0
        if insertKey:
            prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
            cmds.autoKeyframe(state=False)
            cmds.currentTime(cmds.currentTime(q=True) - 1, edit=True)
            cmds.setKeyframe([namespace + ctlIkArmPositionLeft, namespace + ctlIkArmPoleVectorLeft, namespace + ctlIkArmLeft, namespace + ctlFkShoulderLeft, namespace + ctlFkElbowLeft, namespace + ctlFkWristLeft, namespace + ikFkArmLeft], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.currentTime(cmds.currentTime(q=True) + 1, edit=True)

        cmds.setAttr((namespace  + ikFkArmLeft + '.ikFkSwitch'), 10)
    
        cmds.xform((namespace + ctlFkShoulderLeft), ro=rotShoulder, ws=True)
        cmds.xform((namespace + ctlFkElbowLeft), ro=rotElbow, ws=True)
        cmds.xform((namespace + ctlFkWristLeft), ro=rotWrist, ws=True)
        cmds.xform((namespace + ctlFkShoulderLeft), t=posShoulder, ws=True)
        cmds.xform((namespace + ctlFkElbowLeft), t=posElbow, ws=True)
        cmds.xform((namespace + ctlFkWristLeft), t=posWrist, ws=True)

        if insertKey:
            cmds.setKeyframe([namespace + ctlIkArmPositionLeft, namespace + ctlIkArmPoleVectorLeft, namespace + ctlIkArmLeft, namespace + ctlFkShoulderLeft, namespace + ctlFkElbowLeft, namespace + ctlFkWristLeft, namespace + ikFkArmLeft], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.autoKeyframe(state=prevStatusAutoKey)

#=================================================================================================================================================
#
# SIGNATURE:
#    matchFkToIkLeftArm(namespace = ':', insertKey=True)
#
# DESCRIPTION:
#    Seamless FK to IK Switch for the Left Arm.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    insertKey - True or False. Sets or not an animation key when the switch is done.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def matchFkToIkLeftArm(namespace = ':', insertKey=True):
    if cmds.getAttr((namespace  + ikFkArmLeft + '.ikFkSwitch')) == 0:
        showMessage('INFO: Left Arm is already IK.')
    else:
        locLeftShoulder = 'tmpLocLeftShoulderFkToIk'
        locLeftElbow = 'tmpLocLeftElbowFkToIk'
        locLeftWrist = 'tmpLocLeftWristFkToIk'
        locLeftPoleVectorOff = 'locLeftPoleVectorOffFkToIk'
        locLeftPoleVector = 'locLeftPoleVectorFkToIk'

        cmds.spaceLocator(n=locLeftShoulder)
        cmds.spaceLocator(n=locLeftElbow)
        cmds.spaceLocator(n=locLeftWrist)
        cmds.spaceLocator(n=locLeftPoleVectorOff)
        cmds.spaceLocator(n=locLeftPoleVector)
        cmds.parent(locLeftPoleVector, locLeftPoleVectorOff)

        cmds.setAttr((locLeftShoulder + '.ro'), cmds.getAttr(namespace + jntShoulderLeft + '.ro'))
        cmds.setAttr((locLeftElbow + '.ro'), cmds.getAttr(namespace + jntElbowRotLeft + '.ro'))
        cmds.setAttr((locLeftWrist + '.ro'), cmds.getAttr(namespace + jntWristRotLeft + '.ro'))
        cmds.setAttr((locLeftPoleVectorOff + '.ro'), cmds.getAttr(namespace + jntElbowRotLeft + '.ro'))
        cmds.setAttr((locLeftPoleVector + '.ro'), cmds.getAttr(namespace + jntElbowRotLeft + '.ro'))

        posShoulder = cmds.xform((namespace + jntShoulderLeft), q=True, t=True, ws=True)
        posElbow = cmds.xform((namespace + jntElbowPosLeft), q=True, t=True, ws=True)
        posWrist = cmds.xform((namespace + jntWristPosLeft), q=True, t=True, ws=True)
        rotShoulder = cmds.xform((namespace + jntShoulderLeft), q=True, ro=True, ws=True)
        rotElbow = cmds.xform((namespace + jntElbowRotLeft), q=True, ro=True, ws=True)
        rotWrist = cmds.xform((namespace + jntWristRotLeft), q=True, ro=True, ws=True)

        cmds.xform(locLeftShoulder, t=posShoulder, ws=True)
        cmds.xform(locLeftElbow, t=posElbow, ws=True)
        cmds.xform(locLeftWrist, t=posWrist, ws=True)
        cmds.xform(locLeftShoulder, ro=rotShoulder, ws=True)
        cmds.xform(locLeftElbow, ro=rotElbow, ws=True)
        cmds.xform(locLeftWrist, ro=rotWrist, ws=True)

        prevStatusAutoKey = 0
        if insertKey:
            prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
            cmds.autoKeyframe(state=False)
            cmds.currentTime(cmds.currentTime(q=True) - 1, edit=True)
            cmds.setKeyframe([namespace + ctlIkArmPositionLeft, namespace + ctlIkArmPoleVectorLeft, namespace + ctlIkArmLeft, namespace + ctlFkShoulderLeft, namespace + ctlFkElbowLeft, namespace + ctlFkWristLeft, namespace + ikFkArmLeft], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.currentTime(cmds.currentTime(q=True) + 1, edit=True)

        cmds.setAttr((namespace  + ikFkArmLeft + '.ikFkSwitch'), 0)

        cmds.xform((namespace + ctlIkArmPositionLeft), ro=rotShoulder, ws=True)
        cmds.xform((namespace + ctlIkArmLeft), ro=rotWrist, ws=True)
        cmds.xform((namespace + ctlIkArmPositionLeft), t=posShoulder, ws=True)
        cmds.xform((namespace + ctlIkArmLeft), t=posWrist, ws=True)

        cmds.xform(locLeftPoleVectorOff, ro=rotElbow, ws=True)
        cmds.xform(locLeftPoleVectorOff, t=posElbow, ws=True)
        cmds.setAttr((locLeftPoleVector + '.tz'), -7.5)
        posPoleVector = cmds.xform(locLeftPoleVector, q=True, t=True, ws=True)
        cmds.xform((namespace + ctlIkArmPoleVectorLeft), t=posPoleVector, ws=True)

        cmds.delete([locLeftShoulder, locLeftElbow, locLeftWrist, locLeftPoleVectorOff, locLeftPoleVector])

        if insertKey:
            cmds.setKeyframe([namespace + ctlIkArmPositionLeft, namespace + ctlIkArmPoleVectorLeft, namespace + ctlIkArmLeft, namespace + ctlFkShoulderLeft, namespace + ctlFkElbowLeft, namespace + ctlFkWristLeft, namespace + ikFkArmLeft], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.autoKeyframe(state=prevStatusAutoKey)

#=================================================================================================================================================
#
# SIGNATURE:
#    matchIkToFkRightArm(namespace = ':', insertKey=True)
#
# DESCRIPTION:
#    Seamless IK to FK Switch for the Right Arm.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    insertKey - True or False. Sets or not an animation key when the switch is done.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def matchIkToFkRightArm(namespace = ':', insertKey=True):
    if cmds.getAttr((namespace  + ikFkArmRight + '.ikFkSwitch')) == 10:
        showMessage('INFO: Right Arm is already FK.')
    else:
        posShoulder = cmds.xform((namespace + jntShoulderRight), q=True, t=True, ws=True)
        posElbow = cmds.xform((namespace + jntElbowPosRight), q=True, t=True, ws=True)
        posWrist = cmds.xform((namespace + jntWristPosRight), q=True, t=True, ws=True)
        rotShoulder = cmds.xform((namespace + jntShoulderRight), q=True, ro=True, ws=True)
        rotElbow = cmds.xform((namespace + jntElbowRotRight), q=True, ro=True, ws=True)
        rotWrist = cmds.xform((namespace + jntWristRotRight), q=True, ro=True, ws=True)

        prevStatusAutoKey = 0
        if insertKey:
            prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
            cmds.autoKeyframe(state=False)
            cmds.currentTime(cmds.currentTime(q=True) - 1, edit=True)
            cmds.setKeyframe([namespace + ctlIkArmPositionRight, namespace + ctlIkArmPoleVectorRight, namespace + ctlIkArmRight, namespace + ctlFkShoulderRight, namespace + ctlFkElbowRight, namespace + ctlFkWristRight, namespace + ikFkArmRight], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.currentTime(cmds.currentTime(q=True) + 1, edit=True)

        cmds.setAttr((namespace  + ikFkArmRight + '.ikFkSwitch'), 10)

        cmds.xform((namespace + ctlFkShoulderRight), ro=rotShoulder, ws=True)
        cmds.xform((namespace + ctlFkElbowRight), ro=rotElbow, ws=True)
        cmds.xform((namespace + ctlFkWristRight), ro=rotWrist, ws=True)
        cmds.xform((namespace + ctlFkShoulderRight), t=posShoulder, ws=True)
        cmds.xform((namespace + ctlFkElbowRight), t=posElbow, ws=True)
        cmds.xform((namespace + ctlFkWristRight), t=posWrist, ws=True)

        if insertKey:
            cmds.setKeyframe([namespace + ctlIkArmPositionRight, namespace + ctlIkArmPoleVectorRight, namespace + ctlIkArmRight, namespace + ctlFkShoulderRight, namespace + ctlFkElbowRight, namespace + ctlFkWristRight, namespace + ikFkArmRight], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.autoKeyframe(state=prevStatusAutoKey)

#=================================================================================================================================================
#
# SIGNATURE:
#    matchFkToIkRightArm(namespace = ':', insertKey=True)
#
# DESCRIPTION:
#    Seamless FK to IK Switch for the Right Arm.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    insertKey - True or False. Sets or not an animation key when the switch is done.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def matchFkToIkRightArm(namespace = ':', insertKey=True):
    if cmds.getAttr((namespace  + ikFkArmRight + '.ikFkSwitch')) == 0:
        showMessage('INFO: Right Arm is already IK.')
    else:
        locRightShoulder = 'tmpLocRightShoulderFkToIk'
        locRightElbow = 'tmpLocRightElbowFkToIk'
        locRightWrist = 'tmpLocRightWristFkToIk'
        locRightPoleVectorOff = 'locRightPoleVectorOffFkToIk'
        locRightPoleVector = 'locRightPoleVectorFkToIk'

        cmds.spaceLocator(n=locRightShoulder)
        cmds.spaceLocator(n=locRightElbow)
        cmds.spaceLocator(n=locRightWrist)
        cmds.spaceLocator(n=locRightPoleVectorOff)
        cmds.spaceLocator(n=locRightPoleVector)
        cmds.parent(locRightPoleVector, locRightPoleVectorOff)

        cmds.setAttr((locRightShoulder + '.ro'), cmds.getAttr(namespace + jntShoulderRight + '.ro'))
        cmds.setAttr((locRightElbow + '.ro'), cmds.getAttr(namespace + jntElbowRotRight + '.ro'))
        cmds.setAttr((locRightWrist + '.ro'), cmds.getAttr(namespace + jntWristRotRight + '.ro'))
        cmds.setAttr((locRightPoleVectorOff + '.ro'), cmds.getAttr(namespace + jntElbowRotRight + '.ro'))
        cmds.setAttr((locRightPoleVector + '.ro'), cmds.getAttr(namespace + jntElbowRotRight + '.ro'))

        posShoulder = cmds.xform((namespace + jntShoulderRight), q=True, t=True, ws=True)
        posElbow = cmds.xform((namespace + jntElbowPosRight), q=True, t=True, ws=True)
        posWrist = cmds.xform((namespace + jntWristPosRight), q=True, t=True, ws=True)
        rotShoulder = cmds.xform((namespace + jntShoulderRight), q=True, ro=True, ws=True)
        rotElbow = cmds.xform((namespace + jntElbowRotRight), q=True, ro=True, ws=True)
        rotWrist = cmds.xform((namespace + jntWristRotRight), q=True, ro=True, ws=True)

        cmds.xform(locRightShoulder, t=posShoulder, ws=True)
        cmds.xform(locRightElbow, t=posElbow, ws=True)
        cmds.xform(locRightWrist, t=posWrist, ws=True)
        cmds.xform(locRightShoulder, ro=rotShoulder, ws=True)
        cmds.xform(locRightElbow, ro=rotElbow, ws=True)
        cmds.xform(locRightWrist, ro=rotWrist, ws=True)

        prevStatusAutoKey = 0
        if insertKey:
            prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
            cmds.autoKeyframe(state=False)
            cmds.currentTime(cmds.currentTime(q=True) - 1, edit=True)
            cmds.setKeyframe([namespace + ctlIkArmPositionRight, namespace + ctlIkArmPoleVectorRight, namespace + ctlIkArmRight, namespace + ctlFkShoulderRight, namespace + ctlFkElbowRight, namespace + ctlFkWristRight, namespace + ikFkArmRight], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.currentTime(cmds.currentTime(q=True) + 1, edit=True)

        cmds.setAttr((namespace  + ikFkArmRight + '.ikFkSwitch'), 0)

        cmds.xform((namespace + ctlIkArmPositionRight), ro=rotShoulder, ws=True)
        cmds.xform((namespace + ctlIkArmRight), ro=rotWrist, ws=True)
        cmds.xform((namespace + ctlIkArmPositionRight), t=posShoulder, ws=True)
        cmds.xform((namespace + ctlIkArmRight), t=posWrist, ws=True)

        cmds.xform(locRightPoleVectorOff, ro=rotElbow, ws=True)
        cmds.xform(locRightPoleVectorOff, t=posElbow, ws=True)
        cmds.setAttr((locRightPoleVector + '.tz'), 7.5)
        posPoleVector = cmds.xform(locRightPoleVector, q=True, t=True, ws=True)
        cmds.xform((namespace + ctlIkArmPoleVectorRight), t=posPoleVector, ws=True)

        cmds.delete([locRightShoulder, locRightElbow, locRightWrist, locRightPoleVectorOff, locRightPoleVector])

        if insertKey:
            cmds.setKeyframe([namespace + ctlIkArmPositionRight, namespace + ctlIkArmPoleVectorRight, namespace + ctlIkArmRight, namespace + ctlFkShoulderRight, namespace + ctlFkElbowRight, namespace + ctlFkWristRight, namespace + ikFkArmRight], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.autoKeyframe(state=prevStatusAutoKey)

#=================================================================================================================================================
#
# SIGNATURE:
#    matchIkToFkLeftLeg(namespace = ':', insertKey=True)
#
# DESCRIPTION:
#    Seamless IK to FK Switch for the Left Leg.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    insertKey - True or False. Sets or not an animation key when the switch is done.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def matchIkToFkLeftLeg(namespace = ':', insertKey=True):
    if cmds.getAttr((namespace  + ikFkLegLeft + '.ikFkSwitch')) == 10:
        showMessage('INFO: Left Leg is already FK.')
    else:
        posHip = cmds.xform((namespace + jntHipLeft), q=True, t=True, ws=True)
        posKnee = cmds.xform((namespace + jntKneePosLeft), q=True, t=True, ws=True)
        posAnkle = cmds.xform((namespace + jntAnklePosLeft), q=True, t=True, ws=True)
        posToe = cmds.xform((namespace + jntToeLeft), q=True, t=True, ws=True)
        rotHip = cmds.xform((namespace + jntHipLeft), q=True, ro=True, ws=True)
        rotKnee = cmds.xform((namespace + jntKneeRotLeft), q=True, ro=True, ws=True)
        rotAnkle = cmds.xform((namespace + jntAnkleRotLeft), q=True, ro=True, ws=True)
        rotToe = cmds.xform((namespace + jntToeLeft), q=True, ro=True, ws=True)

        prevStatusAutoKey = 0
        if insertKey:
            prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
            cmds.autoKeyframe(state=False)
            cmds.currentTime(cmds.currentTime(q=True) - 1, edit=True)
            cmds.setKeyframe([namespace + ctlIkLegPositionLeft, namespace + ctlIkLegPoleVectorLeft, namespace + ctlIkLegLeft, namespace + ctlFkHipLeft, namespace + ctlFkKneeLeft, namespace + ctlFkAnkleLeft, namespace + ctlFkToeLeft, namespace + ikFkLegLeft], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.currentTime(cmds.currentTime(q=True) + 1, edit=True)

        cmds.setAttr((namespace  + ikFkLegLeft + '.ikFkSwitch'), 10)
    
        cmds.xform((namespace + ctlFkHipLeft), ro=rotHip, ws=True)
        cmds.xform((namespace + ctlFkKneeLeft), ro=rotKnee, ws=True)
        cmds.xform((namespace + ctlFkAnkleLeft), ro=rotAnkle, ws=True)
        cmds.xform((namespace + ctlFkToeLeft), ro=rotToe, ws=True)

        cmds.xform((namespace + ctlFkHipLeft), t=posHip, ws=True)
        cmds.xform((namespace + ctlFkKneeLeft), t=posKnee, ws=True)
        cmds.xform((namespace + ctlFkAnkleLeft), t=posAnkle, ws=True)
        cmds.xform((namespace + ctlFkToeLeft), t=posToe, ws=True)


        cmds.setAttr((namespace  + ctlFkToeLeft + '.rx'), cmds.getAttr((namespace  + ctlFkToeLeft + '.rx')) - 90) #Offset of the X rotation of the Fk Toe Control.

        if insertKey:
            cmds.setKeyframe([namespace + ctlIkLegPositionLeft, namespace + ctlIkLegPoleVectorLeft, namespace + ctlIkLegLeft, namespace + ctlFkHipLeft, namespace + ctlFkKneeLeft, namespace + ctlFkAnkleLeft, namespace + ctlFkToeLeft, namespace + ikFkLegLeft], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.autoKeyframe(state=prevStatusAutoKey)

#=================================================================================================================================================
#
# SIGNATURE:
#    matchFkToIkLeftLeg(namespace = ':', insertKey=True)
#
# DESCRIPTION:
#    Seamless FK to IK Switch for the Left Leg.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    insertKey - True or False. Sets or not an animation key when the switch is done.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def matchFkToIkLeftLeg(namespace = ':', insertKey=True):
    if cmds.getAttr((namespace  + ikFkLegLeft + '.ikFkSwitch')) == 0:
        showMessage('INFO: Left Leg is already IK.')
    else:
        locLeftHip = 'locLeftHipFkToIk'
        locLeftKnee = 'locLeftKneeFkToIk'
        locLeftAnkle = 'locLeftAnkleFkToIk'
        locLeftAnkleCompensation = 'locLeftAnkleCompensationFkToIk'
        locLeftPoleVectorOff = 'locLeftPoleVectorOffFkToIk'
        locLeftPoleVector = 'locLeftPoleVectorFkToIk'

        toeRotZ = cmds.getAttr((namespace + jntToeLeft + '.rz')) * -1
    
        cmds.spaceLocator(n=locLeftHip)
        cmds.spaceLocator(n=locLeftKnee)
        cmds.spaceLocator(n=locLeftAnkle)
        cmds.spaceLocator(n=locLeftAnkleCompensation)
        cmds.spaceLocator(n=locLeftPoleVectorOff)
        cmds.spaceLocator(n=locLeftPoleVector)
        cmds.parent(locLeftPoleVector, locLeftPoleVectorOff)
        cmds.parent(locLeftAnkleCompensation, locLeftAnkle)

        cmds.setAttr((locLeftHip + '.ro'), cmds.getAttr(namespace + jntHipLeft + '.ro'))
        cmds.setAttr((locLeftKnee + '.ro'), cmds.getAttr(namespace + jntKneeRotLeft + '.ro'))
        cmds.setAttr((locLeftAnkle + '.ro'), cmds.getAttr(namespace + jntAnkleRotLeft + '.ro'))
        cmds.setAttr((locLeftAnkleCompensation + '.ro'), cmds.getAttr(namespace + jntAnkleRotLeft + '.ro'))
        cmds.setAttr((locLeftPoleVectorOff + '.ro'), cmds.getAttr(namespace + jntKneeRotLeft + '.ro'))
        cmds.setAttr((locLeftPoleVector + '.ro'), cmds.getAttr(namespace + jntKneeRotLeft + '.ro'))

        posHip = cmds.xform((namespace + jntHipLeft), q=True, t=True, ws=True)
        posKnee = cmds.xform((namespace + jntKneePosLeft), q=True, t=True, ws=True)
        posAnkle = cmds.xform((namespace + jntAnklePosLeft), q=True, t=True, ws=True)
        rotHip = cmds.xform((namespace + jntHipLeft), q=True, ro=True, ws=True)
        rotKnee = cmds.xform((namespace + jntKneeRotLeft), q=True, ro=True, ws=True)
        rotAnkle = cmds.xform((namespace + jntAnkleRotLeft), q=True, ro=True, ws=True)

        cmds.xform(locLeftHip, t=posHip, ws=True)
        cmds.xform(locLeftKnee, t=posKnee, ws=True)
        cmds.xform(locLeftAnkle, t=posAnkle, ws=True)
        cmds.xform(locLeftHip, ro=rotHip, ws=True)
        cmds.xform(locLeftKnee, ro=rotKnee, ws=True)
        cmds.xform(locLeftAnkle, ro=rotAnkle, ws=True)

        prevStatusAutoKey = 0
        if insertKey:
            prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
            cmds.autoKeyframe(state=False)
            cmds.currentTime(cmds.currentTime(q=True) - 1, edit=True)
            cmds.setKeyframe([namespace + ctlIkLegPositionLeft, namespace + ctlIkLegPoleVectorLeft, namespace + ctlIkLegLeft, namespace + ctlFkHipLeft, namespace + ctlFkKneeLeft, namespace + ctlFkAnkleLeft, namespace + ctlFkToeLeft, namespace + ikFkLegLeft], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.currentTime(cmds.currentTime(q=True) + 1, edit=True)

        cmds.setAttr((namespace  + ikFkLegLeft + '.ikFkSwitch'), 0)

        cmds.setAttr((locLeftAnkleCompensation + '.ry'), cmds.getAttr((locLeftAnkleCompensation + '.ry')) - 21.865) #Offset of the rotation of the Ik Leg Control.
        rotAnkle = cmds.xform(locLeftAnkleCompensation, q=True, ro=True, ws=True)

        cmds.xform((namespace + ctlIkLegPositionLeft), ro=rotHip, ws=True)
        cmds.xform((namespace + ctlIkLegLeft), ro=rotAnkle, ws=True)
        cmds.setAttr((namespace + ctlIkLegLeft + '.toeTilt'), toeRotZ)
        cmds.xform((namespace + ctlIkLegPositionLeft), t=posHip, ws=True)
        cmds.xform((namespace + ctlIkLegLeft), t=posAnkle, ws=True)

        cmds.xform(locLeftPoleVectorOff, ro=rotKnee, ws=True)
        cmds.xform(locLeftPoleVectorOff, t=posKnee, ws=True)
        cmds.setAttr((locLeftPoleVector + '.tz'), 7.5)
        posPoleVector = cmds.xform(locLeftPoleVector, q=True, t=True, ws=True)
        cmds.xform((namespace + ctlIkLegPoleVectorLeft), t=posPoleVector, ws=True)

        cmds.delete([locLeftHip, locLeftKnee, locLeftAnkle, locLeftAnkleCompensation, locLeftPoleVectorOff, locLeftPoleVector])

        if insertKey:
            cmds.setKeyframe([namespace + ctlIkLegPositionLeft, namespace + ctlIkLegPoleVectorLeft, namespace + ctlIkLegLeft, namespace + ctlFkHipLeft, namespace + ctlFkKneeLeft, namespace + ctlFkAnkleLeft, namespace + ctlFkToeLeft, namespace + ikFkLegLeft], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.autoKeyframe(state=prevStatusAutoKey)

#=================================================================================================================================================
#
# SIGNATURE:
#    matchIkToFkRightLeg(namespace = ':', insertKey=True)
#
# DESCRIPTION:
#    Seamless IK to FK Switch for the Right Leg.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    insertKey - True or False. Sets or not an animation key when the switch is done.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def matchIkToFkRightLeg(namespace = ':', insertKey=True):
    if cmds.getAttr((namespace  + ikFkLegRight + '.ikFkSwitch')) == 10:
        showMessage('INFO: Right Leg is already FK.')
    else:
        posHip = cmds.xform((namespace + jntHipRight), q=True, t=True, ws=True)
        posKnee = cmds.xform((namespace + jntKneePosRight), q=True, t=True, ws=True)
        posAnkle = cmds.xform((namespace + jntAnklePosRight), q=True, t=True, ws=True)
        posToe = cmds.xform((namespace + jntToeRight), q=True, t=True, ws=True)
        rotHip = cmds.xform((namespace + jntHipRight), q=True, ro=True, ws=True)
        rotKnee = cmds.xform((namespace + jntKneeRotRight), q=True, ro=True, ws=True)
        rotAnkle = cmds.xform((namespace + jntAnkleRotRight), q=True, ro=True, ws=True)
        rotToe = cmds.xform((namespace + jntToeRight), q=True, ro=True, ws=True)

        prevStatusAutoKey = 0
        if insertKey:
            prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
            cmds.autoKeyframe(state=False)
            cmds.currentTime(cmds.currentTime(q=True) - 1, edit=True)
            cmds.setKeyframe([namespace + ctlIkLegPositionRight, namespace + ctlIkLegPoleVectorRight, namespace + ctlIkLegRight, namespace + ctlFkHipRight, namespace + ctlFkKneeRight, namespace + ctlFkAnkleRight, namespace + ctlFkToeRight, namespace + ikFkLegRight], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.currentTime(cmds.currentTime(q=True) + 1, edit=True)

        cmds.setAttr((namespace  + ikFkLegRight + '.ikFkSwitch'), 10)
    
        cmds.xform((namespace + ctlFkHipRight), ro=rotHip, ws=True)
        cmds.xform((namespace + ctlFkKneeRight), ro=rotKnee, ws=True)
        cmds.xform((namespace + ctlFkAnkleRight), ro=rotAnkle, ws=True)
        cmds.xform((namespace + ctlFkToeRight), ro=rotToe, ws=True)
        cmds.xform((namespace + ctlFkHipRight), t=posHip, ws=True)
        cmds.xform((namespace + ctlFkKneeRight), t=posKnee, ws=True)
        cmds.xform((namespace + ctlFkAnkleRight), t=posAnkle, ws=True)
        cmds.xform((namespace + ctlFkToeRight), t=posToe, ws=True)

        cmds.setAttr((namespace  + ctlFkToeRight + '.rx'), cmds.getAttr((namespace  + ctlFkToeRight + '.rx')) - 90) #Offset of the X rotation of the Fk Toe Control.

        if insertKey:
            cmds.setKeyframe([namespace + ctlIkLegPositionRight, namespace + ctlIkLegPoleVectorRight, namespace + ctlIkLegRight, namespace + ctlFkHipRight, namespace + ctlFkKneeRight, namespace + ctlFkAnkleRight, namespace + ctlFkToeRight, namespace + ikFkLegRight], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.autoKeyframe(state=prevStatusAutoKey)

#=================================================================================================================================================
#
# SIGNATURE:
#    matchFkToIkRightLeg(namespace = ':', insertKey=True)
#
# DESCRIPTION:
#    Seamless FK to IK Switch for the Right Leg.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    insertKey - True or False. Sets or not an animation key when the switch is done.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def matchFkToIkRightLeg(namespace = ':', insertKey=True):
    if cmds.getAttr((namespace  + ikFkLegRight + '.ikFkSwitch')) == 0:
        showMessage('INFO: Right Leg is already IK.')
    else:
        locRightHip = 'locRightHipFkToIk'
        locRightKnee = 'locRightKneeFkToIk'
        locRightAnkle = 'locRightAnkleFkToIk'
        locRightAnkleCompensation = 'locRightAnkleCompensationFkToIk'
        locRightPoleVectorOff = 'locRightPoleVectorOffFkToIk'
        locRightPoleVector = 'locRightPoleVectorFkToIk'

        toeRotZ = cmds.getAttr((namespace + jntToeRight + '.rz')) * -1

        cmds.spaceLocator(n=locRightHip)
        cmds.spaceLocator(n=locRightKnee)
        cmds.spaceLocator(n=locRightAnkle)
        cmds.spaceLocator(n=locRightAnkleCompensation)
        cmds.spaceLocator(n=locRightPoleVectorOff)
        cmds.spaceLocator(n=locRightPoleVector)
        cmds.parent(locRightPoleVector, locRightPoleVectorOff)
        cmds.parent(locRightAnkleCompensation, locRightAnkle)

        cmds.setAttr((locRightHip + '.ro'), cmds.getAttr(namespace + jntHipRight + '.ro'))
        cmds.setAttr((locRightKnee + '.ro'), cmds.getAttr(namespace + jntKneeRotRight + '.ro'))
        cmds.setAttr((locRightAnkle + '.ro'), cmds.getAttr(namespace + jntAnkleRotRight + '.ro'))
        cmds.setAttr((locRightAnkleCompensation + '.ro'), cmds.getAttr(namespace + jntAnkleRotRight + '.ro'))
        cmds.setAttr((locRightPoleVectorOff + '.ro'), cmds.getAttr(namespace + jntKneeRotRight + '.ro'))
        cmds.setAttr((locRightPoleVector + '.ro'), cmds.getAttr(namespace + jntKneeRotRight + '.ro'))

        posHip = cmds.xform((namespace + jntHipRight), q=True, t=True, ws=True)
        posKnee = cmds.xform((namespace + jntKneePosRight), q=True, t=True, ws=True)
        posAnkle = cmds.xform((namespace + jntAnklePosRight), q=True, t=True, ws=True)
        rotHip = cmds.xform((namespace + jntHipRight), q=True, ro=True, ws=True)
        rotKnee = cmds.xform((namespace + jntKneeRotRight), q=True, ro=True, ws=True)
        rotAnkle = cmds.xform((namespace + jntAnkleRotRight), q=True, ro=True, ws=True)

        cmds.xform(locRightHip, t=posHip, ws=True)
        cmds.xform(locRightKnee, t=posKnee, ws=True)
        cmds.xform(locRightAnkle, t=posAnkle, ws=True)
        cmds.xform(locRightHip, ro=rotHip, ws=True)
        cmds.xform(locRightKnee, ro=rotKnee, ws=True)
        cmds.xform(locRightAnkle, ro=rotAnkle, ws=True)

        prevStatusAutoKey = 0
        if insertKey:
            prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
            cmds.autoKeyframe(state=False)
            cmds.currentTime(cmds.currentTime(q=True) - 1, edit=True)
            cmds.setKeyframe([namespace + ctlIkLegPositionRight, namespace + ctlIkLegPoleVectorRight, namespace + ctlIkLegRight, namespace + ctlFkHipRight, namespace + ctlFkKneeRight, namespace + ctlFkAnkleRight, namespace + ctlFkToeRight, namespace + ikFkLegRight], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.currentTime(cmds.currentTime(q=True) + 1, edit=True)

        cmds.setAttr((namespace  + ikFkLegRight + '.ikFkSwitch'), 0)

        cmds.setAttr((locRightAnkleCompensation + '.rx'), cmds.getAttr((locRightAnkleCompensation + '.rx')) * 1) #Offset of the rotation of the Ik Leg Control.
        cmds.setAttr((locRightAnkleCompensation + '.ry'), cmds.getAttr((locRightAnkleCompensation + '.ry')) - 21.865 + 180) #Offset of the rotation of the Ik Leg Control.
        cmds.setAttr((locRightAnkleCompensation + '.rz'), cmds.getAttr((locRightAnkleCompensation + '.rz')) * -1) #Offset of the rotation of the Ik Leg Control.
        rotAnkle = cmds.xform(locRightAnkleCompensation, q=True, ro=True, ws=True)

        cmds.xform((namespace + ctlIkLegPositionRight), ro=rotHip, ws=True)
        cmds.xform((namespace + ctlIkLegRight), ro=rotAnkle, ws=True)
        cmds.setAttr((namespace + ctlIkLegRight + '.toeTilt'), toeRotZ)
        cmds.xform((namespace + ctlIkLegPositionRight), t=posHip, ws=True)
        cmds.xform((namespace + ctlIkLegRight), t=posAnkle, ws=True)

        cmds.xform(locRightPoleVectorOff, ro=rotKnee, ws=True)
        cmds.xform(locRightPoleVectorOff, t=posKnee, ws=True)
        cmds.setAttr((locRightPoleVector + '.tz'), -7.5)
        posPoleVector = cmds.xform(locRightPoleVector, q=True, t=True, ws=True)
        cmds.xform((namespace + ctlIkLegPoleVectorRight), t=posPoleVector, ws=True)

        cmds.delete([locRightHip, locRightKnee, locRightAnkle, locRightAnkleCompensation, locRightPoleVectorOff, locRightPoleVector])

        if insertKey:
            cmds.setKeyframe([namespace + ctlIkLegPositionRight, namespace + ctlIkLegPoleVectorRight, namespace + ctlIkLegRight, namespace + ctlFkHipRight, namespace + ctlFkKneeRight, namespace + ctlFkAnkleRight, namespace + ctlFkToeRight, namespace + ikFkLegRight], breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.autoKeyframe(state=prevStatusAutoKey)



#MIRROR/FLIP =====================================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    mirrorAllLeftToRightWorldSpace(namespace = ':')
#
# DESCRIPTION:
#    Preprocess. Mirror all controls Left to Right. World Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def mirrorAllLeftToRightWorldSpace(namespace = ':'):
    allItems = listAllControls
    leftItems = []

    for eachItem in allItems:
        if eachItem.endswith('Left'):
            leftItems.append(namespace + eachItem)

    doMirrorLeftToRightWorldSpace(namespace, leftItems)

#=================================================================================================================================================
#
# SIGNATURE:
#    mirrorAllLeftToRightRootRelative(namespace = ':')
#
# DESCRIPTION:
#    Preprocess. Mirror all controls Left to Right. Root Relative Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def mirrorAllLeftToRightRootRelative(namespace = ':'):
    allItems = listAllControls
    leftItems = []
    rightItems = []
    leftLocators = []
    rightLocators = []

    for eachItem in allItems:
        if eachItem.endswith('Left'):
            leftItems.append(namespace + eachItem)

            locName = eachItem.replace('ctl', 'tmpLoc')
            cmds.spaceLocator(n=locName)
            leftLocators.append(locName)
            cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + eachItem + '.ro'))

        elif eachItem.endswith('Right'):
            rightItems.append(namespace + eachItem)

            locName = eachItem.replace('ctl', 'tmpLoc')
            cmds.spaceLocator(n=locName)
            rightLocators.append(locName)
            cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + eachItem + '.ro'))

    doMirrorLeftToRightRootRelative(namespace, leftItems, rightItems, leftLocators, rightLocators)

#=================================================================================================================================================
#
# SIGNATURE:
#    mirrorAllRightToLeftWorldSpace(namespace = ':')
#
# DESCRIPTION:
#    Preprocess. Mirror all controls Right to Left. World Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def mirrorAllRightToLeftWorldSpace(namespace = ':'):
    allItems = listAllControls
    rightItems = []

    for eachItem in allItems:
        if eachItem.endswith('Right'):
            rightItems.append(namespace + eachItem)

    doMirrorRightToLeftWorldSpace(namespace, rightItems)

#=================================================================================================================================================
#
# SIGNATURE:
#    mirrorAllRightToLeftRootRelative(namespace = ':')
#
# DESCRIPTION:
#    Preprocess. Mirror all controls Right to Left. Root Relative Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def mirrorAllRightToLeftRootRelative(namespace = ':'):
    allItems = listAllControls
    leftItems = []
    rightItems = []
    leftLocators = []
    rightLocators = []

    for eachItem in allItems:
        if eachItem.endswith('Left'):
            leftItems.append(namespace + eachItem)

            locName = eachItem.replace('ctl', 'tmpLoc')
            cmds.spaceLocator(n=locName)
            leftLocators.append(locName)
            cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + eachItem + '.ro'))

        elif eachItem.endswith('Right'):
            rightItems.append(namespace + eachItem)

            locName = eachItem.replace('ctl', 'tmpLoc')
            cmds.spaceLocator(n=locName)
            rightLocators.append(locName)
            cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + eachItem + '.ro'))

    doMirrorRightToLeftRootRelative(namespace, leftItems, rightItems, leftLocators, rightLocators)

#=================================================================================================================================================
#
# SIGNATURE:
#    flipAllWorldSpace(namespace = ':')
#
# DESCRIPTION:
#    Preprocess. Flip all controls positions. World Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def flipAllWorldSpace(namespace = ':'):
    allItems = listAllControls
    leftItems = []

    for eachItem in allItems:
        if eachItem.endswith('Left') or eachItem.endswith('Middle'):
            leftItems.append(namespace + eachItem)

    doFlipWorldSpace(namespace, leftItems)

#=================================================================================================================================================
#
# SIGNATURE:
#    flipAllRootRelative(namespace = ':')
#
# DESCRIPTION:
#    Preprocess. Flip all controls positions. Root Relative Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def flipAllRootRelative(namespace = ':'):
    allItems = listAllControls
    leftItems = []
    rightItems = []
    middleItems = []

    leftLocators = []
    rightLocators = []

    leftFlipLocators = []
    rightFlipLocators = []

    for eachItem in allItems:
        if eachItem.endswith('Left'):
            leftItems.append(namespace + eachItem)

            locName = eachItem.replace('ctl', 'tmpLoc')
            cmds.spaceLocator(n=locName)
            leftLocators.append(locName)
            cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + eachItem + '.ro'))

            locName = eachItem.replace('ctl', 'tmpLocFlip')
            cmds.spaceLocator(n=locName)
            leftFlipLocators.append(locName)
            cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + eachItem + '.ro'))

            rightEachItem = eachItem.replace('Left', 'Right')
            rightItems.append(namespace + rightEachItem)

            locName = rightEachItem.replace('ctl', 'tmpLoc')
            cmds.spaceLocator(n=locName)
            rightLocators.append(locName)
            cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + rightEachItem + '.ro'))

            locName = rightEachItem.replace('ctl', 'tmpLocFlip')
            cmds.spaceLocator(n=locName)
            rightFlipLocators.append(locName)
            cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + rightEachItem + '.ro'))

        elif eachItem.endswith('Middle'):
            middleItems.append(namespace + eachItem)

    doFlipRootRelative(namespace, leftItems, rightItems, middleItems, leftLocators, rightLocators, leftFlipLocators, rightFlipLocators)

#=================================================================================================================================================
#
# SIGNATURE:
#    mirrorSelectedLeftToRightWorldSpace(namespace = ':', objSelected = None)
#
# DESCRIPTION:
#    Preprocess. Mirror selected controls Left to Right. World Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#     objSelected - Selected objects.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def mirrorSelectedLeftToRightWorldSpace(namespace = ':', objSelected = None):
    allItems = listAllControls
    leftItems = []

    for eachItem in allItems:
        if eachItem.endswith('Left') and (namespace + eachItem) in objSelected:
            leftItems.append(namespace + eachItem)

    doMirrorLeftToRightWorldSpace(namespace, leftItems)

    cmds.select(objSelected, r=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    mirrorSelectedLeftToRightRootRelative(namespace = ':', objSelected = None)
#
# DESCRIPTION:
#    Preprocess. Mirror selected controls Left to Right. Rott Relative Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#     objSelected - Selected objects.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def mirrorSelectedLeftToRightRootRelative(namespace = ':', objSelected = None):
    allItems = listAllControls
    leftItems = []
    rightItems = []
    leftLocators = []
    rightLocators = []

    for eachItem in allItems:
        if eachItem.endswith('Left') and (namespace + eachItem) in objSelected:
            leftItems.append(namespace + eachItem)

            locName = eachItem.replace('ctl', 'tmpLoc')
            cmds.spaceLocator(n=locName)
            leftLocators.append(locName)
            cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + eachItem + '.ro'))

            rightEachItem = eachItem.replace('Left', 'Right')
            rightItems.append(namespace + rightEachItem)

            locName = rightEachItem.replace('ctl', 'tmpLoc')
            cmds.spaceLocator(n=locName)
            rightLocators.append(locName)
            cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + rightEachItem + '.ro'))

    doMirrorLeftToRightRootRelative(namespace, leftItems, rightItems, leftLocators, rightLocators)

    cmds.select(objSelected, r=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    mirrorSelectedRightToLeftWorldSpace(namespace = ':', objSelected = None)
#
# DESCRIPTION:
#    Preprocess. Mirror selected controls Right to Left. World Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#     objSelected - Selected objects.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def mirrorSelectedRightToLeftWorldSpace(namespace = ':', objSelected = None):
    allItems = listAllControls
    rightItems = []

    for eachItem in allItems:
        if eachItem.endswith('Right') and (namespace + eachItem) in objSelected:
            rightItems.append(namespace + eachItem)

    doMirrorRightToLeftWorldSpace(namespace, rightItems)

    cmds.select(objSelected, r=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    mirrorSelectedRightToLeftRootRelative(namespace = ':', objSelected = None)
#
# DESCRIPTION:
#    Preprocess. Mirror selected controls Right to Left. Root Relative Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#     objSelected - Selected objects.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def mirrorSelectedRightToLeftRootRelative(namespace = ':', objSelected = None):
    allItems = listAllControls
    leftItems = []
    rightItems = []
    leftLocators = []
    rightLocators = []

    for eachItem in allItems:
        if eachItem.endswith('Right') and (namespace + eachItem) in objSelected:
            rightItems.append(namespace + eachItem)

            locName = eachItem.replace('ctl', 'tmpLoc')
            cmds.spaceLocator(n=locName)
            rightLocators.append(locName)
            cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + eachItem + '.ro'))

            leftEachItem = eachItem.replace('Right', 'Left')
            leftItems.append(namespace + leftEachItem)

            locName = leftEachItem.replace('ctl', 'tmpLoc')
            cmds.spaceLocator(n=locName)
            leftLocators.append(locName)
            cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + leftEachItem + '.ro'))

    doMirrorRightToLeftRootRelative(namespace, leftItems, rightItems, leftLocators, rightLocators)

    cmds.select(objSelected, r=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    flipSelectedWorldSpace(namespace = ':', objSelected = None)
#
# DESCRIPTION:
#    Preprocess. Flip all controls positions. World Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#     objSelected - Selected objects.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def flipSelectedWorldSpace(namespace = ':', objSelected = None):
    allItems = listAllControls
    leftItems = []

    for eachItem in allItems:
        if (eachItem.endswith('Left') or eachItem.endswith('Middle') or eachItem.endswith('Right')) and (namespace + eachItem) in objSelected:
            if eachItem.endswith('Right'):
                eachItem = eachItem.replace('Right', 'Left')

            if (namespace + eachItem) not in leftItems:
                leftItems.append(namespace + eachItem)

    doFlipWorldSpace(namespace, leftItems)

    cmds.select(objSelected, r=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    flipSelectedWorldSpace(namespace = ':', objSelected = None)
#
# DESCRIPTION:
#    Preprocess. Flip all controls positions. Root Relative Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#     objSelected - Selected objects.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def flipSelectedRootRelative(namespace = ':', objSelected = None):
    allItems = listAllControls
    leftItems = []
    rightItems = []
    middleItems = []

    leftLocators = []
    rightLocators = []

    leftFlipLocators = []
    rightFlipLocators = []

    for eachItem in allItems:
        if (eachItem.endswith('Left') or eachItem.endswith('Right')) and (namespace + eachItem) in objSelected:
            if eachItem.endswith('Right'):
                eachItem = eachItem.replace('Right', 'Left')

            if (namespace + eachItem) not in leftItems:
                leftItems.append(namespace + eachItem)

                locName = eachItem.replace('ctl', 'tmpLoc')
                cmds.spaceLocator(n=locName)
                leftLocators.append(locName)
                cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + eachItem + '.ro'))

                locName = eachItem.replace('ctl', 'tmpLocFlip')
                cmds.spaceLocator(n=locName)
                leftFlipLocators.append(locName)
                cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + eachItem + '.ro'))

                rightEachItem = eachItem.replace('Left', 'Right')
                rightItems.append(namespace + rightEachItem)

                locName = rightEachItem.replace('ctl', 'tmpLoc')
                cmds.spaceLocator(n=locName)
                rightLocators.append(locName)
                cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + rightEachItem + '.ro'))

                locName = rightEachItem.replace('ctl', 'tmpLocFlip')
                cmds.spaceLocator(n=locName)
                rightFlipLocators.append(locName)
                cmds.setAttr((locName + '.ro'), cmds.getAttr(namespace + rightEachItem + '.ro'))

        elif eachItem.endswith('Middle') and (namespace + eachItem) in objSelected:
            middleItems.append(namespace + eachItem)

    doFlipRootRelative(namespace, leftItems, rightItems, middleItems, leftLocators, rightLocators, leftFlipLocators, rightFlipLocators)

    cmds.select(objSelected, r=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    doMirrorLeftToRightWorldSpace(namespace = ':', leftItems = None)
#
# DESCRIPTION:
#    Mirror Left to Right. World Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    leftItems - List of the Items to Mirror.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def doMirrorLeftToRightWorldSpace(namespace = ':', leftItems = None):
    prevStatusAutoKey = 0
    prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
    cmds.autoKeyframe(state=False)

    for i in range(0, len(leftItems)):
        if leftItems[i].find('Fk') > -1:
            if not cmds.getAttr((leftItems[i] + '.tx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'), l=True):
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), cmds.getAttr((leftItems[i] + '.tx')) * -1)
            if not cmds.getAttr((leftItems[i] + '.ty'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty'), l=True):
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), cmds.getAttr((leftItems[i] + '.ty')) * -1)
            if not cmds.getAttr((leftItems[i] + '.tz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'), l=True):
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), cmds.getAttr((leftItems[i] + '.tz')) * -1)

            if not cmds.getAttr((leftItems[i] + '.rx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'), l=True):
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rx'), cmds.getAttr((leftItems[i] + '.rx')))
            if not cmds.getAttr((leftItems[i] + '.ry'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'), l=True):
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ry'), cmds.getAttr((leftItems[i] + '.ry')))
            if not cmds.getAttr((leftItems[i] + '.rz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz'), l=True):
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rz'), cmds.getAttr((leftItems[i] + '.rz')))

        elif leftItems[i].find('Ik') > -1:
            if leftItems[i].find('Position') > -1:
                if leftItems[i].find('Arm') > -1:
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), cmds.getAttr((leftItems[i] + '.tx')) * -1)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), cmds.getAttr((leftItems[i] + '.ty')) * -1)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), cmds.getAttr((leftItems[i] + '.tz')) * -1)
                elif leftItems[i].find('Leg') > -1:
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), cmds.getAttr((leftItems[i] + '.tx')))
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), cmds.getAttr((leftItems[i] + '.ty')) * -1)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), cmds.getAttr((leftItems[i] + '.tz')))
            else:
                if leftItems[i].find('Arm') > -1:
                    if not cmds.getAttr((leftItems[i] + '.tx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'), l=True):
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), cmds.getAttr((leftItems[i] + '.tx')) * -1)
                    if not cmds.getAttr((leftItems[i] + '.ty'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty'), l=True):
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), cmds.getAttr((leftItems[i] + '.ty')) * -1)
                    if not cmds.getAttr((leftItems[i] + '.tz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'), l=True):
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), cmds.getAttr((leftItems[i] + '.tz')) * -1)

                    if not cmds.getAttr((leftItems[i] + '.rx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'), l=True):
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rx'), cmds.getAttr((leftItems[i] + '.rx')))
                    if not cmds.getAttr((leftItems[i] + '.ry'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'), l=True):
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ry'), cmds.getAttr((leftItems[i] + '.ry')))
                    if not cmds.getAttr((leftItems[i] + '.rz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz'), l=True):
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rz'), cmds.getAttr((leftItems[i] + '.rz')))
                elif leftItems[i].find('Leg') > -1:
                    if not cmds.getAttr((leftItems[i] + '.tx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'), l=True):
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), cmds.getAttr((leftItems[i] + '.tx')))
                    if not cmds.getAttr((leftItems[i] + '.ty'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty'), l=True):
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), cmds.getAttr((leftItems[i] + '.ty')) * -1)
                    if not cmds.getAttr((leftItems[i] + '.tz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'), l=True):
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), cmds.getAttr((leftItems[i] + '.tz')))

                    if not cmds.getAttr((leftItems[i] + '.rx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'), l=True):
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rx'), cmds.getAttr((leftItems[i] + '.rx')))
                    if not cmds.getAttr((leftItems[i] + '.ry'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'), l=True):
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ry'), cmds.getAttr((leftItems[i] + '.ry')))
                    if not cmds.getAttr((leftItems[i] + '.rz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz'), l=True):
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rz'), cmds.getAttr((leftItems[i] + '.rz')) * -1)

        elif leftItems[i].find('Bend') > -1:
            if leftItems[i].find('Arm') > -1 or leftItems[i].find('Forearm') > -1:
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), cmds.getAttr((leftItems[i] + '.tx')) * -1)
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), cmds.getAttr((leftItems[i] + '.ty')))
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), cmds.getAttr((leftItems[i] + '.tz')))
    
            elif leftItems[i].find('Hip') > -1 or leftItems[i].find('Leg') > -1:
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), cmds.getAttr((leftItems[i] + '.tx')))
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), cmds.getAttr((leftItems[i] + '.ty')) * -1)
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), cmds.getAttr((leftItems[i] + '.tz')))

        elif leftItems[i].find('PoleVector') > -1:
            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), cmds.getAttr((leftItems[i] + '.tx')))
            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), cmds.getAttr((leftItems[i] + '.ty')))
            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), cmds.getAttr((leftItems[i] + '.tz')) * -1)

        else:
            if not cmds.getAttr((leftItems[i] + '.tx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'), l=True):
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), cmds.getAttr((leftItems[i] + '.tx')) * -1)
            if not cmds.getAttr((leftItems[i] + '.ty'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty'), l=True):
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), cmds.getAttr((leftItems[i] + '.ty')) * -1)
            if not cmds.getAttr((leftItems[i] + '.tz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'), l=True):
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), cmds.getAttr((leftItems[i] + '.tz')) * -1)

            if not cmds.getAttr((leftItems[i] + '.rx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'), l=True):
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rx'), cmds.getAttr((leftItems[i] + '.rx')))
            if not cmds.getAttr((leftItems[i] + '.ry'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'), l=True):
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ry'), cmds.getAttr((leftItems[i] + '.ry')))
            if not cmds.getAttr((leftItems[i] + '.rz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz'), l=True):
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rz'), cmds.getAttr((leftItems[i] + '.rz')))


        allAttrs = cmds.listAnimatable(leftItems[i])

        for eachAttr in allAttrs:
            simpleAttr = eachAttr.split('.')[1]
            if simpleAttr not in ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ']:
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.' + simpleAttr), cmds.getAttr((leftItems[i] + '.' + simpleAttr)))

    cmds.autoKeyframe(state=prevStatusAutoKey)

#=================================================================================================================================================
#
# SIGNATURE:
#    doMirrorLeftToRightRootRelative(namespace = ':', leftItems = None, rightItems = None, leftLocators = None, rightLocators = None)
#
# DESCRIPTION:
#    Mirror Left to Right. Root Relative Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    leftItems - List of the Left Items to Mirror.
#    rightItems - List of the Right Items to Mirror.
#    leftLocators - List of the Left Locators to use as Helpers.
#    rightLocators - List of the Right Locators to use as Helpers.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def doMirrorLeftToRightRootRelative(namespace = ':', leftItems = None, rightItems = None, leftLocators = None, rightLocators = None):
    prevStatusAutoKey = 0
    prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
    cmds.autoKeyframe(state=False)

    for i in range(0, len(leftItems)):    
        posItem = cmds.xform(leftItems[i], q=True, t=True, ws=True)
        rotItem = cmds.xform(leftItems[i], q=True, ro=True, ws=True)

        cmds.xform(leftLocators[i], t=posItem, ws=True)
        cmds.xform(leftLocators[i], ro=rotItem, ws=True)

        cmds.xform(leftLocators[i].replace('Left', 'Right'), t=posItem, r=True)
        cmds.xform(leftLocators[i].replace('Left', 'Right'), ro=rotItem, r=True)

        cmds.parent(leftLocators[i], (namespace + rootControlName))
        cmds.parent(leftLocators[i].replace('Left', 'Right'), (namespace + rootControlName))

        posItem = cmds.xform(leftLocators[i], q=True, t=True, r=True)
        rotItem = cmds.xform(leftLocators[i], q=True, ro=True, r=True)

        cmds.setAttr((leftLocators[i].replace('Left', 'Right') + '.tx'), posItem[0] * -1)
        cmds.setAttr((leftLocators[i].replace('Left', 'Right') + '.ty'), posItem[1])
        cmds.setAttr((leftLocators[i].replace('Left', 'Right') + '.tz'), posItem[2])
        
        if leftLocators[i].replace('Left', 'Right').find('IkLeg000Right') == -1 and leftLocators[i].replace('Left', 'Right').find('EyeBrow') == -1:
            cmds.setAttr((leftLocators[i].replace('Left', 'Right') + '.rx'), rotItem[0] - 180)
        if leftLocators[i].replace('Left', 'Right').find('IkLeg000Right') == -1 and leftLocators[i].replace('Left', 'Right').find('ctlEyeBrow') == -1:
            cmds.setAttr((leftLocators[i].replace('Left', 'Right') + '.ry'), rotItem[1] * -1)
            cmds.setAttr((leftLocators[i].replace('Left', 'Right') + '.rz'), rotItem[2] * -1)
        
        cmds.parent(leftLocators[i], w=True)
        cmds.parent(leftLocators[i].replace('Left', 'Right'), w=True)
        
        posItem = cmds.xform(leftLocators[i].replace('Left', 'Right'), q=True, t=True, ws=True)
        rotItem = cmds.xform(leftLocators[i].replace('Left', 'Right'), q=True, ro=True, ws=True)

        
        if not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'), l=True):
            cmds.xform(leftItems[i].replace('Left', 'Right'), t=posItem, ws=True)    
        if not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz'), l=True):
            cmds.xform(leftItems[i].replace('Left', 'Right'), ro=rotItem, ws=True)    
        
        
        if leftLocators[i].replace('Left', 'Right').find('IkLeg000Right') > -1:
            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rx'), cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx')) * -1)
            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rz'), cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz')) * -1)
        elif leftLocators[i].replace('Left', 'Right').find('EyeBrowRibbon') > -1:
            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx')) * -1)
            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ry'), cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry')) * -1)
            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rz'), cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz')) * -1)        
        

        allAttrs = cmds.listAnimatable(leftItems[i])

        for eachAttr in allAttrs:
            simpleAttr = eachAttr.split('.')[1]
            if simpleAttr not in ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ']:
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.' + simpleAttr), cmds.getAttr((leftItems[i] + '.' + simpleAttr)))

    if leftLocators:
        cmds.delete(leftLocators)
    if rightLocators:
        cmds.delete(rightLocators)

    cmds.autoKeyframe(state=prevStatusAutoKey)

#=================================================================================================================================================
#
# SIGNATURE:
#    doMirrorRightToLeftWorldSpace(namespace = ':', rightItems = None)
#
# DESCRIPTION:
#    Mirror Right to Left. World Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    rightItems - List of the Items to Mirror.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def doMirrorRightToLeftWorldSpace(namespace = ':', rightItems = None):
    prevStatusAutoKey = 0
    prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
    cmds.autoKeyframe(state=False)

    for i in range(0, len(rightItems)):

        if rightItems[i].find('Fk') > -1:
            if not cmds.getAttr((rightItems[i] + '.tx'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tx'), l=True):
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tx'), cmds.getAttr((rightItems[i] + '.tx')) * -1)
            if not cmds.getAttr((rightItems[i] + '.ty'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ty'), l=True):
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ty'), cmds.getAttr((rightItems[i] + '.ty')) * -1)
            if not cmds.getAttr((rightItems[i] + '.tz'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tz'), l=True):
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tz'), cmds.getAttr((rightItems[i] + '.tz')) * -1)

            if not cmds.getAttr((rightItems[i] + '.rx'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rx'), l=True):
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rx'), cmds.getAttr((rightItems[i] + '.rx')))
            if not cmds.getAttr((rightItems[i] + '.ry'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ry'), l=True):
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ry'), cmds.getAttr((rightItems[i] + '.ry')))
            if not cmds.getAttr((rightItems[i] + '.rz'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rz'), l=True):
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rz'), cmds.getAttr((rightItems[i] + '.rz')))

        elif rightItems[i].find('Ik') > -1:
            if rightItems[i].find('Position') > -1:
                if rightItems[i].find('Arm') > -1:
                    cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tx'), cmds.getAttr((rightItems[i] + '.tx')) * -1)
                    cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ty'), cmds.getAttr((rightItems[i] + '.ty')) * -1)
                    cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tz'), cmds.getAttr((rightItems[i] + '.tz')) * -1)
                elif rightItems[i].find('Leg') > -1:
                    cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tx'), cmds.getAttr((rightItems[i] + '.tx')))
                    cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ty'), cmds.getAttr((rightItems[i] + '.ty')) * -1)
                    cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tz'), cmds.getAttr((rightItems[i] + '.tz')))
            else:
                if rightItems[i].find('Arm') > -1:
                    if not cmds.getAttr((rightItems[i] + '.tx'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tx'), l=True):
                        cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tx'), cmds.getAttr((rightItems[i] + '.tx')) * -1)
                    if not cmds.getAttr((rightItems[i] + '.ty'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ty'), l=True):
                        cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ty'), cmds.getAttr((rightItems[i] + '.ty')) * -1)
                    if not cmds.getAttr((rightItems[i] + '.tz'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tz'), l=True):
                        cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tz'), cmds.getAttr((rightItems[i] + '.tz')) * -1)

                    if not cmds.getAttr((rightItems[i] + '.rx'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rx'), l=True):
                        cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rx'), cmds.getAttr((rightItems[i] + '.rx')))
                    if not cmds.getAttr((rightItems[i] + '.ry'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ry'), l=True):
                        cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ry'), cmds.getAttr((rightItems[i] + '.ry')))
                    if not cmds.getAttr((rightItems[i] + '.rz'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rz'), l=True):
                        cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rz'), cmds.getAttr((rightItems[i] + '.rz')))
                elif rightItems[i].find('Leg') > -1:
                    if not cmds.getAttr((rightItems[i] + '.tx'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tx'), l=True):
                        cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tx'), cmds.getAttr((rightItems[i] + '.tx')))
                    if not cmds.getAttr((rightItems[i] + '.ty'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ty'), l=True):
                        cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ty'), cmds.getAttr((rightItems[i] + '.ty')) * -1)
                    if not cmds.getAttr((rightItems[i] + '.tz'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tz'), l=True):
                        cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tz'), cmds.getAttr((rightItems[i] + '.tz')))

                    if not cmds.getAttr((rightItems[i] + '.rx'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rx'), l=True):
                        cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rx'), cmds.getAttr((rightItems[i] + '.rx')))
                    if not cmds.getAttr((rightItems[i] + '.ry'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ry'), l=True):
                        cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ry'), cmds.getAttr((rightItems[i] + '.ry')))
                    if not cmds.getAttr((rightItems[i] + '.rz'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rz'), l=True):
                        cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rz'), cmds.getAttr((rightItems[i] + '.rz')) * -1)

        elif rightItems[i].find('Bend') > -1:
            if rightItems[i].find('Arm') > -1 or rightItems[i].find('Forearm') > -1:
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tx'), cmds.getAttr((rightItems[i] + '.tx')) * -1)
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ty'), cmds.getAttr((rightItems[i] + '.ty')))
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tz'), cmds.getAttr((rightItems[i] + '.tz')))
    
            elif rightItems[i].find('Hip') > -1 or rightItems[i].find('Leg') > -1:
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tx'), cmds.getAttr((rightItems[i] + '.tx')))
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ty'), cmds.getAttr((rightItems[i] + '.ty')) * -1)
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tz'), cmds.getAttr((rightItems[i] + '.tz')))

        elif rightItems[i].find('PoleVector') > -1:
            cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tx'), cmds.getAttr((rightItems[i] + '.tx')))
            cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ty'), cmds.getAttr((rightItems[i] + '.ty')))
            cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tz'), cmds.getAttr((rightItems[i] + '.tz')) * -1)

        else:
            if not cmds.getAttr((rightItems[i] + '.tx'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tx'), l=True):
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tx'), cmds.getAttr((rightItems[i] + '.tx')) * -1)
            if not cmds.getAttr((rightItems[i] + '.ty'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ty'), l=True):
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ty'), cmds.getAttr((rightItems[i] + '.ty')) * -1)
            if not cmds.getAttr((rightItems[i] + '.tz'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tz'), l=True):
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tz'), cmds.getAttr((rightItems[i] + '.tz')) * -1)

            if not cmds.getAttr((rightItems[i] + '.rx'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rx'), l=True):
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rx'), cmds.getAttr((rightItems[i] + '.rx')))
            if not cmds.getAttr((rightItems[i] + '.ry'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ry'), l=True):
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ry'), cmds.getAttr((rightItems[i] + '.ry')))
            if not cmds.getAttr((rightItems[i] + '.rz'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rz'), l=True):
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rz'), cmds.getAttr((rightItems[i] + '.rz')))


        allAttrs = cmds.listAnimatable(rightItems[i])

        for eachAttr in allAttrs:
            simpleAttr = eachAttr.split('.')[1]
            if simpleAttr not in ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ']:
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.' + simpleAttr), cmds.getAttr((rightItems[i] + '.' + simpleAttr)))

    cmds.autoKeyframe(state=prevStatusAutoKey)

#=================================================================================================================================================
#
# SIGNATURE:
#    doMirrorRightToLeftRootRelative(namespace = ':', leftItems = None, rightItems = None, leftLocators = None, rightLocators = None)
#
# DESCRIPTION:
#    Mirror Right to Left. Root Relative Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    leftItems - List of the Left Items to Mirror.
#    rightItems - List of the Right Items to Mirror.
#    leftLocators - List of the Left Locators to use as Helpers.
#    rightLocators - List of the Right Locators to use as Helpers.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def doMirrorRightToLeftRootRelative(namespace = ':', leftItems = None, rightItems = None, leftLocators = None, rightLocators = None):
    prevStatusAutoKey = 0
    prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
    cmds.autoKeyframe(state=False)

    for i in range(0, len(rightItems)):    
        posItem = cmds.xform(rightItems[i], q=True, t=True, ws=True)
        rotItem = cmds.xform(rightItems[i], q=True, ro=True, ws=True)

        cmds.xform(rightLocators[i], t=posItem, ws=True)
        cmds.xform(rightLocators[i], ro=rotItem, ws=True)

        cmds.xform(rightLocators[i].replace('Right', 'Left'), t=posItem, r=True)
        cmds.xform(rightLocators[i].replace('Right', 'Left'), ro=rotItem, r=True)

        cmds.parent(rightLocators[i], (namespace + rootControlName))
        cmds.parent(rightLocators[i].replace('Right', 'Left'), (namespace + rootControlName))

        posItem = cmds.xform(rightLocators[i], q=True, t=True, r=True)
        rotItem = cmds.xform(rightLocators[i], q=True, ro=True, r=True)

        cmds.setAttr((rightLocators[i].replace('Right', 'Left') + '.tx'), posItem[0] * -1)
        cmds.setAttr((rightLocators[i].replace('Right', 'Left') + '.ty'), posItem[1])
        cmds.setAttr((rightLocators[i].replace('Right', 'Left') + '.tz'), posItem[2])
        
        if rightLocators[i].replace('Right', 'Left').find('IkLeg000Left') == -1 and rightLocators[i].replace('Right', 'Left').find('EyeBrow') == -1:
            cmds.setAttr((rightLocators[i].replace('Right', 'Left') + '.rx'), rotItem[0] - 180)
        if rightLocators[i].replace('Right', 'Left').find('IkLeg000Left') == -1 and rightLocators[i].replace('Right', 'Left').find('ctlEyeBrow') == -1:
            cmds.setAttr((rightLocators[i].replace('Right', 'Left') + '.ry'), rotItem[1] * -1)
            cmds.setAttr((rightLocators[i].replace('Right', 'Left') + '.rz'), rotItem[2] * -1)
        
        cmds.parent(rightLocators[i], w=True)
        cmds.parent(rightLocators[i].replace('Right', 'Left'), w=True)
        
        posItem = cmds.xform(rightLocators[i].replace('Right', 'Left'), q=True, t=True, ws=True)
        rotItem = cmds.xform(rightLocators[i].replace('Right', 'Left'), q=True, ro=True, ws=True)

        
        if not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tx'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ty'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tz'), l=True):
            cmds.xform(rightItems[i].replace('Right', 'Left'), t=posItem, ws=True)    
        if not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rx'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ry'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rz'), l=True):
            cmds.xform(rightItems[i].replace('Right', 'Left'), ro=rotItem, ws=True)    
        
        
        if rightLocators[i].replace('Right', 'Left').find('IkLeg000Left') > -1:
            cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rx'), cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rx')) * -1)
            cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rz'), cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rz')) * -1)
        elif rightLocators[i].replace('Right', 'Left').find('EyeBrowRibbon') > -1:
            cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tx'), cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tx')) * -1)
            cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ry'), cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ry')) * -1)
            cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rz'), cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rz')) * -1)        
        

        allAttrs = cmds.listAnimatable(rightItems[i])

        for eachAttr in allAttrs:
            simpleAttr = eachAttr.split('.')[1]
            if simpleAttr not in ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ']:
                cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.' + simpleAttr), cmds.getAttr((rightItems[i] + '.' + simpleAttr)))

    if leftLocators:
        cmds.delete(leftLocators)
    if rightLocators:
        cmds.delete(rightLocators)

    cmds.autoKeyframe(state=prevStatusAutoKey)

#=================================================================================================================================================
#
# SIGNATURE:
#    doFlipWorldSpace(namespace = ':', leftItems = None, rightItems = None)
#
# DESCRIPTION:
#    Flip Left and Right. World Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    leftItems - List of the Left Items to Flip.
#    rightItems - List of the Right Items to Flip.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def doFlipWorldSpace(namespace = ':', leftItems = None, rightItems = None):
    prevStatusAutoKey = 0
    prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
    cmds.autoKeyframe(state=False)

    for i in range(0, len(leftItems)):

        if leftItems[i].split(':')[-1].endswith('Middle'):
            if leftItems[i].find('Main') > -1 or leftItems[i].find('Root') > -1:
                pass
	    elif leftItems[i].find('Hip') > -1 or leftItems[i].find('Eye') > -1:
                if not cmds.getAttr((leftItems[i] + '.ry'), l=True):
                    vFlip = cmds.getAttr((leftItems[i] + '.ry')) * -1
                    cmds.setAttr((leftItems[i] + '.ry'), vFlip)
                if not cmds.getAttr((leftItems[i] + '.rz'), l=True):
                    vFlip = cmds.getAttr((leftItems[i] + '.rz')) * -1
                    cmds.setAttr((leftItems[i] + '.rz'), vFlip)
            else:
                if not cmds.getAttr((leftItems[i] + '.rx'), l=True):
                    vFlip = cmds.getAttr((leftItems[i] + '.rx')) * -1
                    cmds.setAttr((leftItems[i] + '.rx'), vFlip)
                if not cmds.getAttr((leftItems[i] + '.ry'), l=True):
                    vFlip = cmds.getAttr((leftItems[i] + '.ry')) * -1
                    cmds.setAttr((leftItems[i] + '.ry'), vFlip)        
        else:
            if leftItems[i].find('Fk') > -1:
                if not cmds.getAttr((leftItems[i] + '.tx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'), l=True):
                    vLeft = cmds.getAttr((leftItems[i] + '.tx')) * -1
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx')) * -1
                    cmds.setAttr((leftItems[i] + '.tx'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), vLeft)
                if not cmds.getAttr((leftItems[i] + '.ty'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty'), l=True):
                    vLeft = cmds.getAttr((leftItems[i] + '.ty')) * -1
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty')) * -1
                    cmds.setAttr((leftItems[i] + '.ty'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), vLeft)
                if not cmds.getAttr((leftItems[i] + '.tz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'), l=True):
                    vLeft = cmds.getAttr((leftItems[i] + '.tz')) * -1
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz')) * -1
                    cmds.setAttr((leftItems[i] + '.tz'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), vLeft)

                if not cmds.getAttr((leftItems[i] + '.rx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'), l=True):
                    vLeft = cmds.getAttr((leftItems[i] + '.rx'))
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'))
                    cmds.setAttr((leftItems[i] + '.rx'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rx'), vLeft)
                if not cmds.getAttr((leftItems[i] + '.ry'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'), l=True):
                    vLeft = cmds.getAttr((leftItems[i] + '.ry'))
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'))
                    cmds.setAttr((leftItems[i] + '.ry'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ry'), vLeft)
                if not cmds.getAttr((leftItems[i] + '.rz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz'), l=True):
                    vLeft = cmds.getAttr((leftItems[i] + '.rz'))
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz'))
                    cmds.setAttr((leftItems[i] + '.rz'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rz'), vLeft)

            elif leftItems[i].find('Ik') > -1:
                if leftItems[i].find('Position') > -1:
                    if leftItems[i].find('Arm') > -1:
                        vLeft = cmds.getAttr((leftItems[i] + '.tx')) * -1
                        vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx')) * -1
                        cmds.setAttr((leftItems[i] + '.tx'), vRight)
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), vLeft)
                        vLeft = cmds.getAttr((leftItems[i] + '.ty')) * -1
                        vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty')) * -1
                        cmds.setAttr((leftItems[i] + '.ty'), vRight)
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), vLeft)
                        vLeft = cmds.getAttr((leftItems[i] + '.tz')) * -1
                        vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz')) * -1
                        cmds.setAttr((leftItems[i] + '.tz'), vRight)
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), vLeft)

                    elif leftItems[i].find('Leg') > -1:
                        vLeft = cmds.getAttr((leftItems[i] + '.tx'))
                        vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'))
                        cmds.setAttr((leftItems[i] + '.tx'), vRight)
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), vLeft)
                        vLeft = cmds.getAttr((leftItems[i] + '.ty')) * -1
                        vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty')) * -1
                        cmds.setAttr((leftItems[i] + '.ty'), vRight)
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), vLeft)
                        vLeft = cmds.getAttr((leftItems[i] + '.tz'))
                        vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'))
                        cmds.setAttr((leftItems[i] + '.tz'), vRight)
                        cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), vLeft)

                else:
                    if leftItems[i].find('Arm') > -1:
                        if not cmds.getAttr((leftItems[i] + '.tx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'), l=True):
                            vLeft = cmds.getAttr((leftItems[i] + '.tx')) * -1
                            vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx')) * -1
                            cmds.setAttr((leftItems[i] + '.tx'), vRight)
                            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), vLeft)
                        if not cmds.getAttr((leftItems[i] + '.ty'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty'), l=True):
                            vLeft = cmds.getAttr((leftItems[i] + '.ty')) * -1
                            vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty')) * -1
                            cmds.setAttr((leftItems[i] + '.ty'), vRight)
                            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), vLeft)
                        if not cmds.getAttr((leftItems[i] + '.tz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'), l=True):
                            vLeft = cmds.getAttr((leftItems[i] + '.tz')) * -1
                            vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz')) * -1
                            cmds.setAttr((leftItems[i] + '.tz'), vRight)
                            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), vLeft)

                        if not cmds.getAttr((leftItems[i] + '.rx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'), l=True):
                            vLeft = cmds.getAttr((leftItems[i] + '.rx'))
                            vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'))
                            cmds.setAttr((leftItems[i] + '.rx'), vRight)
                            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rx'), vLeft)
                        if not cmds.getAttr((leftItems[i] + '.ry'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'), l=True):
                            vLeft = cmds.getAttr((leftItems[i] + '.ry'))
                            vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'))
                            cmds.setAttr((leftItems[i] + '.ry'), vRight)
                            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ry'), vLeft)
                        if not cmds.getAttr((leftItems[i] + '.rz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz'), l=True):
                            vLeft = cmds.getAttr((leftItems[i] + '.rz'))
                            vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz'))
                            cmds.setAttr((leftItems[i] + '.rz'), vRight)
                            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rz'), vLeft)

                    elif leftItems[i].find('Leg') > -1:
                        if not cmds.getAttr((leftItems[i] + '.tx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'), l=True):
                            vLeft = cmds.getAttr((leftItems[i] + '.tx'))
                            vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'))
                            cmds.setAttr((leftItems[i] + '.tx'), vRight)
                            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), vLeft)
                        if not cmds.getAttr((leftItems[i] + '.ty'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty'), l=True):
                            vLeft = cmds.getAttr((leftItems[i] + '.ty')) * -1
                            vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty')) * -1
                            cmds.setAttr((leftItems[i] + '.ty'), vRight)
                            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), vLeft)
                        if not cmds.getAttr((leftItems[i] + '.tz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'), l=True):
                            vLeft = cmds.getAttr((leftItems[i] + '.tz'))
                            vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'))
                            cmds.setAttr((leftItems[i] + '.tz'), vRight)
                            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), vLeft)

                        if not cmds.getAttr((leftItems[i] + '.rx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'), l=True):
                            vLeft = cmds.getAttr((leftItems[i] + '.rx'))
                            vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'))
                            cmds.setAttr((leftItems[i] + '.rx'), vRight)
                            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rx'), vLeft)
                        if not cmds.getAttr((leftItems[i] + '.ry'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'), l=True):
                            vLeft = cmds.getAttr((leftItems[i] + '.ry'))
                            vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'))
                            cmds.setAttr((leftItems[i] + '.ry'), vRight)
                            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ry'), vLeft)
                        if not cmds.getAttr((leftItems[i] + '.rz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz'), l=True):
                            vLeft = cmds.getAttr((leftItems[i] + '.rz')) * -1
                            vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz')) * -1
                            cmds.setAttr((leftItems[i] + '.rz'), vRight)
                            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rz'), vLeft)

            elif leftItems[i].find('Bend') > -1:
                if leftItems[i].find('Arm') > -1 or leftItems[i].find('Forearm') > -1:
                    vLeft = cmds.getAttr((leftItems[i] + '.tx')) * -1
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx')) * -1
                    cmds.setAttr((leftItems[i] + '.tx'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), vLeft)
                    vLeft = cmds.getAttr((leftItems[i] + '.ty'))
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty'))
                    cmds.setAttr((leftItems[i] + '.ty'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), vLeft)
                    vLeft = cmds.getAttr((leftItems[i] + '.tz'))
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'))
                    cmds.setAttr((leftItems[i] + '.tz'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), vLeft)
    
                elif leftItems[i].find('Hip') > -1 or leftItems[i].find('Leg') > -1:
                    vLeft = cmds.getAttr((leftItems[i] + '.tx'))
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'))
                    cmds.setAttr((leftItems[i] + '.tx'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), vLeft)
                    vLeft = cmds.getAttr((leftItems[i] + '.ty')) * -1
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty')) * -1
                    cmds.setAttr((leftItems[i] + '.ty'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), vLeft)
                    vLeft = cmds.getAttr((leftItems[i] + '.tz'))
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'))
                    cmds.setAttr((leftItems[i] + '.tz'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), vLeft)

            elif leftItems[i].find('PoleVector') > -1:
                vLeft = cmds.getAttr((leftItems[i] + '.tx'))
                vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'))
                cmds.setAttr((leftItems[i] + '.tx'), vRight)
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), vLeft)
                vLeft = cmds.getAttr((leftItems[i] + '.ty'))
                vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty'))
                cmds.setAttr((leftItems[i] + '.ty'), vRight)
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), vLeft)
                vLeft = cmds.getAttr((leftItems[i] + '.tz')) * -1
                vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz')) * -1
                cmds.setAttr((leftItems[i] + '.tz'), vRight)
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), vLeft)

            else:
                if not cmds.getAttr((leftItems[i] + '.tx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'), l=True):
                    vLeft = cmds.getAttr((leftItems[i] + '.tx')) * -1
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx')) * -1
                    cmds.setAttr((leftItems[i] + '.tx'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), vLeft)
                if not cmds.getAttr((leftItems[i] + '.ty'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty'), l=True):
                    vLeft = cmds.getAttr((leftItems[i] + '.ty')) * -1
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty')) * -1
                    cmds.setAttr((leftItems[i] + '.ty'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ty'), vLeft)
                if not cmds.getAttr((leftItems[i] + '.tz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'), l=True):
                    vLeft = cmds.getAttr((leftItems[i] + '.tz')) * -1
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz')) * -1
                    cmds.setAttr((leftItems[i] + '.tz'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tz'), vLeft)

                if not cmds.getAttr((leftItems[i] + '.rx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'), l=True):
                    vLeft = cmds.getAttr((leftItems[i] + '.rx'))
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'))
                    cmds.setAttr((leftItems[i] + '.rx'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rx'), vLeft)
                if not cmds.getAttr((leftItems[i] + '.ry'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'), l=True):
                    vLeft = cmds.getAttr((leftItems[i] + '.ry'))
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'))
                    cmds.setAttr((leftItems[i] + '.ry'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ry'), vLeft)
                if not cmds.getAttr((leftItems[i] + '.rz'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz'), l=True):
                    vLeft = cmds.getAttr((leftItems[i] + '.rz'))
                    vRight = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz'))
                    cmds.setAttr((leftItems[i] + '.rz'), vRight)
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rz'), vLeft)


            allAttrs = cmds.listAnimatable(leftItems[i])

            for eachAttr in allAttrs:
                simpleAttr = eachAttr.split('.')[1]
                if simpleAttr not in ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ']:
                    LtoR = cmds.getAttr((leftItems[i] + '.' + simpleAttr))
                    RtoL = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.' + simpleAttr))
                    cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.' + simpleAttr), LtoR)
                    cmds.setAttr((leftItems[i] + '.' + simpleAttr), RtoL)

    cmds.autoKeyframe(state=prevStatusAutoKey)

#=================================================================================================================================================
#
# SIGNATURE:
#    doFlipRootRelative(namespace = ':', leftItems = None, rightItems = None, middleItems = None, leftLocators = None, rightLocators = None, leftFlipLocators = None, rightFlipLocators = None)
#
# DESCRIPTION:
#    Flip Left and Right. Root Relative Space.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#    leftItems - List of the Left Items to Flip.
#    rightItems - List of the Right Items to Flip.
#    middleItems - List of the Middle Items to Flip.
#    leftLocators - List of Left Locators to use as Helpers.
#    rightLocators - List of Right Locators to use as Helpers.
#    leftFlipLocators - List of Left Locators to store temporary positions.
#    rightFlipLocators - List of Right Locators to store temporary positions.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def doFlipRootRelative(namespace = ':', leftItems = None, rightItems = None, middleItems = None, leftLocators = None, rightLocators = None, leftFlipLocators = None, rightFlipLocators = None):
    prevStatusAutoKey = 0
    prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
    cmds.autoKeyframe(state=False)

    lstPosLtoR = []    
    lstRotLtoR = []    
    lstPosRtoL = []    
    lstRotRtoL = []            

    for i in range(0, len(leftItems)):
        #L to R        
        posItem = cmds.xform(leftItems[i], q=True, t=True, ws=True)
        rotItem = cmds.xform(leftItems[i], q=True, ro=True, ws=True)

        cmds.xform(leftLocators[i], t=posItem, ws=True)
        cmds.xform(leftLocators[i], ro=rotItem, ws=True)

        cmds.xform(leftLocators[i].replace('Left', 'Right'), t=posItem, r=True)
        cmds.xform(leftLocators[i].replace('Left', 'Right'), ro=rotItem, r=True)

        cmds.parent(leftLocators[i], (namespace + rootControlName))
        cmds.parent(leftLocators[i].replace('Left', 'Right'), (namespace + rootControlName))

        posItem = cmds.xform(leftLocators[i], q=True, t=True, r=True)
        rotItem = cmds.xform(leftLocators[i], q=True, ro=True, r=True)

        cmds.setAttr((leftLocators[i].replace('Left', 'Right') + '.tx'), posItem[0] * -1)
        cmds.setAttr((leftLocators[i].replace('Left', 'Right') + '.ty'), posItem[1])
        cmds.setAttr((leftLocators[i].replace('Left', 'Right') + '.tz'), posItem[2])
    
        if leftLocators[i].replace('Left', 'Right').find('IkLeg000Right') == -1 and leftLocators[i].replace('Left', 'Right').find('EyeBrow') == -1:
            cmds.setAttr((leftLocators[i].replace('Left', 'Right') + '.rx'), rotItem[0] - 180)
        if leftLocators[i].replace('Left', 'Right').find('IkLeg000Right') == -1 and leftLocators[i].replace('Left', 'Right').find('ctlEyeBrow') == -1:
            cmds.setAttr((leftLocators[i].replace('Left', 'Right') + '.ry'), rotItem[1] * -1)
            cmds.setAttr((leftLocators[i].replace('Left', 'Right') + '.rz'), rotItem[2] * -1)
    
        cmds.parent(leftLocators[i], w=True)
        cmds.parent(leftLocators[i].replace('Left', 'Right'), w=True)
    
        posItemLtoR = cmds.xform(leftLocators[i].replace('Left', 'Right'), q=True, t=True, ws=True)
        rotItemLtoR = cmds.xform(leftLocators[i].replace('Left', 'Right'), q=True, ro=True, ws=True)
        lstPosLtoR.append(posItemLtoR)
        lstRotLtoR.append(rotItemLtoR)
    

        #R to L
        posItem = cmds.xform(rightItems[i], q=True, t=True, ws=True)
        rotItem = cmds.xform(rightItems[i], q=True, ro=True, ws=True)

        cmds.xform(rightFlipLocators[i], t=posItem, ws=True)
        cmds.xform(rightFlipLocators[i], ro=rotItem, ws=True)

        cmds.xform(rightFlipLocators[i].replace('Right', 'Left'), t=posItem, r=True)
        cmds.xform(rightFlipLocators[i].replace('Right', 'Left'), ro=rotItem, r=True)

        cmds.parent(rightFlipLocators[i], (namespace + rootControlName))
        cmds.parent(rightFlipLocators[i].replace('Right', 'Left'), (namespace + rootControlName))

        posItem = cmds.xform(rightFlipLocators[i], q=True, t=True, r=True)
        rotItem = cmds.xform(rightFlipLocators[i], q=True, ro=True, r=True)

        cmds.setAttr((rightFlipLocators[i].replace('Right', 'Left') + '.tx'), posItem[0] * -1)
        cmds.setAttr((rightFlipLocators[i].replace('Right', 'Left') + '.ty'), posItem[1])
        cmds.setAttr((rightFlipLocators[i].replace('Right', 'Left') + '.tz'), posItem[2])
    
        if rightFlipLocators[i].replace('Right', 'Left').find('IkLeg000Left') == -1 and rightFlipLocators[i].replace('Right', 'Left').find('EyeBrow') == -1:
            cmds.setAttr((rightFlipLocators[i].replace('Right', 'Left') + '.rx'), rotItem[0] - 180)
        if rightFlipLocators[i].replace('Right', 'Left').find('IkLeg000Left') == -1 and rightFlipLocators[i].replace('Right', 'Left').find('ctlEyeBrow') == -1:
            cmds.setAttr((rightFlipLocators[i].replace('Right', 'Left') + '.ry'), rotItem[1] * -1)
            cmds.setAttr((rightFlipLocators[i].replace('Right', 'Left') + '.rz'), rotItem[2] * -1)
    
        cmds.parent(rightFlipLocators[i], w=True)
        cmds.parent(rightFlipLocators[i].replace('Right', 'Left'), w=True)
    
        posItemRtoL = cmds.xform(rightFlipLocators[i].replace('Right', 'Left'), q=True, t=True, ws=True)
        rotItemRtoL = cmds.xform(rightFlipLocators[i].replace('Right', 'Left'), q=True, ro=True, ws=True)
        lstPosRtoL.append(posItemRtoL)
        lstRotRtoL.append(rotItemRtoL)

    for i in range(0, len(middleItems)):
        if middleItems[i].find('Main') > -1 or middleItems[i].find('Root') > -1:
            pass
        elif middleItems[i].find('Hip') > -1 or middleItems[i].find('Eye') > -1:
            if not cmds.getAttr((middleItems[i] + '.ry'), l=True):
                vFlip = cmds.getAttr((middleItems[i] + '.ry')) * -1
                cmds.setAttr((middleItems[i] + '.ry'), vFlip)
            if not cmds.getAttr((middleItems[i] + '.rz'), l=True):
                vFlip = cmds.getAttr((middleItems[i] + '.rz')) * -1
                cmds.setAttr((middleItems[i] + '.rz'), vFlip)
        else:
            if not cmds.getAttr((middleItems[i] + '.rx'), l=True):
                vFlip = cmds.getAttr((middleItems[i] + '.rx')) * -1
                cmds.setAttr((middleItems[i] + '.rx'), vFlip)
            if not cmds.getAttr((middleItems[i] + '.ry'), l=True):
                vFlip = cmds.getAttr((middleItems[i] + '.ry')) * -1
                cmds.setAttr((middleItems[i] + '.ry'), vFlip)    

    for i in range(0, len(leftItems)):
        posItemLtoR = lstPosLtoR[i]    
        rotItemLtoR = lstRotLtoR[i]    
        posItemRtoL = lstPosRtoL[i]    
        rotItemRtoL = lstRotRtoL[i]    

        #L to R
        if not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ty'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tz'), l=True):
            cmds.xform(leftItems[i].replace('Left', 'Right'), t=posItemLtoR, ws=True)    
        if not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry'), l=True) and not cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz'), l=True):
            cmds.xform(leftItems[i].replace('Left', 'Right'), ro=rotItemLtoR, ws=True)    
    
    
        if leftLocators[i].replace('Left', 'Right').find('IkLeg000Right') > -1:
            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rx'), cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rx')) * -1)
            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rz'), cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz')) * -1)
        elif leftLocators[i].replace('Left', 'Right').find('EyeBrowRibbon') > -1:
            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.tx'), cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.tx')) * -1)
            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.ry'), cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.ry')) * -1)
            cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.rz'), cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.rz')) * -1)        
    

    
        #R to L
        if not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tx'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ty'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tz'), l=True):
            cmds.xform(rightItems[i].replace('Right', 'Left'), t=posItemRtoL, ws=True)    
        if not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rx'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ry'), l=True) and not cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rz'), l=True):
            cmds.xform(rightItems[i].replace('Right', 'Left'), ro=rotItemRtoL, ws=True)    
    
    
        if rightLocators[i].replace('Right', 'Left').find('IkLeg000Left') > -1:
            cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rx'), cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rx')) * -1)
            cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rz'), cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rz')) * -1)
        elif rightLocators[i].replace('Right', 'Left').find('EyeBrowRibbon') > -1:
            cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.tx'), cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.tx')) * -1)
            cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.ry'), cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.ry')) * -1)
            cmds.setAttr((rightItems[i].replace('Right', 'Left') + '.rz'), cmds.getAttr((rightItems[i].replace('Right', 'Left') + '.rz')) * -1)
    
        allAttrs = cmds.listAnimatable(leftItems[i])

        for eachAttr in allAttrs:
            simpleAttr = eachAttr.split('.')[1]
            if simpleAttr not in ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ']:
                LtoR = cmds.getAttr((leftItems[i] + '.' + simpleAttr))
                RtoL = cmds.getAttr((leftItems[i].replace('Left', 'Right') + '.' + simpleAttr))
                cmds.setAttr((leftItems[i].replace('Left', 'Right') + '.' + simpleAttr), LtoR)
                cmds.setAttr((leftItems[i] + '.' + simpleAttr), RtoL)

    if leftLocators:
        cmds.delete(leftLocators)
    if rightLocators:
        cmds.delete(rightLocators)
    if leftFlipLocators:    
        cmds.delete(leftFlipLocators)
    if rightFlipLocators:
        cmds.delete(rightFlipLocators)

    cmds.autoKeyframe(state=prevStatusAutoKey)



#RESET POSES =====================================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    resetSelected(namespace, selectedItems)
#
# DESCRIPTION:
#    Reset the position of the selected controls.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#     selectedItems - List of selected controls.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def resetSelected(namespace, selectedItems):

    for eachItem in selectedItems:
        allAttrs = cmds.listAnimatable(eachItem)
        for eachAttr in allAttrs:
            attr = eachAttr.split('.')[1]

            if attr.find('scale') > -1 or attr.find('globalScale') > -1 or attr.find('handType') > -1:
                cmds.setAttr((eachItem + '.' + attr), 1)
            elif attr.find('typeOfControls') > -1:
                cmds.setAttr((eachItem + '.' + attr), 2)
            elif attr.find('follow') > -1 or attr.find('stretchy') > -1 or attr.find('volumetricStretch') > -1:
                if attr.find('follow') > -1 and eachItem.find('PoleVector') == -1 and attr.find('followHead') == -1:
                    cmds.setAttr((eachItem + '.' + attr), 0)
                else:
                    cmds.setAttr((eachItem + '.' + attr), 10)
            else:
                cmds.setAttr((eachItem + '.' + attr), 0)

#=================================================================================================================================================
#
# SIGNATURE:
#    resetAll(namespace)
#
# DESCRIPTION:
#    Reset the position of all controls.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def resetAll(namespace):

    allItems = cmds.sets(namespace + animationControlsSet, q=True)

    for eachItem in allItems:
        allAttrs = cmds.listAnimatable(eachItem)
        for eachAttr in allAttrs:
            attr = eachAttr.split('.')[1]

            if attr.find('scale') > -1 or attr.find('globalScale') > -1 or attr.find('handType') > -1:
                cmds.setAttr((eachItem + '.' + attr), 1)
            elif attr.find('typeOfControls') > -1:
                cmds.setAttr((eachItem + '.' + attr), 2)
            elif attr.find('follow') > -1 or attr.find('stretchy') > -1 or attr.find('volumetricStretch') > -1:
                if attr.find('follow') > -1 and eachItem.find('PoleVector') == -1 and attr.find('followHead') == -1:
                    cmds.setAttr((eachItem + '.' + attr), 0)
                else:
                    cmds.setAttr((eachItem + '.' + attr), 10)
            else:
                cmds.setAttr((eachItem + '.' + attr), 0)

#=================================================================================================================================================
#
# SIGNATURE:
#    resetPose(namespace)
#
# DESCRIPTION:
#    Reset the position of the controls to a T-Pose.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def resetPose(namespace):

    allItems = cmds.sets(namespace + animationControlsSet, q=True)

    for eachItem in allItems:
        if eachItem.find('ctlRoot000Middle') == - 1 and eachItem.find('ctlMain000Middle') == -1:
            allAttrs = cmds.listAnimatable(eachItem)
            for eachAttr in allAttrs:
                attr = eachAttr.split('.')[1]

                if attr.find('scale') > -1 or attr.find('globalScale') > -1 or attr.find('handType') > -1:
                    cmds.setAttr((eachItem + '.' + attr), 1)
                elif attr.find('typeOfControls') > -1:
                    cmds.setAttr((eachItem + '.' + attr), 2)
                elif attr.find('follow') > -1 or attr.find('stretchy') > -1 or attr.find('volumetricStretch') > -1:
                    if attr.find('follow') > -1 and eachItem.find('PoleVector') == -1 and attr.find('followHead') == -1:
                        cmds.setAttr((eachItem + '.' + attr), 0)
                    else:
                        cmds.setAttr((eachItem + '.' + attr), 10)
                else:
                    cmds.setAttr((eachItem + '.' + attr), 0)

    prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
    cmds.autoKeyframe(state=False)

    posLeftArm = cmds.xform((namespace + grpResetPoseLeftArm), q=True, t=True, ws=True)
    posRightArm = cmds.xform((namespace + grpResetPoseRightArm), q=True, t=True, ws=True)
    posLeftLeg = cmds.xform((namespace + grpResetPoseLeftLeg), q=True, t=True, ws=True)
    posRightLeg = cmds.xform((namespace + grpResetPoseRightLeg), q=True, t=True, ws=True)
    rotLeftArm = cmds.xform((namespace + grpResetPoseLeftArm), q=True, ro=True, ws=True)
    rotRightArm = cmds.xform((namespace + grpResetPoseRightArm), q=True, ro=True, ws=True)
    rotLeftLeg = cmds.xform((namespace + grpResetPoseLeftLeg), q=True, ro=True, ws=True)
    rotRightLeg = cmds.xform((namespace + grpResetPoseRightLeg), q=True, ro=True, ws=True)

    cmds.xform((namespace + ctlIkArmLeft), t=posLeftArm, ws=True)
    cmds.xform((namespace + ctlIkArmRight), t=posRightArm, ws=True)
    cmds.xform((namespace + ctlIkLegLeft), t=posLeftLeg, ws=True)
    cmds.xform((namespace + ctlIkLegRight), t=posRightLeg, ws=True)
    cmds.xform((namespace + ctlIkArmLeft), ro=rotLeftArm, ws=True)
    cmds.xform((namespace + ctlIkArmRight), ro=rotRightArm, ws=True)
    cmds.xform((namespace + ctlIkLegLeft), ro=rotLeftLeg, ws=True)
    cmds.xform((namespace + ctlIkLegRight), ro=rotRightLeg, ws=True)

    posLeftArmPoleVector = cmds.xform((namespace + grpResetPosePoleVectorLeftArm), q=True, t=True, ws=True)
    posRightArmPoleVector = cmds.xform((namespace + grpResetPosePoleVectorRightArm), q=True, t=True, ws=True)
    posLeftLegPoleVector = cmds.xform((namespace + grpResetPosePoleVectorLeftLeg), q=True, t=True, ws=True)
    posRightLegPoleVector = cmds.xform((namespace + grpResetPosePoleVectorRightLeg), q=True, t=True, ws=True)

    cmds.xform((namespace + ctlIkArmPoleVectorLeft), t=posLeftArmPoleVector, ws=True)
    cmds.xform((namespace + ctlIkArmPoleVectorRight), t=posRightArmPoleVector, ws=True)
    cmds.xform((namespace + ctlIkLegPoleVectorLeft), t=posLeftLegPoleVector, ws=True)
    cmds.xform((namespace + ctlIkLegPoleVectorRight), t=posRightLegPoleVector, ws=True)

    cmds.autoKeyframe(state=prevStatusAutoKey)



#PIN CONTROLS ====================================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    doPin(ctlFrom, ctlTo)
#
# DESCRIPTION:
#    Pin the selected controls together.
# 
# REQUIRES:
#     ctlFrom - Driver control.
#     ctlTo - Driven control.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def doPin(ctlFrom, ctlTo):
    cpaName = ctlTo.replace('ctl', 'cpaPin')

    pinTo = ctlTo.replace('ctl', 'pin')

    cmds.parentConstraint(ctlFrom, pinTo, mo=True, n=cpaName)

#=================================================================================================================================================
#
# SIGNATURE:
#    deletePin(ctlToUnpin)
#
# DESCRIPTION:
#    Deletes the pin of the driven controls.
# 
# REQUIRES:
#     ctlToUnpin - Driven control.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def deletePin(ctlToUnpin):
    for eachCtl in ctlToUnpin:
        cpaName = eachCtl.replace('ctl', 'cpaPin')
        if cmds.objExists(cpaName):
            cmds.delete(cpaName)
        else:
            showMessage('USE: Select a Driven Control with an active Pin.')

#=================================================================================================================================================
#
# SIGNATURE:
#    bakeAndDeletePin(ctlToUnpin, startFrame=None, endFrame=None)
#
# DESCRIPTION:
#    Bakes the Animation and Deletes the pin of the driven controls.
# 
# REQUIRES:
#     ctlToUnpin - Driven control.
#     startFrame - Start frame of the animation to Bake.
#     endFrame - End frame of the animation to Bake.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def bakeAndDeletePin(ctlToUnpin, startFrame=None, endFrame=None):
    for eachCtl in ctlToUnpin:

        cpaName = eachCtl.replace('ctl', 'cpaPin')
        if cmds.objExists(cpaName):

            currTime = cmds.currentTime(q=True)

            if not startFrame:
                startFrame = cmds.playbackOptions(q=True, ast=True)
            if not endFrame:
                endFrame = cmds.playbackOptions(q=True, aet=True)

            delta = endFrame - startFrame

            prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
            cmds.autoKeyframe(state=False)

            listPos = []
            listRot = []
            for i in range(startFrame, endFrame + 1):
                cmds.currentTime(i)
                posCtl = cmds.xform(eachCtl, q=True, t=True, ws=True)
                rotCtl = cmds.xform(eachCtl, q=True, ro=True, ws=True)
                listPos.append(posCtl)
                listRot.append(rotCtl)

            cmds.currentTime(startFrame)

            cmds.delete(cpaName)

            j = 0
            for i in range(startFrame, endFrame + 1):
                cmds.currentTime(i)
                cmds.xform(eachCtl, t=listPos[j], ws=True)
                cmds.xform(eachCtl, ro=listRot[j], ws=True)
                cmds.setKeyframe(eachCtl, breakdown=0, controlPoints=0, shape=0, hierarchy='none')
                j += 1
        
            cmds.currentTime(currTime)
            cmds.autoKeyframe(state=prevStatusAutoKey)

        else:
            showMessage('USE: Select a Driven Control with an active Pin.')

#=================================================================================================================================================
#
# SIGNATURE:
#    createPinControl()
#
# DESCRIPTION:
#    Creates an Extra Controls to Pin other Controls to.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def createPinControl():
    ctlName = None

    ctlLastIndex = None
    lastIndex = None

    allPinCtls = cmds.ls('ctlPinExtra*Middle')
    if allPinCtls:
        for eachPinCtl in allPinCtls:
            if cmds.objExists(eachPinCtl + '.lastIndex'):
                ctlLastIndex = eachPinCtl + '.lastIndex'
                lastIndex = str(int(cmds.getAttr(ctlLastIndex)) + 1).zfill(3)
                break

    if ctlLastIndex:
        ctlName = cmds.curve(d=1, p=extraPinControlShape, n=('ctlPinExtra' + lastIndex + 'Middle'))
        cmds.closeCurve(ctlName, preserveShape=0, replaceOriginal=1)

        cmds.setAttr((ctlName + '.sx'), 2.5)
        cmds.setAttr((ctlName + '.sy'), 2.5)
        cmds.setAttr((ctlName + '.sz'), 2.5)

        cmds.setAttr((ctlName + '.sx'), l=True, k=False)
        cmds.setAttr((ctlName + '.sy'), l=True, k=False)
        cmds.setAttr((ctlName + '.sz'), l=True, k=False)

        offGrpName = cmds.group(empty=True, n=ctlName.replace('ctl', 'off'))
        xtraGrpName = cmds.group(empty=True, n=ctlName.replace('ctl', 'xtra'))
        pinGrpName = cmds.group(empty=True, n=ctlName.replace('ctl', 'pin'))

        cmds.parent(ctlName, pinGrpName)
        cmds.parent(pinGrpName, xtraGrpName)
        cmds.parent(xtraGrpName, offGrpName)

        cmds.setAttr(ctlLastIndex, l=False)
        cmds.setAttr(ctlLastIndex, lastIndex, type='string')
        cmds.setAttr(ctlLastIndex, l=True)
    else:
        ctlName = cmds.curve(d=1, p=extraPinControlShape, n='ctlPinExtra000Middle')

        cmds.setAttr((ctlName + '.sx'), 2.5)
        cmds.setAttr((ctlName + '.sy'), 2.5)
        cmds.setAttr((ctlName + '.sz'), 2.5)

        cmds.setAttr((ctlName + '.sx'), l=True, k=False)
        cmds.setAttr((ctlName + '.sy'), l=True, k=False)
        cmds.setAttr((ctlName + '.sz'), l=True, k=False)

        cmds.closeCurve(ctlName, preserveShape=0, replaceOriginal=1)
        offGrpName = cmds.group(empty=True, n=ctlName.replace('ctl', 'off'))
        xtraGrpName = cmds.group(empty=True, n=ctlName.replace('ctl', 'xtra'))
        pinGrpName = cmds.group(empty=True, n=ctlName.replace('ctl', 'pin'))

        cmds.parent(ctlName, pinGrpName)
        cmds.parent(pinGrpName, xtraGrpName)
        cmds.parent(xtraGrpName, offGrpName)

        cmds.addAttr(ctlName , ln='lastIndex', dt='string')  
        cmds.setAttr((ctlName + '.lastIndex'), e=True, k=True)
        cmds.setAttr((ctlName + '.lastIndex'), '000', type='string')
        cmds.setAttr((ctlName + '.lastIndex'), l=True)

    colorGreen(ctlName)
    cmds.select(ctlName, r=True)

#=================================================================================================================================================
#
# SIGNATURE:
#    removeSelectedPinControl(pinCtlName)
#
# DESCRIPTION:
#    Delete the selected Extra Pin Control/s.
# 
# REQUIRES:
#     pinCtlName - Selected Extra Pin Control/s.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def removeSelectedPinControl(pinCtlName):
    for eachPinCtl in pinCtlName:
        if cmds.objExists(eachPinCtl + '.lastIndex'):
            lastIndex = cmds.getAttr((eachPinCtl + '.lastIndex'))

            lastPinCtl = 'ctlPinExtra' + lastIndex + 'Middle'            

            if cmds.objExists(lastPinCtl):
                cmds.addAttr(lastPinCtl , ln='lastIndex', dt='string')  
                cmds.setAttr((lastPinCtl + '.lastIndex'), e=True, k=True)
                cmds.setAttr((lastPinCtl + '.lastIndex'), lastIndex, type='string')
                cmds.setAttr((lastPinCtl + '.lastIndex'), l=True)
            else:
                intLastIndex = int(lastIndex)
                iFoundTheOne = False
                while not iFoundTheOne:
                    lastPinCtl = 'ctlPinExtra' + str(intLastIndex).zfill(3) + 'Middle'            

                    if cmds.objExists(lastPinCtl):
                        cmds.addAttr(lastPinCtl , ln='lastIndex', dt='string')  
                        cmds.setAttr((lastPinCtl + '.lastIndex'), e=True, k=True)
                        cmds.setAttr((lastPinCtl + '.lastIndex'), str(intLastIndex).zfill(3), type='string')
                        cmds.setAttr((lastPinCtl + '.lastIndex'), l=True)
                        iFoundTheOne = True

                    intLastIndex -= 1

        pinGrpName = cmds.listRelatives(eachPinCtl, p=True)[0]
        xtraGrpName = cmds.listRelatives(pinGrpName, p=True)[0]
        offGrpName = cmds.listRelatives(xtraGrpName, p=True)[0]
        if offGrpName.find('PinExtra') > -1 and cmds.objExists(offGrpName):
            cmds.delete(offGrpName)
        else:
            showMessage('USE: Select a valid Extra Pin Control.')


#=================================================================================================================================================
#
# SIGNATURE:
#    removeAllPinControl()
#
# DESCRIPTION:
#    Delete All Extra Pin Controls.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def removeAllPinControl():
    allPinOff = cmds.ls('offPinExtra*Middle')
    cmds.delete(allPinOff)



#GLOBAL SWITCH ===================================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    seamlessGlobalOrFollowSwitch(selectedCtls)
#
# DESCRIPTION:
#    Seamless Switch of Controls with Global or Follow Attributes.
# 
# REQUIRES:
#     selectedCtls - Selected controls.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def seamlessGlobalOrFollowSwitch(selectedCtls):
    for eachCtl in selectedCtls:
        if cmds.objExists((eachCtl + '.global')):
            prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
            cmds.autoKeyframe(state=False)

            posCtl = cmds.xform(eachCtl, q=True, t=True, ws=True)
            rotCtl = cmds.xform(eachCtl, q=True, ro=True, ws=True)

            cmds.currentTime(cmds.currentTime(q=True) - 1, edit=True)
            cmds.setKeyframe(eachCtl, breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.currentTime(cmds.currentTime(q=True) + 1, edit=True)

            globalValue = cmds.getAttr((eachCtl + '.global'))
            if globalValue == 10:
                cmds.setAttr((eachCtl + '.global'), 0)
            elif globalValue == 0:
                cmds.setAttr((eachCtl + '.global'), 10)
            else:
                cmds.setAttr((eachCtl + '.global'), 10 - globalValue)

            cmds.xform(eachCtl, t=posCtl, ws=True)
            cmds.xform(eachCtl, ro=rotCtl, ws=True)

            cmds.setKeyframe(eachCtl, breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.autoKeyframe(state=prevStatusAutoKey)

        elif cmds.objExists((eachCtl + '.follow')):
            prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
            cmds.autoKeyframe(state=False)

            posCtl = cmds.xform(eachCtl, q=True, t=True, ws=True)
            rotCtl = cmds.xform(eachCtl, q=True, ro=True, ws=True)

            cmds.currentTime(cmds.currentTime(q=True) - 1, edit=True)
            cmds.setKeyframe(eachCtl, breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.currentTime(cmds.currentTime(q=True) + 1, edit=True)

            globalValue = cmds.getAttr((eachCtl + '.follow'))
            if globalValue == 10:
                cmds.setAttr((eachCtl + '.follow'), 0)
            elif globalValue == 0:
                cmds.setAttr((eachCtl + '.follow'), 10)
            else:
                cmds.setAttr((eachCtl + '.follow'), 10 - globalValue)

            cmds.xform(eachCtl, t=posCtl, ws=True)
            cmds.xform(eachCtl, ro=rotCtl, ws=True)

            cmds.setKeyframe(eachCtl, breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.autoKeyframe(state=prevStatusAutoKey)

        else:
            showMessage('USE: Select a control with a Global or a Follow Attribute.')



#DYNAMIC PIVOT ===================================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    createDynamicMainPivot(namespace)
#
# DESCRIPTION:
#    Creates a Control to control the Pivot of the Main Control.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def createDynamicMainPivot(namespace):
    if not cmds.objExists('offDynamicPivot000Middle'):
        dynPivotName = 'ctlDynamicPivot000Middle'

        dynPivotName = cmds.curve(d=1, p=dynamicPivotControlShape, n=dynPivotName)
        cmds.closeCurve(dynPivotName, preserveShape=0, replaceOriginal=1)

        offGrpName = cmds.group(empty=True, n=dynPivotName.replace('ctl', 'off'))
        xtraGrpName = cmds.group(empty=True, n=dynPivotName.replace('ctl', 'xtra'))
        pinGrpName = cmds.group(empty=True, n=dynPivotName.replace('ctl', 'pin'))

        cmds.parent(dynPivotName, pinGrpName)
        cmds.parent(pinGrpName, xtraGrpName)
        cmds.parent(xtraGrpName, offGrpName)

        colorBlue(dynPivotName)
        cmds.setAttr((dynPivotName + '.v'), l=1, k=0)

        cmds.setAttr((dynPivotName + '.sx'), 5)
        cmds.setAttr((dynPivotName + '.sy'), 5)
        cmds.setAttr((dynPivotName + '.sz'), 5)

        cmds.setAttr((dynPivotName + '.sx'), l=True, k=False)
        cmds.setAttr((dynPivotName + '.sy'), l=True, k=False)
        cmds.setAttr((dynPivotName + '.sz'), l=True, k=False)

        cmds.delete(cmds.pointConstraint((namespace + mainControlName), offGrpName, o=(0,0,0)))
        cmds.delete(cmds.orientConstraint((namespace + mainControlName), offGrpName, o=(0,0,0)))

        cmds.connectAttr((dynPivotName + '.translate'), (namespace + mainControlName + '.rotatePivot'), f=True)

        cmds.select(dynPivotName, r=True)
    else: 
        showMessage('INFO: Dynamic Pivot is already created.')

#=================================================================================================================================================
#
# SIGNATURE:
#    bakeAndDeleteDynamicMainPivot(namespace, startFrame=None, endFrame=None)
#
# DESCRIPTION:
#    Bakes the Animation of the Main Control and Deletes Dynamic Pivot Control.
# 
# REQUIRES:
#     namespace - Name of the Namespace of the referred Rig.
#     startFrame - Start frame of the animation to Bake.
#     endFrame - End frame of the animation to Bake.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def bakeAndDeleteDynamicMainPivot(namespace, startFrame=None, endFrame=None):
    if cmds.objExists('offDynamicPivot000Middle'):
        currTime = cmds.currentTime(q=True)

        if not startFrame:
            startFrame = cmds.playbackOptions(q=True, ast=True)
        if not endFrame:
            endFrame = cmds.playbackOptions(q=True, aet=True)

        delta = endFrame - startFrame

        prevStatusAutoKey = cmds.autoKeyframe(q=True, state=True)
        cmds.autoKeyframe(state=False)

        listPos = []
        listRot = []
        pivotPos = []
        for i in range(startFrame, endFrame + 1):
            cmds.currentTime(i)
            posCtl = cmds.xform((namespace + mainControlName), q=True, t=True, ws=True)
            rotCtl = cmds.xform((namespace + mainControlName), q=True, ro=True, ws=True)
            listPos.append(posCtl)
            listRot.append(rotCtl)

            posPivot = cmds.xform('ctlDynamicPivot000Middle', q=True, t=True, ws=True)
            pivotPos.append(posPivot)

        cmds.currentTime(startFrame)

        if cmds.objExists('offDynamicPivot000Middle'):
            cmds.delete('offDynamicPivot000Middle')

        cmds.setAttr((namespace + mainControlName + '.rotatePivotX'), 0)
        cmds.setAttr((namespace + mainControlName + '.rotatePivotY'), 0)
        cmds.setAttr((namespace + mainControlName + '.rotatePivotZ'), 0)

        j = 0
        for i in range(startFrame, endFrame + 1):
            cmds.currentTime(i)

            cmds.setAttr((namespace + mainControlName + '.rotatePivotX'), pivotPos[j][0])
            cmds.setAttr((namespace + mainControlName + '.rotatePivotY'), pivotPos[j][1])
            cmds.setAttr((namespace + mainControlName + '.rotatePivotZ'), pivotPos[j][2])
            cmds.setKeyframe(namespace + mainControlName + '.rotatePivotX', breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.setKeyframe(namespace + mainControlName + '.rotatePivotY', breakdown=0, controlPoints=0, shape=0, hierarchy='none')
            cmds.setKeyframe(namespace + mainControlName + '.rotatePivotZ', breakdown=0, controlPoints=0, shape=0, hierarchy='none')

            cmds.xform((namespace + mainControlName), t=listPos[j], ws=True)
            cmds.xform((namespace + mainControlName), ro=listRot[j], ws=True)
            cmds.setKeyframe(namespace + mainControlName, breakdown=0, controlPoints=0, shape=0, hierarchy='none')

            j += 1

        cmds.currentTime(currTime)
        cmds.autoKeyframe(state=prevStatusAutoKey)
    else: 
        showMessage('INFO: Dynamic Pivot does not exists.')



#EXTRA METHODS ===================================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    colorBlue(ctlToColor)
#
# DESCRIPTION:
#    Sets the Control Color to Blue.
# 
# REQUIRES:
#     colorBlue - Control to color.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def colorBlue(ctlToColor):
    cmds.setAttr((ctlToColor + '.overrideEnabled'), 1)
    cmds.setAttr((ctlToColor + '.overrideColor'), 6)

#=================================================================================================================================================
#
# SIGNATURE:
#    colorRed(ctlToColor)
#
# DESCRIPTION:
#    Sets the Control Color to Red.
# 
# REQUIRES:
#     colorBlue - Control to color.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def colorRed(ctlToColor):
    cmds.setAttr((ctlToColor + '.overrideEnabled'), 1)
    cmds.setAttr((ctlToColor + '.overrideColor'), 13)

#=================================================================================================================================================
#
# SIGNATURE:
#    colorGreen(ctlToColor)
#
# DESCRIPTION:
#    Sets the Control Color to Green.
# 
# REQUIRES:
#     colorBlue - Control to color.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def colorGreen(ctlToColor):
    cmds.setAttr((ctlToColor + '.overrideEnabled'), 1)
    cmds.setAttr((ctlToColor + '.overrideColor'), 14)



#SHOW MESSAGE ====================================================================================================================================
#=================================================================================================================================================

#=================================================================================================================================================
#
# SIGNATURE:
#    showMessage(strMessage)
#
# DESCRIPTION:
#    Opens a small window to inform of an error or another message.
# 
# REQUIRES:
#     strMessage - Message to Display.
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def showMessage(strMessage):
    if cmds.window('crashTestDummyWindowModalMessage', ex=True) == True:
        cmds.deleteUI('crashTestDummyWindowModalMessage')

    cmds.window('crashTestDummyWindowModalMessage', w=640, h=100, t='Info', s=False)

    cmds.formLayout('messageLayout')

    cmds.text('txtMessage', l=strMessage, w=640, align='center')
    cmds.button('btnAccept', l='OK', w=120, h=35, c=closeWindow)    

    cmds.formLayout('messageLayout', e=True, attachForm=[
                            ('txtMessage', 'top', 10),
                            ('txtMessage', 'left', 10),

                            ('btnAccept', 'top', 30),
                            ('btnAccept', 'left', 240)])

    cmds.setParent('..')

    cmds.showWindow('crashTestDummyWindowModalMessage')

    cmds.window('crashTestDummyWindowModalMessage', e=True, w=640, h=100)

#=================================================================================================================================================
#
# SIGNATURE:
#    closeWindow(* args)
#
# DESCRIPTION:
#    Event. Closes the Message Window.
# 
# REQUIRES:
#     Nothing
#
# RETURNS:
#    Nothing
#
#=================================================================================================================================================
def closeWindow(* args):
    cmds.deleteUI('crashTestDummyWindowModalMessage')

#=================================================================================================================================================
#=================================================================================================================================================
#    LOGIC
#=================================================================================================================================================
#=================================================================================================================================================
