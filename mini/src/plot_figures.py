import pandas as pd
import matplotlib.pyplot as plt


def read_and_average_results(file_name):
    with open(file_name+".txt") as f:
        data = [float(line.rstrip('\n')) for line in f]
        average = sum(data)/len(data)
        return average

rl_5 = read_and_average_results("results/out-5-RL")
rl_10 = read_and_average_results("results/out-10-RL")
rl_20 = read_and_average_results("results/out-20-RL")
#rl_30 = read_and_average_results("results/out-30-RL")
gr_5 = read_and_average_results("results/out-5-Greedy")
gr_10 = read_and_average_results("results/out-10-Greedy")
gr_20 = read_and_average_results("results/out-20-Greedy")
#gr_30 = read_and_average_results("results/out-30-Greedy")
cl_5 = read_and_average_results("results/out-5-Cloud")
cl_10 = read_and_average_results("results/out-10-Cloud")
cl_20 = read_and_average_results("results/out-20-Cloud")
#cl_30 = read_and_average_results("results/out-30-Cloud")
rn_5 = read_and_average_results("results/out-5-Random")
rn_10 = read_and_average_results("results/out-10-Random")
rn_20 = read_and_average_results("results/out-20-Random")
#rn_30 = read_and_average_results("results/out-30-Random")
print(cl_10)

rl_values = [rl_5, rl_10, rl_20]
greedy_values = [gr_5, gr_10, gr_20]
cloud_values = [cl_5, cl_10, cl_20]
random_values = [rn_5, rn_10, rn_20]


index = ['Case 1', 'Case 2', 'Case 3']
df = pd.DataFrame({'DRL': rl_values,
                    'MWF': greedy_values,
                    "FOG-Only":cloud_values,
                    "Random":random_values,
                    }, index=index)
ax = df.plot.bar(rot=0, width=0.8, color={"DRL": "pink", "MWF": "grey", "FOG-Only": "green", "Random": "red"})
ax.set_axisbelow(True)
bars = ax.patches
hatches = ["\\\\","\\\\","\\\\","//","//","//","..","..","..","..","..",".."]
for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)
ax.yaxis.grid(color='blue', linestyle='dashed')
plt.ylabel("Avg. Task Delay (s)")
plt.legend(fontsize="large")
plt.show()
