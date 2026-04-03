grades ={"alice": "A","bob":"B"}
attendance ={"alice":90,"bob":85}

grades["bob"] = "A"
attendance["bob"] = 88

grades["charlie"] = "C'
attendance["charlie"] = 80

grades.pop("alice")
attendance.pop("alice")

for student in grades:
  print(student,"-grade", grades[student],"attendance:",attendance[student])
  
