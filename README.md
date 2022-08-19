# Advanced-Keylogger
A Advanced Keylogger based on the keylogger I already made with added functionality

## Functionalties Added
- Added Email Functionality


### Email Functionality
- Made using **MIME** library where we basically use **MIMEMultiPart** to first attach from , to , subject and body to the object then after doing so use **MIMEBase** to attach the attachehment after opening the attachment as read binary.
- After this is done we create a **SMTP** seesion and login using tls and once done send a mail using fromaddr, toaddr, text
- For now this is triggered after we press the **Key.esc** or escape key
