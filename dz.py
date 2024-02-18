from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
        

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def check_if_10(self):
        length=self
        if len(length)!=10:
            raise Exception("Wrong phone number format. Should be 10 digits.")
        else:
            return self
              
class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,item):
        try:
            self.phones.append(str(Phone.check_if_10(item)))
        except Exception as e:
            print(e)
        
    def remove_phone(self,item):
        if item in self.phones:
            self.phones.remove(item)
    
    def edit_phone(self,old,new):
        if old in self.phones:
            self.phones.remove(old)
            try:
                self.phones.append(str(Phone.check_if_10(new)))
            except Exception as e:
                print(e)
        
    def find_phone(self,phone):
        if phone in self.phones:
            return f"{self.name}: {phone}"
        else:
            return "Not found"
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict):
    def add_record (self,item):
        self.data[item.name]=item.phones
    
    def find(self,item):
        for i,_ in self.data.items():
            if str(i)==item:
                return self.get(i)
            
    def delete(self,item):
        for i,_ in self.data.items():
            if str(i)==item:
                pass

    
