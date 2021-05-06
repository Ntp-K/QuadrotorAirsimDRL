#import setup_path 
from airsim.AirSimClient import *


# connect to the AirSim simulator
client = MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

landed = client.getMultirotorState().landed_state
if landed == LandedState.Landed:
    print("taking off...")
    client.takeoffAsync().join()
else:
    print("already flying...")
    client.hoverAsync().join()

print("flying test...")
# #NED coordinate system, +X is North, +Y is East and +Z is Down
print("climbing attitude")
client.moveToPositionAsync(0,0,-40,10).join()
print("presude to destination")
client.moveToPositionAsync(225,0,-40,10).join()
client.moveToPositionAsync(225,0,0,10).join()
print("done")

