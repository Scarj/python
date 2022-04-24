#Begin Portion 2#
import random

from course01.assignment.balancer.Server import Server


class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        while server.load() >= 90:
            server = random.choice(self.servers)
        self.connections[connection_id] = server
        server.add_connection(connection_id)
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        if connection_id in self.connections:
            server = self.connections[connection_id]
            server.close_connection(connection_id)
            del self.connections[connection_id]

    def avg_load(self):
        """Calculates the average load of all servers"""
        result = 0
        for server in self.connections.values():
            result += server.load()
        # Sum the load of each server and divide by the amount of servers
        return result / len(self.servers)

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            self.servers.append(Server())
        pass

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#