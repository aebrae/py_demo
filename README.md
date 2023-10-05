# py_demo
Automation scripts to process and then upload new products(text & image files) to an eCommerce website running a Django framework. Image and text files are processed and uploaded separately, using two different REST API endpoints. After upload to webserver is complete, a PDF is automatically generated based on the new text files and another script attaches the PDF and sends an email to the new products supplier as confirmation. health_check.py script automatically sends an email via SMTP if something is wrong with the server after the script is set to a CRON job to execute every 60 seconds.  

Scripts written from scratch by Alex Ebrahim. 
