#%%
import pandas as pd
import tkinter as tk
import mysql.connector



class GUI:
    def __init__(self):
        self.db = Database()
    
    def start(self):
        #window = tk.Tk()    
        #_headder = tk.Label(text="What would you like to do?")
        #b_New_Project = tk.Button(text="New Project",command=self.add_new_project)
        #b_New_Client = tk.Button(text="New Client",command=self.add_new_client)
        #b_New_Model = tk.Button(text="New Model",command=self.add_new_model)
        #b_New_Component = tk.Button(text="New Component",command=self.add_new_component)
        #l_headder.pack()
        #b_New_Project.pack()
        #b_New_Client.pack()
        #b_New_Model.pack()
        #b_New_Component.pack()
        #window.mainloop()   
        pass

    def add_new_project(self):
        new_project_window = tk.Tk()
        l_npw_headder = tk.Label(text="New Project Wizard")

        l_npw_headder.pack()

        new_project_window.mainloop()

    def add_new_model(self):
        pass

    def add_new_client(self):
        pass

    def add_new_component(self):
        pass

class Database:
    
    def __init__(self):
        self.my_database = mysql.connector.connect(
        host="localhost",
        user="demo",
        password="Demo_password",
        database="mydb"
        )
        self.interface = self.my_database.cursor()

    def get_cell_value(self,table,table_ID,entry_id,column_name):
        try:
            self.interface.execute(f"SELECT {column_name} FROM {table} WHERE {table_ID} = {entry_id}")
            data = self.interface.fetchall()
            data = data[0]
            data = data[0]
            return(data)
        except:
            return(None)

    def get_cell_id(self,table,table_ID,column_name,entry_value):
        try:
            self.interface.execute(f"SELECT {table_ID} FROM {table} WHERE {column_name} = '{entry_value}'")
            data = self.interface.fetchall()
            data = data[0]
            data = data[0]
            return(data)
        except:
            return(None)

    def add_model(self,model_name,faction_name,publisher):
        try:
            publisher_id = self.get_cell_id('Publisher','idPublisher','publisher_name',publisher)
            if publisher_id == None:
                #error code for assigning a model a publisher that does not exist
                return(1)
            facton_id = self.get_cell_id('factions','idfactions','faction_name',faction_name)
            if facton_id == None:
                #error code for assigning a model a publisher that does not exist
                return(2)        

            sql = f"INSERT INTO Models (model_name,factions_idfactions,Publisher_idPublisher) VALUES ('{model_name}',{facton_id},{publisher_id})"
            self.interface.execute(sql)
            self.my_database.commit()
            return(0)
        except:
            return("Unknown Error")

    def add_artwork(self,model_name,file_name):
        model_id = self.get_cell_id('Models','idModels',"model_name",model_name)
        if model_id == None:
            #error code for assigning a model a publisher that does not exist
            return(1)

        sql = "INSERT INTO Artwork (Models_idModels,file_name) VALUES (%s,%s)"
        val = (f"{model_id}",f"{file_name}")
        self.interface.execute(sql,val)
        self.my_database.commit()

    def create_project(self,project_name,order_id):
        sql = "INSERT INTO project (project_name,Orders_order_ID) VALUES (%s,%s)"
        val = (f"{project_name}",f"{order_id}")
        self.interface.execute(sql,val)
        self.my_database.commit()

    def add_model_to_project(self,project_name,model_name):
        model_id = self.get_cell_id('Models','idModels',"model_name",model_name)
        if model_id == None:
            #error code for assigning a model a publisher that does not exist
            return(1)
        project_id = self.get_cell_id('Models','idproject',"project_name",project_name)
        if project_id == None:
            #error code for assigning a model a publisher that does not exist
            return(1)

        sql = "INSERT INTO Project_models (Models_idModels,project_idproject) VALUES (%s,%s)"
        val = (f"{model_id}",f"{project_id}")
        self.interface.execute(sql,val)
        self.my_database.commit()

    def add_publisher(self,publisher_name,publisher_site = 'None Given'):
        try:
            sql = "INSERT INTO Publisher (publisher_name,publisher_site) VALUES (%s,%s)"
            val = (f"{publisher_name}",f"{publisher_site}")
            self.interface.execute(sql,val)
            self.my_database.commit()
            return(0)
        except:
            #error code for invalid/duplicate entry
            return(1)

    def add_tag(self,tag_name):
        sql = f"INSERT INTO tags (tag_name) VALUE ('{tag_name}')"
        try:
            self.interface.execute(sql)
            self.my_database.commit()
            return(0)
        except:
            #error for duplicate/invalid entry
            return(1)

    def add_component(self,model_name,component_type,file_type,file_name,component_volume,component_print_time_resin,component_print_time_FDM):
        model_id = self.get_cell_id("Models","idModels","model_name",model_name)
        sql = "INSERT INTO components (component_type,file_type,file_name,Models_idModels,component_volume,component_print_time_resin,component_print_time_FDM) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (component_type,file_type,file_name,model_id,component_volume,component_print_time_resin,component_print_time_FDM)
        self.interface.execute(sql,val)
        self.my_database.commit()

    def add_client(self,client_name,client_contact):
        sql = "INSERT INTO Client (client_name,client_contact) VALUES (%s,%s)"
        val = (f"{client_name}",f"{client_contact}")
        self.interface.execute(sql,val)
        self.my_database.commit()

    def add_faction(self,faction_name):
        sql = f"INSERT INTO factions (faction_name) VALUE ('{faction_name}')"
        try:
            self.interface.execute(sql)
            self.my_database.commit()
            return(0)
        except:
            #error for duplicate/invalid entry
            return(1)        

    def get_model_components(self,model,detail="basic"):
        if detail == "basic":
            self.interface.execute(f"SELECT m.model_name, c.file_name FROM models AS m JOIN components AS c ON c.Models_idModels = m.idModels WHERE m.model_name = '{model}'")
            data = self.interface.fetchall()
            return(data)
        if detail == "advanced":
            self.interface.execute(f"SELECT * FROM models AS m JOIN components AS c ON c.Models_idModels = m.idModels WHERE m.model_name = '{model}'")            
            data = self.interface.fetchall()
            return(data)

main = GUI()
db = Database()
main.start()
print(db.add_model("test 2","test-faction","Unassigned"))

# %%
