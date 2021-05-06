# geo-address
geopy - is used to map longitute and latitude of the addrees
openpyxl is used to write data to excel.
1.geoenv is the virtual environment. 
activate virtual env using the following command
    source geoenv/bin/activate
2. Make sure u have python3.8 installed in your system
3.install the requirements using pip install -r requirement.txt 
4.do migrations using the following command.
    python3 manage.py makemigrations
    python3 manage.py migrate
5 Run the project using this command.
    python3 manage.py runserver
6. go to url 127.0.0.1:8000
7. upload user.xlsx file by downloading in your system and click on submit button which shows up longitude and latitue of the address in excel file.
8. New file generated is address.xlsx which will be in your project folder. 
