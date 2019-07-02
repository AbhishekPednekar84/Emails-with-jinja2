# Emails with jinja2

This simple project sends an email using **smtplib**, **web scraping (bs4)** and **jinja2**. The program scrapes the *"Top Picks"* section of [The Statesman](https://www.thestatesman.com/) website, sends the headline, headline url and the image url to the jinja2 html template. Once the template is rendered, it is sent via email using smtplib. 

constants.py outlines the parameters that need to be set in order to send the email. The project uses the Gmail SMTP settings.

**Sample image** -

![sample image](https://github.com/AbhishekPednekar84/Emails-with-jinja2/blob/master/images/Sample-Image.jpg)
