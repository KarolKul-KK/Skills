import numpy

past_velocity = 0
momentum = 0.1
while loss > 0.1:
    w, loss, gradient = get_current_parametrs()
    velocity = past_velocity * momentum + learning_rate * gradient
    w=w+momentum * velocity - learning_rate * gradient
    past_velocity = velocity
    upadte_parameter(w)