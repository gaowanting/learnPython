def get_reward(self):
    if self.current_step==0:
        return 0
    else:
        assets = self.account_information['total_assets'][-1]
        cash = self.account_information['cash'][-1]
        cash_penalty = max(0, (assets*self.cash_penalty_proportion-cash))
        assets -= cash_penalty
        reward = (assets/self.initial_amount)-1
        reward/=self.current_step   # step越大，reward越小
        return reward

'''
1
reward = 'cumulative return'
'''

'''
2 引入cash penalty
out_of_cash_penalty (int, float): Penalty to apply if the algorithm runs out of cash

cash_penalty_proportion=0.1,

if out_of_cash_penalty is None:
   out_of_cash_penalty = -initial_amount * 0.5
'''

'''
reward_scaling (float): Scaling value to multiply reward by at each step.
# reward is (cash + assets) - (cash_last_step + assets_last_step)
reward 随总资产变换
'''


'''
scale cash purchases to asset # changes
      actions = actions / closings
'''