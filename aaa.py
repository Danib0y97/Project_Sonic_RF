
import retro

env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis')
obs = env.reset()
print(obs.shape)


obs = env.reset()

done = False

for game in range(1):
    while not done:
        if done:
           obs = env.reset()
           env.render()
           obs,reward,done,info = env.step(env.action_space.sample())