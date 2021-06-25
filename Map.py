from Obst import Obstacle
from Spike import Spike

def draw(map, window):
    map = map.splitlines()

    spikes = []
    obstacles = []
    for y, line in enumerate(map):
        for x, c in enumerate(line):
            if c == "O":
                obs = Obstacle(x * 48, y * 48)
                obstacles.append(obs)
                window.blit(obs.sprite, (obs.x, obs.y))
            
            if c == "S":
                spike = Spike(x * 48, y * 48)
                spikes.append(spike)
                window.blit(spike.sprite, (spike.x, spike.y))
    
    return obstacles, spikes