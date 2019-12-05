import math

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    drunkDriver = params['all_wheels_on_track']
    
    
    heading = params['heading'] #direction our car is going in degrees 0-360
    nextWaypoint = params['closest_waypoints'] #x,y list of next waypoint on track
    agentX = params['x']
    agentY = params['y']
    
    #Calculate heading for next closest waypoint
    x1 = nextWaypoint[0] - agentX
    y1 = nextWaypoint[1] - agentY
    trueHeading = math.degrees(math.atan2(y1, x1)) #get the angle between our car coordinate and nextWaypoint in degrees.
    
    headingDiff = heading - trueHeading
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 10
        if drunkDriver == False:
            reward = 10
        if headingDiff > 5:
            reward -= 10
    elif distance_from_center <= marker_2:
        reward = 5
        if drunkDriver == False:
            reward = 5
        if headingDiff > 5:
            reward -= 5
    elif distance_from_center <= marker_3:
        reward = 2
        if drunkDriver == False:
            reward = 2
        if headingDiff > 5:
            reward -= 2
    elif drunkDriver:
        reward = 1e-3
        
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    return float(reward)
