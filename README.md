Matplotlib Starter
=================

Start Plotting with Matplotlib easily and freely.

You can designate below infomation for each graph.

| variable name | description |
----|----
| file_name | file_name |
| rows | rows of X, Y value of graph in the file |
| label | name of graph |
| color | color of graph |
| marker | shape of point of plot |
| start | X value when to start plotting |
| end | X value when to end plotting |
| thin_out | thin out each thin_out points from raw data |
| plot_type | plot or scatter |
| lambda_function | lambda function of data processing for X, Y value |

## Install
```bash
$ git clone https://github.com/takayuki5168/matplotlib-starter.git
$ cd matplotlib-starter
$ pip install --user .
```

## Example
```python
from matplotlib_starter import MatplotlibStarter, MetaData
import sys, signal

signal.signal(signal.SIGINT, lambda signal, frame: sys.exit(0))

ax11 = [MetaData("sample.log", [-1, 2], label="Pitch"),
        MetaData("sample.log", [-1, 3], label="Yaw")]
ax12 = [MetaData("sample.log", [-1, 2], label="Pitch", color="blue", marker="*", end=2, lambda_function=[lambda x:x/100., lambda x:x]),
       MetaData("sample.log", [-1, 3], label="Yaw", color="green", marker="*", end=2, lambda_function=[lambda x:x/100., lambda x:x])]
ax13 = [MetaData("sample.log", [-1, 2], label="Pitch", color="blue", thin_out=20, plot_type="scatter", lambda_function=[lambda x:x/100., lambda x:x]),
       MetaData("sample.log", [-1, 3], label="Yaw", color="green", thin_out=20, plot_type="scatter", lambda_function=[lambda x:x/100., lambda x:x])]

ax21 = [MetaData("sample.log", [-1, 0], label="u1"),
        MetaData("sample.log", [-1, 1], label="u2")]
ax22 = [MetaData("sample.log", [-1, 0], label="u1", color="purple", marker="*", end=2, lambda_function=[lambda x:x/100., lambda x:x-0.7]),
       MetaData("sample.log", [-1, 1], label="u2", color="orange", marker="*", end=2, lambda_function=[lambda x:x/100., lambda x:x*20])]
ax23 = [MetaData("sample.log", [-1, 0], label="u1", color="purple", thin_out=20, plot_type="scatter", lambda_function=[lambda x:x/100., lambda x:x-0.7]),
       MetaData("sample.log", [-1, 1], label="u2", color="orange", thin_out=20, plot_type="scatter", lambda_function=[lambda x:x/100., lambda x:x*20])]

ax11_title = ["State of Diabolo (raw data)", "step", "angle[degree]"]
ax12_title = ["State of Diabolo (colored, scaled, markered, parted)", "time[s]", "angle[degree]"]
ax13_title = ["State of Diabolo (scatter, thinned out)", "time[s]", "angle[degree]"]

ax21_title = ["Control input from Robot (raw data)", "step", ""]
ax22_title = ["Control Input from Robot (colored, scaled, markered, parted)", "time[s]", ""]
ax23_title = ["Control Input from Robot (sctter, thinned out)", "time[s]", ""]

plotter = MatplotlibStarter(hspace=0.6)
plotter.execute(2, 3,
                [[ax11, ax12, ax13],
                 [ax21, ax22, ax23]],
                [[ax11_title, ax12_title, ax13_title],
                 [ax21_title, ax22_title, ax23_title]])
```

You can execute like below.

```bash
$ cd example
$ python plot.py
```

![Graph](https://github.com/takayuki5168/MatplotlibStarter/blob/master/example/image/sample.png)

See [example](https://github.com/takayuki5168/MatplotlibStarter/tree/master/example).