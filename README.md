# simple-library

**This django web app project is an online booking library where you can :**

* Search and explore books .
* Reserve any copy if avaiable .
* Search authors ,and scan info about their lives.
* Basic login/signup features .
<br/>
<br/>
**In order to use this django web app :**

1. First of all **clone or download** this github repository. And change your direcroy to the installed project.
2. **make virual environment** , to make sure the installation you are going to make
in the next steps won't affect existing libraries and so your own projects .
     * Make sure you have **virtualenv** installed to your machine , if not you can install it by:
        python3 -m pip install --user virtualenv
     * Make sure you have **virtualenvwrapper** , if not ! , you can install it by :
        pip install virtualenvwrapper (some extra steps may be required you can follow this documentation :
        (https://virtualenvwrapper.readthedocs.io/en/latest/)
     **NOW** you can make your virtual environment :
     * mkvirtualenv env1
     * And to start working on this freshly new environment type : workon env1
3. Install **python3.7.2** from this link (https://www.python.org/downloads/release/python-372/) .
4. Install **postgresql** from this link (https://www.postgresql.org/download/)
5. Install **requiremnts file** using the command :
    pip install -r requirements.txt
<br/>
<br/>
**CONGRATS ! We Are done now from setting up our environment , LET'S DIG IN !**
<br/>
<br/>
**To run our simple-library web app :**
1. **Setup database** with postgresql .
2. **Export environment veriables** which they are basically (SECRET_KEY, WSGI_APPLICATION, DATABASE_URL, SENDGRID_API_KEY
                                                          EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, AWS_ACCESS_KEY_ID
                                                          AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, CacheControl)
3. **Make sure you still exist in the base project directory** , then type :
     python3 manage.py migrate (this command will build up database tables for you)

4. **And finally** ! to run it type :
     python3 manage.py runserver
     **jump to any web browser and surf this web app !**
<br/>
<br/>
Don't hesitate and contact me if you encounterd any problem !
