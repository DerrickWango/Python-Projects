



























from tkinter import *





































from tkinter import ttk
















































































































import math






































root = Tk()




























































































































equation = IntVar()





















































equa =''





















































































def btnPress(num,event=None):


























































































































    
    global equa





































    








    
    equa = equa + str(num)





















    
    equation.set(equa)
 



























































def EqualPress(event=None):















































    
    global equa










    
    try:




        




        

    
        total = str(eval(equa))































        
        equation.set(total)










        
        equa = ""


















        
    except:




        









        
        equation.set("Error")






        








        
def ClearPress(event=None):





























































































    
    global equa








    
    equa = ""
































































    
    equation.set("")





    
 

'''def sqroot():


























    global equa























    
    for numbut in ("7.08.09.0","4.05.06.0","1.02.03.0","0.0"):























    
        for num in numbut:






        
        
            equa = equa + str(num)
















            
            equation.set(math.sqrt(num)< ADD THIS TO FUNCTIONALITY>













































            '''
















































    
root.title('calculator')









root.resizable(width=False, height=False)










'''








































root.geometry('330x425+100+100')





























root.bind('<Return>',EqualPress)




















root.bind('<Escape>',ClearPress)




















root.bind('<1>',btnPress(1))































root.bind('<2>',btnPress(2))

















root.bind('<3>',btnPress(3))













root.bind('<4>',btnPress(4))

























root.bind('<5>',btnPress(5))











root.bind('<6>',btnPress(6))










root.bind('<7>',btnPress(7))

















root.bind('<8>',btnPress(8))



































root.bind('<9>',btnPress(9))























root.bind('<0>',btnPress(0))




#============================================================================================================================================#





















#============================================================================================================================================#















'''


























entry1= ttk.Entry(root,textvariable=equation,justify='right',font = 'arial 10 bold').grid(row=0,rowspan = 3 ,columnspan=4,sticky=W+E)
























'''



























to do:








1: Key bindings for number keys







2: make it scientific by adding keys for:









                 (i): square root







                 






                 
                 (ii): logarithms

































                 
                 (iii): cosines



































































                 
                 (iv): Tangents














































                 
                 (v): statistical tools such as:





























































                 
                          (a): Regression





























































                          
                          (b): Standard deviation.









































































































                          
                          (c): Time series.
















































                          
                          (d): Correlation, etc.
                          







































































































3: Add other configurations for keys and other additional functionalities that come with a scientific calculator.































































'''





































one = ttk.Button(root,text = '7' ,command = lambda:btnPress(7)).grid(row =4,column=0)



















































































two = ttk.Button(root,text = '8', command = lambda:btnPress(8)).grid(row =4,column=1)




































































































three =ttk. Button(root,text = '9', command = lambda:btnPress(9)).grid(row =4,column=2)



























































































four = ttk.Button(root,text = '/', command = lambda:btnPress('/')).grid(row =4,column=3)














































































five = ttk.Button(root,text = '4', command = lambda:btnPress(4)).grid(row =5,column=0)












































































six = ttk.Button(root,text = '5', command = lambda:btnPress(5)).grid(row =5,column=1)


























































































seven = ttk.Button(root,text = '6', command = lambda:btnPress(6)).grid(row =5,column=2)





























































































eight = ttk.Button(root,text = '+', command = lambda:btnPress('+')).grid(row =5,column=3)
















































































































nine = ttk.Button(root,text = '1', command = lambda:btnPress(1)).grid(row =6,column=0)





































































































































ten = ttk.Button(root,text = '2', command = lambda:btnPress(2)).grid(row =6,column=1)






















































































































eleven =ttk.Button(root,text = '3', command = lambda:btnPress(3)).grid(row =6,column=2)































































































































twelve = ttk.Button(root,text = '-', command = lambda:btnPress('-')).grid(row =6,column=3)






































































































thirteen = ttk.Button(root,text = '0', command = lambda:btnPress(0)).grid(row =7,column=0)






























































































































thirteen = ttk.Button(root,text = '^2', command = lambda:btnPress('**2')).grid(row =7,column=1)






















































































































fifteen = ttk.Button(root,text = 'x', command = lambda:btnPress('*')).grid(row =7,column=2)































































































































































sixteen = ttk.Button(root,text = 'CE',command =ClearPress).grid(row =3,columnspan=4,sticky=W+E)
















































































































































































































































eighteen = ttk.Button(root,text = '^',command =lambda:btnPress('**')).grid(row =7,column=3)




























































































'''







































































































































































































































nineteen = ttk.Button(root,text = 'sqrt',command =btnPress('math.sqrt(0)')).grid(row =7,column=3)'''






























































































































equalsbtn = ttk.Button(root,text = '=',command = EqualPress).grid(row =8,columnspan=4,sticky =W+E)



















































































































seventeen = ttk.Button(root,text = 'QUIT',command =root.destroy).grid(row =9,columnspan=4,sticky=W+E)














































































































































































































































































































































































































































































































root.mainloop()
