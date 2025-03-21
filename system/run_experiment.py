import subprocess

algos = ["FedAvg"]
datasets = ["NSLKDD"]
jr = "1"
client_activity_rate = "0"
batch_size = "64"
num_clients = 50
num_classes = 10

for algo in algos:
    for dataset in datasets:
        go_value = f"_nc{num_clients}"
        command = [
            "python",
            "main.py",
            "-algo", algo,
            "-jr", jr,
            "-data", dataset,
            "-go", go_value,
            "-nc", str(num_clients),
            "-nb", str(num_classes),
            "-car", client_activity_rate,
            "-lbs", batch_size
        ]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running command: {e}")