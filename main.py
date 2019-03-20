import os                                                                       
from multiprocessing import Pool                                                
                                                                                
                                                                                
processes = ('4.py', '3.py','2.py')                                    
other = ('4.py',)
                                                  
                                                                                
def run_process(process):                                                             
    os.system('python {}'.format(process))                                       
                                                                                
                                                                                
pool = Pool(processes=3)                                                        
pool.map(run_process, processes) 
pool.map(run_process, other) 
