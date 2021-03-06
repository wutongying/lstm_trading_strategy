import caffe
#import global_var as GV
import numpy as np


class EuclideanLossLayer(caffe.Layer):
    """
    Compute the Euclidean Loss in the same manner as the C++ EuclideanLossLayer
    to demonstrate the class interface for developing layers in Python.
    """

    def setup(self, bottom, top):
        pass

    def reshape(self, bottom, top):
        self.diff = np.zeros_like(bottom[0].data, dtype=np.float32)
        top[0].reshape(1)
#        top[1].reshape(*bottom[0].data.shape)

    def forward(self, bottom, top):
        self.diff[...] = bottom[0].data - bottom[1].data.reshape(bottom[0].data.shape)
        top[0].data[...] = np.sum(self.diff**2) / bottom[0].data.size / 2
#        top[1].data[...] = self.diff[...]

    def backward(self, top, propagate_down, bottom):
        for i in range(2):
            if not propagate_down[i]:
                continue
            if i == 0:
                sign = 1
            else:
                sign = -1
            bottom[i].diff[...] = sign * self.diff / bottom[i].data.size
