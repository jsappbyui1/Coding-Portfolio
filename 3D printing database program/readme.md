# Overview

I designed this software to be a tool to me in my personal work as a commission 3D model printer and painter.  It is designed to keep track of model components, print-times, and other important details so that I can do my work more efficiently.  

[Software Demo Video](https://youtu.be/Tu5giRjTywg)

# Relational Database

For this database I built out a local SQL database that is managed through MySQL Workbench.  Most of the database is centered around two tables, projects and Models, with other tables attached to enable functionality in the program such as calculating the total print time for a model given a parts list with attached print times.  

# Development Environment

This software was designed using VScode 2019 edition in python 3.9.7.  

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [W3 Schools tutorial for Python-SQL intergration](https://www.w3schools.com/python/python_mysql_getstarted.asp)


# Future Work

* GUI - The goal of this project was to simplify it so that you can add a model at the push of a button.  This version does not have that capability yet.
* Project Management - While you can create a project using the current code, using the information that entry provides is relatively difficult at this time.