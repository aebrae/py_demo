#!/usr/bin/env python3
"""Creates a PDF based on the text files sent by the supplier and 
then sends an email to the supplier indicating they were processed via PDF attachemnt"""
import os
import reports
import emails

from datetime import datetime
now = datetime.now()
date_text = now.strftime("%B %d, %Y")
#print(date_text) # August 15, 2023

source_path = "/supplier_data/descriptions/"
dest_path = "/home/aebrae/processed.pdf"
table_data = []
for file_name in os.listdir(source_path):   #pre-pocesses the text files to add the data to a table object
                if file_name.endswith('txt'):
                        with open(source_path+file_name, "r") as file:
                                temp_list = []
                                temp_name = "name: "+file.readline()
                                temp_name += "weight: "+file.readline().strip()
                                temp_list = [temp_name]
                                #print(temp_list)
                                table_data.append(temp_list)


if __name__ == "__main__":
        title = "Processed Update on " + date_text
        reports.generate_report(dest_path, title, table_data) #report is generated as a PDF file with processed data from the above section

        From, To, = "sender@gmail.com", "recipient@gmail.com"
        subject_line = "Upload Completed - Online Fruit Store"
        body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
        emails.send_email(emails.generate_email(From,To,subject_line,dest_path)  #sends a pre-filled email with the newly generated PDF as an email attachment 
