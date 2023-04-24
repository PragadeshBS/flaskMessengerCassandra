from cassandra.cluster import Cluster

cluster = Cluster(['40.87.13.169'], port=9042)
# cluster = Cluster(['40.76.203.235'], port=9042)

session = cluster.connect('test')

print("connection successful")