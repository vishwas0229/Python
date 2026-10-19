class getInfo:
    def name(self):
        Name = input("Enter Name: ")
        return Name
    
    def dob(self):
        print("Date of Birth")
        self.day = int(input("Day: "))
        self.month = int(input("Month (in numeric): "))
        self.year = int(input("Year: "))
        return f"{self.day}/{self.month}/{self.year}"

    def gender(self):
        while 1:
            Gender = input("Gender (M/F): ")
            if Gender.lower() == 'm':
                return "MALE"
            elif Gender.lower() == 'f':
                return "FEMALE"
            else:
                print("Invalid input.")
                
    
user = getInfo()

info = {
    "Name" : user.name(),
    "Date of Birth" : user.dob(),
    "Gender" : user.gender()
    }

print(info)