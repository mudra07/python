cet={"alice","bob"}
jee={"bob","eve"}
neet={"alice","eve"}
print("all students:",cet|jee|neet)
print("students in all exams:",cet&jee&neet)
print("CET but not JEE:",cet-jee)
