#easyOCR project by Arush James

import easyocr
import os
import streamlit as st 
import mysql.connector
st.title("Extracting text from image using EasyOCR")
path = st.text_input("")
if path =="": 
    st.markdown("#### :orange[Enter a file path]")
elif os.path.exists(path) == True:
    reader=easyocr.Reader(['en'])
    results = reader.readtext(path,detail=0)
    def convert(list):
        return (*list, )
    st.write(results)
    db = mysql.connector.connect(  
    host="localhost",
    username="root",
    password="",
    database="project"
    )
    
    if len(results)==8:
        mycursor=db.cursor()
        mycursor.execute("INSERT INTO prj1(Info1,Info2,Info3,Info4,Info5,Info6,Info7,Info8,Info9,Info10,Info11,Info12,Info13,Info14,Info15) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,null,null,null,null,null,null,null)", (results))
        db.commit()
        st.markdown("##### :green[Success!! The extracted text has been stored in a database]")
    elif len(results)==9:
        mycursor=db.cursor()
        mycursor.execute("INSERT INTO prj1(Info1,Info2,Info3,Info4,Info5,Info6,Info7,Info8,Info9,Info10,Info11,Info12,Info13,Info14,Info15) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,null,null,null,null,null,null)", (results))
        db.commit()
        st.markdown("##### :green[Success!! The extracted text has been stored in a database]")
    elif len(results)==10:
        mycursor=db.cursor()
        mycursor.execute("INSERT INTO prj1(Info1,Info2,Info3,Info4,Info5,Info6,Info7,Info8,Info9,Info10,Info11,Info12,Info13,Info14,Info15) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,null,null,null,null,null)", (results))
        db.commit()
        st.markdown("##### :green[Success!! The extracted text has been stored in a database]")
    elif len(results)==11:
        mycursor=db.cursor()
        mycursor.execute("INSERT INTO prj1(Info1,Info2,Info3,Info4,Info5,Info6,Info7,Info8,Info9,Info10,Info11,Info12,Info13,Info14,Info15) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,null,null,null,null)", (results))
        db.commit()
        st.markdown("##### :green[Success!! The extracted text has been stored in a database]")
    elif len(results)==12:
        mycursor=db.cursor()
        mycursor.execute("INSERT INTO prj1(Info1,Info2,Info3,Info4,Info5,Info6,Info7,Info8,Info9,Info10,Info11,Info12,Info13,Info14,Info15) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,null,null,null)", (results))
        db.commit()
        st.markdown("##### :green[Success!! The extracted text has been stored in a database]")
    elif len(results)==13:
        mycursor=db.cursor()
        mycursor.execute("INSERT INTO prj1(Info1,Info2,Info3,Info4,Info5,Info6,Info7,Info8,Info9,Info10,Info11,Info12,Info13,Info14,Info15) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,null,null)", (results))
        db.commit()
        st.markdown("##### :green[Success!! The extracted text has been stored in a database]")
    elif len(results)==14:
        mycursor=db.cursor()
        mycursor.execute("INSERT INTO prj1(Info1,Info2,Info3,Info4,Info5,Info6,Info7,Info8,Info9,Info10,Info11,Info12,Info13,Info14,Info15) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,null)", (results))
        db.commit()
        st.markdown("##### :green[Success!! The extracted text has been stored in a database]")
    elif len(results)==15:
        mycursor=db.cursor()
        mycursor.execute("INSERT INTO prj1(Info1,Info2,Info3,Info4,Info5,Info6,Info7,Info8,Info9,Info10,Info11,Info12,Info13,Info14,Info15) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (results))
        db.commit()
        st.markdown("##### :green[Success!! The extracted text has been stored in a database]")
    
else:
    st.markdown("#### :red[Incorrect path or file does not exist]")
