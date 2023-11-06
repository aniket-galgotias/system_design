import hashlib
class Node:
    def __init__(self,server):
        self.server = server
        self.next = None
        
class ConsistenceHashing:
    def __init__(self,virtual=4):
        self.virtual=virtual
        self.node=[]
        self.hash_ring={}
    
    def add_server(self,server):
        response = {}
        if server is None:
            response['error'] = "Please provide valid server."
        if response.get('error',''):
            return response
        try:
            for replica_server in range(self.virtual):
                new_server_key = f"{server}:{replica_server}"
                server_hash_value = hashlib.md5(new_server_key.encode()).hexdigest()
                new_server_node = Node(server)
                self.node.append(new_server_key)
                if server_hash_value not in self.hash_ring:
                    self.hash_ring[server_hash_value] = new_server_key
            respnse = {"message":"server added successfully"}
        except Exception :
            respnse = {"message": "something went wrong, Please try again."}
        return respnse
    
    
            
            