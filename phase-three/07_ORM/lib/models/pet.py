from models.__init__ import CURSOR, CONN


class Pet:

    def __init__(self, name="Pet", age=0, breed='Unknown', owner_id=None, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.breed = breed
        self.owner_id = owner_id
        
    def save(self):
        sql = """
            INSERT INTO pets(name,age,breed,owner_id)
            VALUES (?,?,?,?)
        """
        CURSOR.execute(sql, (self.name,self.age,self.breed,self.owner_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                breed TEXT,
                owner_id INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS pets;"
        CURSOR.execute(sql)
        CONN.commit()

    @property
    def owner(self):
        from models.owner import Owner
        return Owner.find_by_id(self.owner_id)
    
    def update(self):
        sql ="""
            UPDATE pets
            SET name=?, 
            age=?,
            breed=?,
            owner_id=?
            WHERE id=?;
        """
        CURSOR.execute(sql, (self.name,self.age,self.breed,self.owner_id,self.id))
        CONN.commit()

    def delete(self):
        if not self.id:
            print('no id')
            return None
        
        sql="""
            DELETE FROM pets
            WHERE id=?;
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        print('successfully deleted from db')
        self.id = None
        

    @classmethod
    def create(cls, name, age, breed, owner_id):
        # this creates a new instance and kicks off the __init__
        new_pet = cls(name=name, age=age, breed=breed, owner_id=owner_id)
        new_pet.save()
        return new_pet

    def __repr__(self):
        return f'<Pet name={self.name} owner_id={self.owner_id}>'
    
    @classmethod
    def create_instance(cls, row):
        return cls(id=row[0], name=row[1], age=row[2], breed = row[3], owner_id=row[4])
    
    @classmethod
    def find_by_id(cls, id):
        sql="""
        SELECT * FROM pets
        WHERE id=?;
        """
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.create_instance(row)