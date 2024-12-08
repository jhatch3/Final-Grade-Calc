import streamlit as st

gradeTarget = None
finalWorth = None


#   TL/DR
#   Inspiration from https://www.rapidtables.com/calc/grade/final-grade-calculator.html. 
#   Wanted to clone it, but make it look better. As well, used this to learn streamlit and 
#   basic write, header, input functions. 
    


def gradeCalc(current, target, worth):
    """ 
    Function to calculate needed score on final to get target 

    See more:
    https://www.rapidtables.com/calc/grade/final-grade-calculator.html 
    """

    # Convert perecent into decimal
    current = current / 100
    target = target / 100
    worth = worth / 100
    
    # Calculate grade needed return it as a perecnt rounded to 2 decimal places
    top = target - (1 - worth) * current
    bottom = worth

    # return it as a perecnt rounded to 2 decimal places
    grade = (top / bottom) * 100
    return round(grade, 2)


st.title('Final grade')
while True: 
    # Get valid current grade input
    st.header("Enter Current Grade (%)")
    currentGrade = st.number_input("Current ", format="%0.1f")
    if currentGrade > 100.0 or currentGrade < 0.0:
        st.write("Input a valid percent")
    
    else:
        break

# Get valid final worth input
if currentGrade != 0.0:
    st.header("What is your Final Worth (%)")
    finalWorth = st.number_input("Worth", format="%0.1f")

# Get valid target grade input
if finalWorth != None and finalWorth != 0.0:
    st.header("What is your Target Grade (%)")
    gradeTarget = st.number_input("Target", format = "%0.1f") 

# Take inputs and plug into calculator, then print results
if gradeTarget != None and gradeTarget != 0.0:
    st.header(f"Grade Needed on Final to get {gradeTarget}%")
    gradeNeed = gradeCalc(currentGrade, gradeTarget, finalWorth)
    st.write(f"% {gradeNeed}")
