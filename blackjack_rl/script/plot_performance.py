from matplotlib import pyplot as plt
import os, pickle

# data dir
data_dir = "../../data"
lspi_path = os.path.join(data_dir, "lspi_rewards.txt")
monte_path = os.path.join(data_dir, "monte_rewards.txt")
qlearning_path = os.path.join(data_dir, "qlearning_rewards.txt")
plot_path = os.path.join(data_dir, "performance.jpg")


def plot_performance():
    paths = [lspi_path, monte_path, qlearning_path]
    names = ["lspi", "monte", "qlearning"]
    fig = plt.figure()
    x = list(range(100))
    for idx, path in enumerate(paths):
        if os.path.exists(path):
            with open(path, "rb") as f:
                data = pickle.load(f)
                print(data)
                ax = fig.add_subplot(1, 1, 1)
                ax.plot(x, data, label=names[idx])
                ax.set_xlabel('epoch')
                ax.set_ylabel('reward')
    plt.legend()
    plt.show()
    fig.savefig(plot_path)


if __name__ == '__main__':
    plot_performance()