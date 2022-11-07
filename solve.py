list = input().split()
res_d = dict()
def main(list):
    
    try:
        N_DataCenter = int(list[0])
        N_Servers    = int(list[1])
        N_Operations = int(list[2])
        Data_Servers = [0] 
        
        res_d = {a: a * 0 for a in range(1,N_DataCenter+1)}
        
        for i in range(N_DataCenter):
            Data_Servers.append([1] * N_Servers)
            
        for i in range(0, N_Operations):
            count_reset = 0
            operation_name = input().split()
            
            try:
                _OPERATION = str(operation_name[0])
                _DATA      = int(operation_name[1])
                _SERVER    = int(operation_name[2])    
            except IndexError:
                pass
            if   _OPERATION == 'DISABLE':
                Data_Servers[_DATA][_SERVER-1] = 0
                
            elif _OPERATION == 'GETMAX':
                Ws = []
                get_max = []
                for i in range(1, N_DataCenter+1):
                    Work_servers = Ws.append(Data_Servers[i].count(1))   
                try:
                    for i in Ws:
                        get_max.append(res_d[i] * i)
                    for i in get_max:
                        if get_max.count(i) > 1:
                            print(get_max.index(i) + 1)
                            break
                        else:
                            print(get_max.index(max(get_max)) + 1)
                            break
                except KeyError:
                    pass
                
            elif _OPERATION == 'RESET':
                k = 0
                while k < N_Servers:
                    Data_Servers[_DATA][k] = 1
                    k += 1    
                count_reset += 1
                reset_dict(res_d, count_reset, _DATA)
                               
            elif _OPERATION == 'GETMIN':    
                Ws = []
                get_max = []
                for i in range(1, N_DataCenter+1):
                    Work_servers = Ws.append(Data_Servers[i].count(1))   
                try:
                    for i in Ws:
                        get_max.append(res_d[i] * i)
                    for i in get_max:
                        if get_max.count(i) > 1:
                            print(get_max.index(i) + 1)
                            break
                        else:
                            print(get_max.index(min(get_max))+1)
                            break          
                except KeyError:
                    pass
            
    except Exception as e:
        print(f'Error: {e}')
        
def reset_dict(res_d, k:int, Num_data:str):
    try:
        if Num_data in res_d.keys():
            k = res_d[Num_data] + 1
            res_d.update([(Num_data,k)])
            k = 0
        else:
            res_d.update([(Num_data,k)])
    except Exception as e:
        print(f"Error of dict: {e}")

def large(arr): 
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
           max_ = ele
        else:
            return 0
    return max_         
            
main(list)