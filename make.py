"""
write the Python code to make a Actually make multiple files which which will contain the. Practical content which have to be done in the files. As per the specified file. For example, there are 12 practicals and I am providing a string which contains the objective slash M of all the practicals. Now we have to write each practical in each file. 4 letter reference.

"""

# Importing the required modules
import os
import re


practicals = """1. Write HTML/Java scripts to display your CV in navigator, your Institute website, Department Website and Tutorial website for specific subject
2. Write an HTML program to design an entry form of student details and send it to store at database server like SQL, Oracle or MS Access.
3. Write programs using Java script for Web Page to display browsers information.
5. Write a Java applet to display the Application Program screen i.e. calculator and other.
6. Writing program in XML for creation of DTD, which specifies set of rules. Create a style sheet in CSS/ XSL & display the document in internet explorer.
7. Program to illustrate JDBC connectivity. Program for maintaining database by sending queries. Design and implement a simple servlet book query with the help of JDBC & SQL. Create MS Access Database, Create on ODBC link,Compile & execute JAVA JDVC Socket.
8. Install TOMCAT web server and APACHE. Access the above developed static web pages for books web site, using these servers by putting the web pages developed.
9. Assume four users user1, user2, user3 and user4 having the passwords pwd1, pwd2, pwd3 and pwd4 respectively. Write a servlet for doing the following. Create a Cookie and add these four user id’s and passwords to this Cookie. 2. Read the user id and passwords entered in the Login form and authenticate with the values available in the cookies.
10. Install a database (Mysql or Oracle). Create a table which should contain at least the following fields: name, password, email-id, phone number Write a java program/servlet/JSP to connect to that database and extract data from the tables and display them. Insert the details of the users who register with the web site, whenever a new user clicks the submit button in the registration page.
11. Write a JSP which insert the details of the 3 or 4 users who register with the web site by using registration form. Authenticate the user when he submits the login form using the user name and password from the database
12. Design and implement a simple shopping cart example with session tracking API."""

# Creating a list of practicals
practicals = practicals.split("\n")

# Creating a list of practicals by removing the starting serial numbers
practicals = [re.sub(r"\d+\.\s", "", practical) for practical in practicals]

# stripping the practicals
practicals = [practical.strip() for practical in practicals]
i= 1
for practical in practicals:
    print(practical)
    # creating a file with the practical number
    with open(f"{i}.html", "w") as file:
        file.write(f"""<!DOCTYPE html>
        <html>
        <head>
        <title>{practical}</title>""")
    i += 1
