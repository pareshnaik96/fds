import requests
import time

nodes = {
    "node1": "http://localhost:5001",
    "node2": "http://localhost:5002",
    "node3": "http://localhost:5003",
}

def put(node, key, value, clock, sender):
    url = f"{nodes[node]}/replicate"
    data = {"key": key, "value": value, "clock": clock, "sender": sender}
    res = requests.post(url, json=data)
    print(f"PUT to {node}: {res.json()}")

def get(node, key):
    url = f"{nodes[node]}/get?key={key}"  # ✅ Corrected here
    res = requests.get(url)
    print(f"GET from {node}: {res.json()}")

# Simulate causal scenario
print("---- Step 1: node1 writes x=A ----")
put("node1", "x", "A", {"node1": 1, "node2": 0, "node3": 0}, "node1")
time.sleep(1)

print("---- Step 2: node2 reads x ----")
get("node2", "x")
time.sleep(1)

print("---- Step 3: node2 writes x=B ----")
put("node2", "x", "B", {"node1": 1, "node2": 1, "node3": 0}, "node2")
time.sleep(1)

print("---- Step 4: node3 reads x ----")
get("node3", "x")
