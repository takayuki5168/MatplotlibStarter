from matplotlib_starter import MatplotlibStarter, MetaData
import sys, signal

# SigIntHandler
signal.signal(signal.SIGINT, lambda signal, frame: sys.exit(0))

# set Graph Information
ax11 = [MetaData("sample.log", [-1, 2], label="Pitch"),
        MetaData("sample.log", [-1, 3], label="Yaw")]
ax12 = [MetaData("sample.log", [-1, 2], label="Pitch", color="blue", marker=".", end=2, lambda_function=[lambda x:x/100., lambda x:x]),
       MetaData("sample.log", [-1, 3], label="Yaw", color="green", marker="o", end=2, lambda_function=[lambda x:x/100., lambda x:x])]
ax13 = [MetaData("sample.log", [-1, 2], label="Pitch", color="blue", thin_out=20, plot_type="scatter", lambda_function=[lambda x:x/100., lambda x:x]),
       MetaData("sample.log", [-1, 3], label="Yaw", color="green", thin_out=20, plot_type="scatter", lambda_function=[lambda x:x/100., lambda x:x])]

ax21 = [MetaData("sample.log", [-1, 0], label="u1"),
        MetaData("sample.log", [-1, 1], label="u2")]
ax22 = [MetaData("sample.log", [-1, 0], label="u1", color="purple", marker="^", end=2, lambda_function=[lambda x:x/100., lambda x:x-0.7]),
       MetaData("sample.log", [-1, 1], label="u2", color="orange", marker="*", end=2, lambda_function=[lambda x:x/100., lambda x:x*20])]
ax23 = [MetaData("sample.log", [-1, 0], label="u1", color="purple", thin_out=20, plot_type="scatter", lambda_function=[lambda x:x/100., lambda x:x-0.7]),
       MetaData("sample.log", [-1, 1], label="u2", color="orange", thin_out=20, plot_type="scatter", lambda_function=[lambda x:x/100., lambda x:x*20])]

# set Title Information
ax11_title = ["State of Diabolo (raw data)", "step", "angle[degree]"]
ax12_title = ["State of Diabolo (colored, scaled, markered, parted)", "time[s]", "angle[degree]"]
ax13_title = ["State of Diabolo (colored, scatter, thinned out)", "time[s]", "angle[degree]"]

ax21_title = ["Control input from Robot (raw data)", "step", ""]
ax22_title = ["Control Input from Robot (colored, scaled, markered, parted)", "time[s]", ""]
ax23_title = ["Control Input from Robot (colored, sctter, thinned out)", "time[s]", ""]

# Execute
plotter = MatplotlibStarter(hspace=0.6)
plotter.execute(2, 3,
                [[ax11, ax12, ax13],
                 [ax21, ax22, ax23]],
                [[ax11_title, ax12_title, ax13_title],
                 [ax21_title, ax22_title, ax23_title]])

