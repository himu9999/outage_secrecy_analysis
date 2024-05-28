pip install numpy matplotlib
import numpy as np
import matplotlib.pyplot as plt
# Define the simulation parameters
num_d2d_pairs = np.arange(1, 6)  # Number of D2D pairs from 1 to 5
max_transmit_power = np.arange(10, 35, 5)  # Transmit power from 10 to 30 dBm
def simulate_mode_selection_with_ris(num_pairs, power):
    # Placeholder for the actual simulation logic
    return 200 + num_pairs * 100 + power * 10

def simulate_mode_selection_without_ris(num_pairs, power):
    # Placeholder for the actual simulation logic
    return 150 + num_pairs * 80 + power * 5

def simulate_reuse_mode_with_ris(num_pairs, power):
    # Placeholder for the actual simulation logic
    return 180 + num_pairs * 90 + power * 8

def simulate_reuse_mode_without_ris(num_pairs, power):
    # Placeholder for the actual simulation logic
    return 120 + num_pairs * 60 + power * 3

def simulate_random_selection_1(num_pairs, power):
    # Placeholder for the actual simulation logic
    return 100 + num_pairs * 50 + power * 2

def simulate_random_selection_2(num_pairs, power):
    # Placeholder for the actual simulation logic
    return 90 + num_pairs * 40 + power * 1
# Initialize result arrays
results_pairs = {
    "Mode selection with RIS": [],
    "Mode selection without RIS": [],
    "Reuse mode with RIS": [],
    "Reuse mode without RIS": [],
    "Random Selection_1": [],
    "Random Selection_2": []
}

results_power = {
    "Mode selection with RIS": [],
    "Mode selection without RIS": [],
    "Reuse mode with RIS": [],
    "Reuse mode without RIS": [],
    "Random Selection_1": [],
    "Random Selection_2": []
}

# Simulate for number of D2D pairs
for pairs in num_d2d_pairs:
    results_pairs["Mode selection with RIS"].append(simulate_mode_selection_with_ris(pairs, 20))
    results_pairs["Mode selection without RIS"].append(simulate_mode_selection_without_ris(pairs, 20))
    results_pairs["Reuse mode with RIS"].append(simulate_reuse_mode_with_ris(pairs, 20))
    results_pairs["Reuse mode without RIS"].append(simulate_reuse_mode_without_ris(pairs, 20))
    results_pairs["Random Selection_1"].append(simulate_random_selection_1(pairs, 20))
    results_pairs["Random Selection_2"].append(simulate_random_selection_2(pairs, 20))

# Simulate for maximum transmit power
for power in max_transmit_power:
    results_power["Mode selection with RIS"].append(simulate_mode_selection_with_ris(3, power))
    results_power["Mode selection without RIS"].append(simulate_mode_selection_without_ris(3, power))
    results_power["Reuse mode with RIS"].append(simulate_reuse_mode_with_ris(3, power))
    results_power["Reuse mode without RIS"].append(simulate_reuse_mode_without_ris(3, power))
    results_power["Random Selection_1"].append(simulate_random_selection_1(3, power))
    results_power["Random Selection_2"].append(simulate_random_selection_2(3, power))
# Plot results for number of D2D pairs
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
for key in results_pairs:
    plt.plot(num_d2d_pairs, results_pairs[key], label=key)
plt.xlabel('Number of D2D pairs')
plt.ylabel('Average sum data rate (kb/s)')
plt.legend()
plt.grid(True)

# Plot results for maximum transmit power
plt.subplot(1, 2, 2)
for key in results_power:
    plt.plot(max_transmit_power, results_power[key], label=key)
plt.xlabel('Maximum transmit power of D2D pairs (dBm)')
plt.ylabel('Average sum data rate (kb/s)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
