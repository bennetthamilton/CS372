# Title: Project 6 - Dijkstra's and ARP Sniffing
# Name: Bennett Hamilton
# Date: 11/11/23
# Description: implement Dijkstra’s Algorithm to print out the shortest path 
#              from one IP to another IP, showing the IPs of all the routers in between.

import sys
import json
import math  # If you want to use math.inf for infinity

# helper function to get the minimum distance node from the set of nodes to visit
# ref: https://beej.us/guide/bgnet0/html/split/project-6-routing-with-dijkstras.html
def get_min_distance_node(to_visit, distance):
    min_node = None
    min_distance = math.inf

    for node in to_visit:
        if distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]

    return min_node

# helper function that performs the "relaxing" portion of dijkstra's algorithm
def relax(current_node, neighbor, routers, distance, parent):
    # compute distance from the starting node to the neighbor
    # if the computed distance is less than the neighbor’s current value in distance:
        # set neighbors distance to computed value
        # set neighbors partent to current node
    pass

# helper function to get the shortest path from source to destination
# ref: https://beej.us/guide/bgnet0/html/split/project-6-routing-with-dijkstras.html
def get_shortest_path(parent, src, dest):
    # set current node to destination node
    # initialize path as an empty array

    # while current node is not source node:
        # append current node to path
        # set current node to parent of current node
    
    # append source node to path
    # reverse path (correct order)
    # return path
    pass

# ref: https://beej.us/guide/bgnet0/html/split/project-6-routing-with-dijkstras.html
def dijkstras_shortest_path(routers, src_ip, dest_ip):
    """
    This function takes a dictionary representing the network, a source
    IP, and a destination IP, and returns a list with all the routers
    along the shortest path.

    The source and destination IPs are **not** included in this path.

    Note that the source IP and destination IP will probably not be
    routers! They will be on the same subnet as the router. You'll have
    to search the routers to find the one on the same subnet as the
    source IP. Same for the destination IP. [Hint: make use of your
    find_router_for_ip() function from the last project!]

    The dictionary keys are router IPs, and the values are dictionaries
    with a bunch of information, including the routers that are directly
    connected to the key.

    This partial example shows that router `10.31.98.1` is connected to
    three other routers: `10.34.166.1`, `10.34.194.1`, and `10.34.46.1`:

    {
        "10.34.98.1": {
            "connections": {
                "10.34.166.1": {
                    "netmask": "/24",
                    "interface": "en0",
                    "ad": 70
                },
                "10.34.194.1": {
                    "netmask": "/24",
                    "interface": "en1",
                    "ad": 93
                },
                "10.34.46.1": {
                    "netmask": "/24",
                    "interface": "en2",
                    "ad": 64
                }
            },
            "netmask": "/24",
            "if_count": 3,
            "if_prefix": "en"
        },
        ...

    The "ad" (Administrative Distance) field is the edge weight for that
    connection.

    **Strong recommendation**: make functions to do subtasks within this
    function. Having it all built as a single wall of code is a recipe
    for madness.
    """

    # ref: https://www.geeksforgeeks.org/python-list-comprehension/
    to_visit = set(routers.keys())
    distance = {node: math.inf for node in to_visit}
    parent = {node: None for node in to_visit}

    distance[src_ip] = 0

    while to_visit:
        current_node = get_min_distance_node(to_visit, distance)
        to_visit.remove(current_node)

        for neighbor in routers[current_node]["connections"]:
            if neighbor in to_visit:
                relax(current_node, neighbor, routers, distance, parent)
    
    # find the router on the same subnet as the destination IP (this is the destination router)
    dest_router = find_router_for_ip(routers, dest_ip)

    # find the shortest path from source to destination
    shortest_path = get_shortest_path(parent, src_ip, dest_router)

    return shortest_path

# ref: Project 5 from netfuncs.py
def find_router_for_ip(routers, ip):
    """
    Search a dictionary of routers (keyed by router IP) to find which
    router belongs to the same subnet as the given IP.

    Return None if no routers is on the same subnet as the given IP.
    """

    # ref: https://www.programiz.com/python-programming/methods/dictionary/items
    for router_ip, router_info in routers.items():
        netmask_slash = router_info.get("netmask")
        # if there is a subnet match then return that ipv4 address
        if ips_same_subnet(router_ip, ip, netmask_slash):
            return router_ip

    return None    # if there are no routers with matching subnet

# ref: Project 5 from netfuncs.py
def ips_same_subnet(ip1, ip2, slash):
    """
    Given two dots-and-numbers IP addresses and a subnet mask in slash
    notataion, return true if the two IP addresses are on the same
    subnet.

    Returns a boolean.
    """

    # ref: https://beej.us/guide/bgnet0/html/split/ip-subnets-and-subnet-masks.html
    subnet_mask = get_subnet_mask_value(slash)
    
    # convert ipv4 addresses to 32 bit integer value
    ip1_value = ipv4_to_value(ip1)
    ip2_value = ipv4_to_value(ip2)

    # use mask to get subnets from ipv4 addresses
    ip1_subnet = ip1_value & subnet_mask
    ip2_subnet = ip2_value & subnet_mask

    # compare, return true or false
    return ip1_subnet == ip2_subnet

# ref: Project 5 from netfuncs.py
def get_subnet_mask_value(slash):
    """
    Given a subnet mask in slash notation, return the value of the mask
    as a single number of integer type. The input can contain an IP
    address optionally, but that part should be discarded.

    Returns an integer type.
    """
    TOTAL_BITS = 32
    # get only the slash and following number
    length = int(slash.split("/")[1])

    # calculate mask value using prefix length
    mask_value = (0xffffffff << (TOTAL_BITS - length)) & 0xffffffff

    return mask_value

# ref: Project 5 from netfuncs.py
def ipv4_to_value(ipv4_addr):
    """
    Convert a dots-and-numbers IP address to a single 32-bit numeric
    value of integer type. 
    
    Returns an integer type.
    """

    ipv4_addr_bytes = ipv4_addr.split(".")

    # no need to convert to hex since its the same value, therefore bitwise function is the same
    # ref: https://beej.us/guide/bgnet0/html/split/ip-subnets-and-subnet-masks.html
    ipv4_value = 0
    for part in ipv4_addr_bytes:
        ipv4_value = (ipv4_value << 8) | int(part)

    return ipv4_value

#------------------------------
# DO NOT MODIFY BELOW THIS LINE
#------------------------------
def read_routers(file_name):
    with open(file_name) as fp:
        data = fp.read()

    return json.loads(data)

def find_routes(routers, src_dest_pairs):
    for src_ip, dest_ip in src_dest_pairs:
        path = dijkstras_shortest_path(routers, src_ip, dest_ip)
        print(f"{src_ip:>15s} -> {dest_ip:<15s}  {repr(path)}")

def usage():
    print("usage: dijkstra.py infile.json", file=sys.stderr)

def main(argv):
    try:
        router_file_name = argv[1]
    except:
        usage()
        return 1

    json_data = read_routers(router_file_name)

    routers = json_data["routers"]
    routes = json_data["src-dest"]

    find_routes(routers, routes)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    
