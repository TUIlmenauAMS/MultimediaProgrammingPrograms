# -*- coding: utf-8 -*-
__author__ = 'Gerald Schuller'
__copyright__ = 'G.S.'

"""
Simple program to use a linear neural network layer as signal detector.
Gerald Schuller, Nov. 2019.
"""

import torch 
import torch.nn as nn

device='cpu'
#device='cuda'

class LinNet(nn.Module):
    def __init__(self):
      super(LinNet, self).__init__()
      # Define the model. 
      self.layer1=nn.Sequential(nn.Linear(in_features=2, out_features=2, bias=True))
      #https://pytorch.org/docs/stable/nn.html?highlight=linear#torch.nn.Linear  
      # Generate a fully connected linear neural network model, 1 layer, bias, linear activation function 
      # returns: Trainable object
      self.act = nn.LeakyReLU() #non-linear activation function
      #self.act = nn.ReLU() #non-linear activation function
      #self.act = nn.Softmax() #turns an output into a probability distribution. Sums up to 1, which assumes that always one output is the true one
    
    def forward(self, x):
      out = self.layer1(x)
      out = self.act(out)  #comment out if not desired
      return out
      
if __name__ == '__main__':
   #input tensor, type torch tensor:
   #Indices: batch, additional dimensions, features or signal dimension. Here: 1 batch, 3 samples, signal dimension 2: 
   #Training set:
   X=torch.tensor([[1., 2.], [2., 1.],[1., 1.]])
   #X=X.view(1,3,2) #adding the first dimension for the batch
   print("X.shape", X.shape)
   #Target:
   Y=torch.tensor([[1., 0.], [0., 1.],[0., 0.]])
   #Y=Y.view(1,3,2)
   print("Y.shape", Y.shape)
   #Validation set, to test generalization:
   Xval=torch.tensor([[0.5, 1.0], [1., 0.5],[0.5, 0.5]])
   #Xval=Xval.view(1,3,2)
   #Validation Target:
   Yval=torch.tensor([[1., 0.], [0., 1.],[0., 0.]])
   #Yval=Yval.view(1,3,2)
   
   #create network object:
   model = LinNet().to(device)
   print("Define loss function:")
   loss_fn = nn.MSELoss()
   """
   Y=Y.argmax(dim=-1) #CrossEntropyLoss takes index of true class as input, not probability distribution as MSE. CrossEntropyLoss does not really fit here, because it need exactly 1 class to be true (the index in the traget), but here we also have a case were no class is true! 
   Yval=Yval.argmax(dim=-1)
   print("Y.shape=", Y.shape)
   loss_fn = nn.CrossEntropyLoss()
   """
   #loss_fn = nn.BCELoss() #needs values between 0 and 1.
   print("Define optimizer:")
   #learning_rate = 1e-4
   #optimizer = torch.optim.Adam(model.parameters())
   optimizer = torch.optim.SGD(model.parameters(),lr=0.1)
   for epoch in range(10000):
       Ypred=model(X) #the model produces prediction output
       loss=loss_fn(Ypred, Y) #prediction and target compared by loss
       if epoch%100==0:
          print(epoch, loss.item()) #print current loss value
       optimizer.zero_grad() #optimizer sets previous gradients to zero
       loss.backward() #optimizer computes new gradients
       optimizer.step() #optimizer updates weights
       
   Ypred=model(X) # Make Predictions based on the obtained weights 
   print("Ypred training set=", Ypred) 
   loss=loss_fn(Ypred, Y)
   print("Loss on trainig set:", loss)
   Yvalpred=model(Xval) # Make Predictions based on the obtained weights 
   print("Y validation set=", Yvalpred) 
   loss=loss_fn(Yvalpred, Yval)
   print("Loss on validation set:", loss)
   
   weights = model.state_dict()   #read obtained weights
   print("weights=", weights)
   
   
