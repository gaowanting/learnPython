
# every episode reset the environment, such as let the car return to the origin
state = env.reset()

for t in range(100):
    # 渲染环境，可视化  a window pops up rendering CartPole
    env.render()
    print(state)

    # a random action, actually,it depends on policy function or Q function to choose the action
    action = env.action_space.sample()
    # agent choose an action, update state & reward, done indicates whether to end（over = 1），info
    state, reward, done, info = env.step(action)

    if done:
        print("finish")
        break

env.close()

