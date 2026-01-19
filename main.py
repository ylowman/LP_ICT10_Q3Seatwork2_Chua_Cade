from pyscript import document, window

def checkTeam():
    result_element = document.querySelector("#result")
    registration = document.querySelector('input[name="registration"]:checked').value if document.querySelector('input[name="registration"]:checked') else None
    medical = document.querySelector('input[name="medical"]:checked').value if document.querySelector('input[name="medical"]:checked') else None
    section = document.querySelector("#section").value
    grade = document.querySelector("#grade").value
    
    # Check eligibility
    if registration != "yes":
        result_element.innerText = "You are not eligible. Please register online first."
        return
    
    if medical != "yes":
        result_element.innerText = "You are not eligible. Please secure medical clearance from the clinic."
        return
    
    if not section or not grade:
        result_element.innerText = "Please select both grade and section."
        return
    
    if section == "Emerald":
        team = "Red Bulldogs"
    elif section == "Ruby":
        team = "Blue Bears"
    elif section == "Sapphire":
        team = "Green Hornets"
    elif section == "Topaz":
        team = "Yellow Tigers"
    else:
        team = "Unknown"
    
    result_element.innerText = f"{grade} {section} - {team}. Congratulations! You are in the {team} team."

window.checkTeam = checkTeam