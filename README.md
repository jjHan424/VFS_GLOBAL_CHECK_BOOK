# VFS_GLOBAL_CHECK_BOOK
A tool for automatically ***CHECK*** available appointments on VFS Global and automatically ***ENTER*** the reservation person’s information 
## BRIEF INTRODUCTION
This code is written in *Python* based on the *selenium*. Its functions can be summarized as:
1. **AUTOMATICALLY** **CHECK** if there is a available appointments
2. If there is a availble appointment, it can **ENTER** the information of the reservation person **IMMEDIATELY**, such as name, gender, date of birth, country and so on.
## UNIQUE FEATURE
1. Support multiple account login settings to prevent account being locked
2. If login fails, you can customize multiple logins
3. Can automatically enter the reservation person information once the available appointments are detected
4. Can monitor multiple **VISA CENTERS** at one time
5. After detecting the available appointment time, it can **send an email** in time
6. All settings are saved locally to **protect your privacy**
## BEFORE USE
***You need basic Python knowledge and the ability to debug code***
## HOW TO USE
1. Set your multiple vfs counts in "config.ini". *(Of course, it’s also possible to have only one account.)*
2. **vfs_country:** this is only available for ITALY and GERMANY in CHINA. If you are in other countries except CHINA, you can enter the web site in Line 106-109 in *vfs_visa_main.py*
3. The settings about email is in the file *vfs_visa_main.py* Lines 28-32. The function about email is based on SMTP
4. There is no need to modify the code in the file *ReadConfig.py*
## LAST
If you have the basic ability to ***debug code***, you can quickly use this code

If you need anything, please contact ***hanjunjie0931@gmail.com***, I will provide help when I am free

**Hope you can get your visa smoothly**
