Matplotlib Starter
=================

Start Plotting with Matplotlib easily and freely.

You can designate below infomation for each graph.
- file_name        file_name
- rows             rows of x, y value of graph in the file
- label            name of graph
- color            color of graph
- start            x value when to start plotting
- end              x value when to end plotting
- lambda_function  lambda function of data processing for x, y value

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

ax1 = [MetaData("sample.log", [-1, 2], label="Pitch", color="blue", lambda_function=[lambda x:x/100., lambda x:x]),
       MetaData("sample.log", [-1, 3], label="Yaw", color="green", lambda_function=[lambda x:x/100., lambda x:x])]
ax2 = [MetaData("sample.log", [-1, 0], label="u1", color="purple", lambda_function=[lambda x:x/100., lambda x:x-0.7]),
       MetaData("sample.log", [-1, 1], label="u2", color="orange", lambda_function=[lambda x:x/100., lambda x:x*20])]

ax1_title = ["State of Diabolo", "time[s]", "angle[degree]"]
ax2_title = ["Control Input from Robot", "time[s]", ""]

plotter = MatplotlibStarter(hspace=0.6)
plotter.execute(2, 1,
                [[ax1],
                 [ax2]],
                [[ax1_title],
                 [ax2_title]])
```

You can execute like below.

See [example](https://github.com/takayuki5168/matplotlib-starter/example).

```bash
$ cd example
$ python plot.py
```

![Graph](https://github.com/takayuki5168/MatplotlibStarter/blob/master/example/image/sample.png)