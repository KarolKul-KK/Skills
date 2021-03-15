import numpy as np


# variables
timesteps = 100
input_features = 32
output_features = 64

# random input data
inputs = np.random.random((timesteps, input_features))

# vector contain only 0 values
state_t = np.zeros((output_features))

# create random matrix
W = np.random.random((output_features, input_features))
U = np.random.random((output_features, output_features))
b = np.random.random((output_features))

successive_outputs = []
for input_t in inputs:
    output_t = np.tanh(np.dot(W, input_t) + np.dot(U, state_t) + b)


    # saving output values in list
    successive_outputs.append(output_t)

    # updating
    state_t = output_t

# final output, tensor 2d(timesteps, output_features)
final_output_sequence = np.concatenate(successive_outputs, axis=0)
