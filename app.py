import streamlit as st
from PIL import Image
import pickle


model = pickle.load(open('model1.pkl', 'rb'))

def run():
    img1 = Image.open('Credit.png')
    img1 = img1.resize((156,145))
    st.image(img1,use_column_width=False)
    st.title("Credit Card Approval Prediction")

    ## Account No
    account_no = st.text_input('Account number')

    ## Full Name
    fn = st.text_input('Full Name')

    ## For gender
    gen_display = ('F','M')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    ## For Own Vehichle
    veh_display = ('N','Y')
    veh_options = list(range(len(veh_display)))
    veh = st.selectbox("Own Vehichle", veh_options, format_func=lambda x: veh_display[x])

    ## For Own Realty
    rea_display = ('N','Y')
    rea_options = list(range(len(rea_display)))
    rea = st.selectbox("Own Property",  rea_options, format_func=lambda x: rea_display[x])

    ## For Children
    chi_display = ('No','One','Two','Three','More than Four')
    chi_options = list(range(len(chi_display)))
    chi = st.selectbox("Children",chi_options, format_func=lambda x: chi_display[x])

     ## Applicant Annual Income
    mon_income = st.number_input("Applicant's Annual Income(₹)",value=0)   

    ## For profession
    prof_display = ('Student','Working','Commercial associate','State servant','Pensioner')
    prof_options = list(range(len(prof_display)))
    prof = st.selectbox("Profession",prof_options, format_func=lambda x: prof_display[x])
   
   ## For Education Type
    ty_edu_display = ('Lower secondary','Academic degree','Secondary / secondary special','Incomplete higher','Higher education')
    ty_edu_options = list(range(len(ty_edu_display)))
    ty_edu = st.selectbox("Education", ty_edu_options, format_func=lambda x:ty_edu_display[x]) 
    
     ## For Marital Status
    marital_Status_display = ('Single / not married','Separated','Widow','Civil marriage','Married')
    marital_Status_options = list(range(len(marital_Status_display)))
    marital_Status = st.selectbox("Marital Status", marital_Status_options, format_func=lambda x:marital_Status_display[x]) 
    
     ## For Housing Type
    ty_hou_display = ('Rented apartment','With parents','Municipal apartment','Office apartment','Co-op apartment','House / apartment')
    ty_hou_options = list(range(len(ty_hou_display)))
    ty_hou = st.selectbox("Housing Type", ty_hou_options, format_func=lambda x:ty_hou_display[x]) 
  
     ## Applicant Age
    age = st.number_input("Applicant's Age",value=0)
    
    ## Applicant Work Experience
    exp = st.number_input("Applicant's Working Experience",value=0)
    
     ## Applicant Family Member
    fm_display = ('One','Two','Three','Four','Five','More than Six')
    fm_options = list(range(len(fm_display)))
    fm = st.selectbox("Applicant Family Members", fm_options, format_func=lambda x:fm_display[x]) 
  

    if st.button("Submit"):
       # fm = 
       # if fm == 0:
      #      fam1_member = 0
     #   if fm == 1:
    #        fam1_member = 1
        features = [[gen,veh,rea,chi,mon_income,prof,ty_edu,marital_Status, ty_hou, age,exp,fm]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.success(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'Congratulations !! you will get the Credit Card from Bank.'
            )
        else:
            st.error(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'According to our Calculations, you will not get the Credit Card from Bank.'
           ) 
           
run()