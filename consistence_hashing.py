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
                    self.hash_ring[server_hash_value] = new_server_node
            respnse = {"message":"server added successfully"}
        except Exception :
            respnse = {"message": "something went wrong, Please try again."}
        return respnse
    
    
    def remove_server(self,remove_server):
        response = {}
        if remove_server is None:
            response['error'] = "Please provide valid server."
        if response.get('error',''):
            return response
        try:
            node_list = [node for node in self.node if node.key==remove_server]
            for remove_server_node in node_list:
                self.node.remove(remove_server_node)
                for replica_server in range(self.virtual):
                    remove_server_key = f"{remove_server}:{replica_server}"
                    hash_value = hashlib.md5(remove_server_key.encode()).hexdigest()
                    if hash_value in self.hash_ring:
                        del self.hash_ring[hash_value]
            respnse = {"message":"server removed successfully"}
        except Exception:
             respnse = {"message": "something went wrong, Please try again."}
        return response
    
    
    def get_data_store_node(self,data):
        if data is None:
            return None
        response = {}
        try:
            insert_data_hash_value = hashlib.md5(data.e3ncode()).hexdigest()
            for hash_value,server_node in self.hash_ring.items():
                if hash_value >= insert_data_hash_value:
                    response = {"message":"Data store at server_node :" f"{hash_value}"}
                    return response
            return self.hash_ring[0]
        except Exception:
            response = {"message": "something went wrong, Please try again."}
        return response
            
            