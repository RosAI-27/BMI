import streamlit as st 

st.title("BMI Calculator")

weight  = st.number_input("Enter your weight in Kgs")
status = st.ratio("Select your height format:", ("cms", "meters", "foot"))

try: 
    if status == "cms":
        height = st.number_input('Centimeters')
        bmi = weight/((height/100)**2)


    elif status == 'meter':
        height = st.number_input('meters')
        bmi = weight/((height)**2)
    elif status == 'foot':
        height = st.number_input('foot')
        bmi = weight/((height)/3.28)**2
except:
    print('Zero division error')
    
if (st.button("Calculate BMI")):
    st.write(f'Your BMI index is {round(bmi)}')
    
    if bmi < 18.5:
        st.warning('You are underweight')
    elif (bmi>=18.5 and bmi<=24.9):
        st.success('You are Healthy')
    elif (bmi>24.9 and bmi<=29.9):
        st.error("You are overweight")
    elif (bmi>=30):
        st.warning('You are extremely overweight')
        