print("Enter the marks scored by the students")
written = int(input("Written test = "))
lab = int(input("Lab test = "))
assign = int(input("Assignment = "))

print(f"Grade of the student is {(written*70/100)+(lab*20/100)+(assign*10/100)}")