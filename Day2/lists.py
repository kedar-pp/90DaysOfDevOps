# Creating a list
servers = ['server1', 'server2', 'server3']
print(servers)  # Output: ['server1', 'server2', 'server3']

# Append - Adding a new server to the list
servers.append('server4')
print(servers)  # Output: ['server1', 'server2', 'server3', 'server4']

# Insert - Adding a server at a specific position
servers.insert(1, 'server5')
print(servers)  # Output: ['server1', 'server5', 'server2', 'server3', 'server4']

# Length - Finding the number of servers
num_servers = len(servers)
print(f"Number of servers: {num_servers}")  # Output: Number of servers: 5