class Mail:

    def __init__(self,email):
        self.email=email

    def is_valid(self):
        if '@' in self.email:
            parts = self.email.split('@')
            if len(parts) == 2:
                if '.' in parts[1]:
                    return True
        return False

    def get_domain(self):
        if self.is_valid():
            domain=self.email.split('@')
            return domain[1]

        else:
            return None
    
#if __name__=="__main__":

email=Mail("123@gmail.com")
print(email.is_valid())
print(email.get_domain())


    
    
    