#载入模块
import pandas as pd
from sklearn.neural_network import MLPRegressor
 #导入数据
train_data = pd.read_table('train_data.txt')
train_truth = pd.read_table('train_truth.txt')
test_data = pd.read_table('test_data.txt')
#构建并训练模型 1个输入层 2个隐含层（均有4个神经元）
sss = MLPRegressor(
        hidden_layer_sizes=(4,4), activation='relu',solver='adam',
        alpha=0.01,max_iter=2000)
   
print ("fitting model right now")
sss.fit(train_data,train_truth)
test = sss.predict(test_data)
#保存结果
f = open('text_predict.txt','w')
f.write('y')
f.write('\n')
for i in range(len(test)):
    f.write(str(test[i]))
    f.write('\n')
f.close()

