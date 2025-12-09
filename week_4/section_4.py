import random

# Section 4: Worm Propagation Simulation
# list to hold the network
network = []
number_of_computers = 20


# Status 0 = clean, Status 1 = infected
for i in range(number_of_computers):
    ip_address = "192.168.1." + str(i)
    network.append([ip_address, 0]) 

# Infection first computer
network[0][1] = 1
print("Start: Computer " + network[0][0] + " is infected!")

# Run the simulation for 5 time steps
for time_step in range(1, 6):
    print("\n--- Time Step: " + str(time_step) + " ---")
    
    # Find out who is currently infected
    infected_indices = []
    for i in range(len(network)):
        if network[i][1] == 1:
            infected_indices.append(i)
    
    # Each infected computer tries to infect 2 others
    for infected_index in infected_indices:
        # Try 2 times
        for attempt in range(2):
            # Pick a random target index between 0 and 19
            target = random.randint(0, number_of_computers - 1)
            
            # Check if the target is already infected
            if network[target][1] == 0:
                network[target][1] = 1
                print("Success: Host " + network[target][0] + " is now infected.")
            else:
                # pass if already infected
                pass

    # Count how many are infected now
    total_count = 0
    for computer in network:
        if computer[1] == 1:
            total_count = total_count + 1
            
    print("Total infected computers: " + str(total_count) + " out of " + str(number_of_computers))

    # Stop if everyone is infected
    if total_count == number_of_computers:
        print("Network is fully compromised.")
        break