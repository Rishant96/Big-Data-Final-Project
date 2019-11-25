import pandas as pd

training = pd.read_csv('training_median.csv')
testing = pd.read_csv('testing_portfolios_median.csv')
losses = pd.read_csv('training_loss_ratios.csv', header=None)
print('training', 'losses', 'testing')
