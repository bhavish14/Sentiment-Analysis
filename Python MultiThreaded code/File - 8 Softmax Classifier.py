import csv
import numpy as np

import tensorflow as tf
sess = tf.InteractiveSession()











username, positive, negative, neutral, no_tweets = np.genfromtxt('', delimiter=',', skip_header = 1, unpack = True, dtype='str')

val_mat = []
for i in range(len(positive)):
    temp = []
    temp.append(positive[i])
    temp.append(negative[i])
    temp.append(neutral[i])
    val_mat.append(temp)
z = np.zeros((248,3))


train_step.run(feed_dict={x: val_mat, y_: z})

#Placeholders
x = tf.placeholder(tf.float32, shape = [248, 3])
y_ = tf.placeholder(tf.float32, shape = [248, 3])

#Variables
W = tf.Variable(tf.zeros([3, 1]))
b = tf.Variable(tf.zeros([3]))

#initializing Variables
sess.run(tf.global_variables_initializer())

#regression model (y = weight * x + bias)
y = tf.matmul(x,W) + b

#loss function
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))

#training
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

for _ in range(1000):
  batch = mnist.train.next_batch(100)
  train_step.run(feed_dict={x: batch[0], y_: batch[1]})

#Model Evaluation
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
