# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 12:54:38 2022

@author: dell
"""

import streamlit as st
import pandas as pd
import pickle
# DB Management

st.header("Hii!welcome to PreFree App!")
st.image("https://th.bing.com/th/id/OIP.SRhgcQZRJkST6QvCoSFFIgHaGE?w=218&h=180&c=7&r=0&o=5&dpr=1.7&pid=1.7")


import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Simple Login App"""
    
	st.title("Patient Login page")
    
    
    
    
    
    
	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		st.subheader("Login Section")
        

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				task = st.selectbox("Task",["As Admin"," As Patient_login","Database"])
				if task == "As Admin":
					st.subheader("Add Admin information") 
                   

				elif task == " As Patient_login":
					st.subheader("Patient login")
					loaded_model=pickle.load(open('C:/Users/shubhangi vajpai/OneDrive/Desktop/predicting health risks/trained_model1.sav','rb'))


                # creating a function for Prediction

					def health_risks_prediction(inpArray):
						#print("---------------------------------")
						#print("       DecisionTreeClassifier")
					# print("Level of Risk:1-3   low->1,high->3")
						#print("__________________________________")
						inpFrame=['Enter Age of Patient:','Enter systolic Blood Pressure of Patient:','Enter Diastolic Blood Pressuree of Patient:','Enter Blood Glucose Level of Patient:','Enter Body Temperarature of  Patient:','Enter Heart Rateof Patient:',]
						inpArray=list()
						for i in  range(6):
							temp=input(inpFrame[i])
							inpArray.append(float(temp))

						patientPredict=loaded_model.predict([inpArray])
						#print("________________________________________")
						return ("Risk Level of patient is:",patientPredict[0])
						#print('-----------------------------------------')

					def main():
						
						
						#giving a title
						st.title('Predicting Health Risks for Pregnant Patients Web App')
						
						
						# getting the input data from the user
						
						Age=st.text_input('Age of the Patient')
						SystolicBP=st.text_input('Systolic BP of Patient')
						DiastolicBP=st.text_input('Diastolic BP of the Patient')
						BS=st.text_input('Blood glucose Levels of the Patient')
						BodyTemp=st.text_input('Body Temp of the Patient')
						HeartRate=st.text_input('Heart Rate of the Patient')
						
						# code for Prediction
						
						diagnosis=''
						
						# creating a button for Prediction
						if st.button('Health Risks test Result'):
							diagnosis=health_risks_prediction([Age,SystolicBP,DiastolicBP,BS, BodyTemp,HeartRate])
						st.success(diagnosis)
						
					if __name__=='__main__':
						main()
        

				elif task == "Database":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
    main()