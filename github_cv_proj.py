# cv_builder

print ("____YOUR PERFECT CV_____")

name = input("Name:")
gpa = input("GPA:")


education = {}
has_edu = True

while has_edu is True:
    school = input("Enter the schools you have gone to(or press Enter to FINISH):")

    if school == "":
        has_edu = False
    else:
        grad_year = input("When did you graduate from the school:")

        education[school] = grad_year


skills = []
has_skills = True

while has_skills is True:
    new_skill = input("Enter a skill( or press ENTER to FINISH)")

    if new_skill == "":
        has_skills = False
    else:
        skills.append(new_skill)

check = open(name , "w")
check.write("___Your Perfect CV____\n")
check.write("Name:" + name + "\n")
check.write("GPA:" + gpa + "\n")

check.write("\nEDUCATION:\n")
for school_name in education:
    year = education[school_name]
    check.write("- " + school_name + ": " + year + "\n")

check.write("\nSKILLS:\n")
for s in skills:
    check.write("- " + s + "\n")
check.close()
