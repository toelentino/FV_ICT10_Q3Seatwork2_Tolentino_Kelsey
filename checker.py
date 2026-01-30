from pyscript import document

def check_team(event):
    # For selected values:
    # this is for the registration status yes or no
    registration = document.querySelector('input[name="registration"]:checked').value
    # this is for the medical clearance status yes or no
    medical = document.querySelector('input[name="medical"]:checked').value
    # this is for the selected grade level of the user
    grade_level = document.querySelector('select[name="grade_level"]').value
        # this is for the selected section of the user
    section = document.querySelector('select[name="section"]').value

    result_div = document.getElementById("result")

    if registration == "yes":# must be registered
        if medical == "yes":# must have medical clearance
            if grade_level in ["7", "8", "9", "10"]:
                # These are my nested conditions for the grade level, teams, and sections
                if grade_level == "7":
                    if section == "Emerald":
                        team = "Blue Bears"
                    elif section == "Ruby":
                        team = "Red Bulldogs"
                    elif section == "Sapphire":
                        team = "Yellow Tigers"
                    elif section == "Topaz":
                        team = "Green Hornets"
                    elif section == "Jade":
                        team = "Green Hornets"
                elif grade_level == "8":
                    if section == "Emerald":
                        team = "Yellow Tigers"
                    elif section == "Ruby":
                        team = "Blue Bears"
                    elif section == "Sapphire":
                        team = "Green Hornets"
                    elif section == "Topaz":
                        team = "Red Bulldogs"
                    elif section == "Jade":
                        team = "Blue Bears"
                elif grade_level == "9":
                    if section == "Emerald":
                        team = "Green Hornets"
                    elif section == "Ruby":
                        team = "Yellow Tigers"
                    elif section == "Sapphire":
                        team = "Red Bulldogs"
                    elif section == "Topaz":
                        team = "Blue Bears"
                    elif section == "Jade":
                        team = "Blue Bears"
                elif grade_level == "10":
                    if section == "Emerald":
                        team = "Red Bulldogs"
                    elif section == "Ruby":
                        team = "Green Hornets"
                    elif section == "Sapphire":
                        team = "Blue Bears"
                    elif section == "Topaz":
                        team = "Yellow Tigers"
                    elif section == "Jade":
                        team = "Yellow Tigers"

                #for this part, this is where it will indicate if the student is eligible or not. 
                # if all the conditions are met, then the congratualtions message will be shown to the user
                # otherwise, they either have to secure their medical clearance or complete their registration.
                result_div.innerHTML = f"🎉 Congratulations! You are eligible.<br>Your team is: <b>{team}</b>"
            else:
                result_div.innerHTML = "❌ Only Grades 7–10 can join."
        else:
            result_div.innerHTML = "⚠️ Please secure your medical clearance."
    else:
        result_div.innerHTML = "⚠️ Please complete your online registration."