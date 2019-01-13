from matplotlib import pyplot as plt
import numpy as np

class MetaData:
    def __init__(self, file_name, rows, label=""):
        self.file_name = file_name
        self.rows = rows
        self.label = label
        
class MatplotlibTemplate:
    def __init__(self, vsplit, hsplit, metadata_list, real_time=False, split_char=" "):
        self.fig = plt.figure(figsize=(6, 4))
        
        self.axes = [[0 for h in range(hsplit)] for v in range(vsplit)]
        self.lines = [[[0 for i in range(len(metadata_list[v][h]))] for h in range(hsplit)] for v in range(vsplit)]
        for v in range(vsplit):
            for h in range(hsplit):
                self.axes[v][h] = self.fig.add_subplot(vsplit, hsplit, h + 1 + v * hsplit)
                for metadata_idx in range(len(metadata_list[v][h])):
                    metadata = metadata_list[v][h][metadata_idx]
                    with open(metadata.file_name, "r") as f:
                        x = []
                        y = []
                        cnt = 0
                        for line in f:
                            number_vector = line[:-1].split(split_char)
                            if number_vector == ["\n"] or number_vector == [""]:
                                continue
                            if metadata.rows[0] == -1:
                                x.append(cnt)
                            else:
                                x.append(float(number_vector[metadata.rows[0]]))
                            y.append(float(number_vector[metadata.rows[1]]))
                            cnt += 1
                        self.lines[v][h][metadata_idx], = self.axes[v][h].plot(np.array(x), np.array(y))#, label[v][h][i])

    def execute(self):
        plt.show()
    
if __name__ == "__main__":
    a = [MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log_with_robust.log", [-1, 2], "Pitch"),
         MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log_with_robust.log", [-1, 3], "Yaw")]
    b = [MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log.log", [-1, 0], "u1"),
         MetaData("/home/takayuki/ros/kinetic/src/jsk_diabolo_pr2/log/log-by-logger/sample_log.log", [-1, 1], "u2")]
    
    plotter = MatplotlibTemplate(2, 1,
                                 [[a],
                                  [b]])

    '''
    plotter = MatplotlibTemplate(3, 2,
                                 [[a, b, c],
                                  [d, e, f]])
    '''
    
    plotter.execute()
