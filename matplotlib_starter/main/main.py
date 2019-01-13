from matplotlib import pyplot as plt
import numpy as np

import sys, signal

class MetaData:
    def __init__(self, file_name, rows, label="", color=None, start=None, end=None, lambda_function=[lambda x:x, lambda x:x]):
        self.file_name = file_name
        self.rows = rows    # rows of x, y in file
        self.label = label
        self.color = color
        self.start = start   # plot from x after self.start
        self.end = end   # plot by x after self.end
        self.lambda_function = lambda_function   # convert x, y raw values in file, with your customized function
        
class MatplotlibStarter:
    def __init__(self, wspace=None, hspace=None):
        self.fig = plt.figure()
        self.fig.subplots_adjust(wspace=wspace, hspace=hspace)

    def execute(self, vsplit, hsplit, metadata_list, titles_list, real_time=False, split_char=" "):
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
                    end = metadata.end
                    
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
                            elif end != None and x > end:
                                continue
                            if start != None:
                                x = x - start
                            
                            x_list.append(x)                                
                            y_list.append(y)
                            
                        print(label)
                        if color == None:
                            self.lines[v][h][metadata_idx], = self.axes[v][h].plot(np.array(x_list), np.array(y_list), label=metadata.label)
                        else:
                            self.lines[v][h][metadata_idx], = self.axes[v][h].plot(np.array(x_list), np.array(y_list), label=metadata.label, color=color)
                self.axes[v][h].legend()
                
        plt.show()
    
if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda signal, frame: sys.exit(0))

    '''
    ax1 = [MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log.log", [-1, 2], label="Pitch", color="blue", lambda_function=[lambda x:x/100., lambda x:x]),
         MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log.log", [-1, 3], label="Yaw", color="green", lambda_function=[lambda x:x/100., lambda x:x])]
    ax2 = [MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log.log", [-1, 0], label="u1", color="purple", lambda_function=[lambda x:x/100., lambda x:x-0.7]),
         MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log.log", [-1, 1], label="u2", color="orange", lambda_function=[lambda x:x/100., lambda x:x*20])]
    '''
    ax1 = [MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log_with_robust.log", [-1, 2], label="Pitch", color="blue", lambda_function=[lambda x:x/100., lambda x:x], start=33, end=48),
         MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log_with_robust.log", [-1, 3], label="Yaw", color="green", lambda_function=[lambda x:x/100., lambda x:x], start=32, end=48)]
    ax2 = [MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log_with_robust.log", [-1, 0], label="u1", color="purple", lambda_function=[lambda x:x/100., lambda x:x-0.7], start=32, end=48),
         MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log_with_robust.log", [-1, 1], label="u2", color="orange", lambda_function=[lambda x:x/100., lambda x:x*20], start=32, end=48)]


    
    ax1_title = ["State of Diabolo", "time[s]", "angle[degree]"]
    ax2_title = ["Control Input from Robot", "time[s]", ""]
    
    plotter = MatplotlibStarter(hspace=0.6)
    plotter.execute(2, 1,
                    [[ax1],
                     [ax2]],
                    [[ax1_title],
                     [ax2_title]])

    '''
    plotter = MatplotlibStarter(3, 2,
                                 [[a, b, c],
                                  [d, e, f]])
    '''
