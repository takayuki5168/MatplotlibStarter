from matplotlib import pyplot as plt
import numpy as np

import sys, signal

class MetaData:
    def __init__(self, file_name, rows, label="", color=None, start=None, lambda_function=[lambda x:x, lambda x:x]):
        self.file_name = file_name
        self.rows = rows    # rows of x, y in file
        self.label = label
        self.color = color
        self.start = start   # plot from x after self.start
        self.lambda_function = lambda_function   # convert x, y raw values in file, with your customized function
        
class MatplotlibStarter:
    def __init__(self, vsplit, hsplit, metadata_list, titles_list, real_time=False, split_char=" "):
        self.fig = plt.figure(figsize=(6, 4))
        
        self.axes = [[0 for h in range(hsplit)] for v in range(vsplit)]
        self.lines = [[[0 for i in range(len(metadata_list[v][h]))] for h in range(hsplit)] for v in range(vsplit)]
        for v in range(vsplit):
            for h in range(hsplit):
                self.axes[v][h] = self.fig.add_subplot(vsplit, hsplit, h + 1 + v * hsplit)
                self.axes[v][h].set_title(titles_list[v][h][0])
                self.axes[v][h].set_xlabel(titles_list[v][h][1])
                self.axes[v][h].set_ylabel(titles_list[v][h][2])
                for metadata_idx in range(len(metadata_list[v][h])):
                    metadata = metadata_list[v][h][metadata_idx]
                    lambda_x = metadata.lambda_function[0]
                    lambda_y = metadata.lambda_function[1]
                    label = metadata.label
                    color = metadata.color
                    start = metadata.start
                    
                    with open(metadata.file_name, "r") as f:
                        x_list = []
                        y_list = []
                        cnt = 0
                        for line in f:
                            number_vector = line[:-1].split(split_char)
                            if number_vector == ["\n"] or number_vector == [""]:
                                continue
                            
                            if metadata.rows[0] == -1:
                                x = lambda_x(cnt)
                            else:
                                x = lambda_x(float(number_vector[metadata.rows[0]]))
                            y = lambda_y(float(number_vector[metadata.rows[1]]))
                            cnt += 1

                            if start != None and x < start:
                                continue
                            
                            x_list.append(x)                                
                            y_list.append(y)
                            
                        print(label)
                        if color == None:
                            self.lines[v][h][metadata_idx], = self.axes[v][h].plot(np.array(x_list), np.array(y_list), label=metadata.label)
                        else:
                            self.lines[v][h][metadata_idx], = self.axes[v][h].plot(np.array(x_list), np.array(y_list), label=metadata.label, color=color)
                self.axes[v][h].legend()

    def execute(self):
        plt.show()
    
if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda signal, frame: sys.exit(0))

    '''
    ax1 = [MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log_with_robust.log", [-1, 2], label="Pitch", color="blue", start=3200),
         MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log_with_robust.log", [-1, 3], label="Yaw", color="green", start=3200)]
    ax2 = [MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log_with_robust.log", [-1, 0], label="u1", color="purple", start=3200, lambda_function=[lambda x:x, lambda x:x-0.7]),
         MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log_with_robust.log", [-1, 1], label="u2", color="orange", start=3200, lambda_function=[lambda x:x, lambda x:x*20])]
    '''

    ax1 = [MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log.log", [-1, 2], label="Pitch", color="blue"),
         MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log.log", [-1, 3], label="Yaw", color="green")]
    ax2 = [MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log.log", [-1, 0], label="u1", color="purple", lambda_function=[lambda x:x, lambda x:x-0.7]),
         MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log.log", [-1, 1], label="u2", color="orange", lambda_function=[lambda x:x, lambda x:x*20])]

    
    ax1_title = ["State of Diabolo", "step", "degree"]
    ax2_title = ["Manipulation from Robot", "step", ""]
    
    plotter = MatplotlibStarter(2, 1,
                                 [[ax1],
                                  [ax2]],
                                 [[ax1_title],
                                  [ax2_title]])

    '''
    plotter = MatplotlibStarter(3, 2,
                                 [[a, b, c],
                                  [d, e, f]])
    '''
    
    plotter.execute()
