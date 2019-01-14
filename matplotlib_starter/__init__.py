import pkg_resources

__version__ = pkg_resources.get_distribution(
        'matplotlib_starter').version



from matplotlib import pyplot as plt
import numpy as np

class MetaData:
    def __init__(self, file_name, rows, label="", color=None, marker=None, start=None, end=None, thin_out=1, plot_type="plot", lambda_function=[lambda x:x, lambda x:x]):
        self.file_name = file_name
        self.rows = rows    # rows of x, y in file
        self.label = label
        self.color = color
        self.marker = marker
        self.start = start   # plot from x of self.start
        self.end = end   # plot by x of self.end
        self.thin_out = thin_out
        self.plot_type = plot_type
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
                    label = metadata.label
                    color = metadata.color
                    marker = metadata.marker
                    start = metadata.start
                    end = metadata.end
                    thin_out = metadata.thin_out
                    plot_type = metadata.plot_type
                    lambda_x = metadata.lambda_function[0]
                    lambda_y = metadata.lambda_function[1]
                    
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

                            # start and end
                            if start != None and x < start:
                                continue
                            elif end != None and x > end:
                                continue
                            if start != None:
                                x = x - start

                            # thin out
                            if cnt % thin_out != 0:
                                continue
                            
                            x_list.append(x)                                
                            y_list.append(y)

                        if plot_type == "plot":
                            self.lines[v][h][metadata_idx], = self.axes[v][h].plot(np.array(x_list), np.array(y_list), marker=marker, label=metadata.label, color=color)
                        elif plot_type == "scatter":
                            #self.lines[v][h][metadata_idx], = self.axes[v][h].scatter(np.array(x_list), np.array(y_list), marker=marker, label=metadata.label, color=color)                            
                            self.axes[v][h].scatter(np.array(x_list), np.array(y_list), marker=marker, label=metadata.label, color=color)                            
                self.axes[v][h].legend()
                
        plt.show()
