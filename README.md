# Cbot -
In order to spread awareness among the citizens on the novel coronavirus outbreak in India, 3 LPU students has made a webapp that will help people to track Covid-19 infections more accurately and effectively. The 'C-BOT' webapp, which is currently available on localhost, keep the user updated about number of case rising in India every day.C-BOT has a user friendly interface and one just has to simply register/signup to the webapp for its use. The webapp is easy accessible and can be accessed almost anywhere, or from any device. Every person who use the C-Bot will be helping in the fight against coronavirus (COVID-19). The webapp will help the user understand where and how quickly the virus is spreading, so it can respond quickly and effectively. Besides this, the webapp also has a dedicated chatbot that gives you a series of options to determine if you have any symptoms of Covid-19 as well as inform you about the various facilities and updates from the health ministry along with a series of helpline numbers nationally. The webapp also provides you with the best hospitals options nearby your state. With the launch of this webapp, our objective seeks to limit the spread of the Covid-19 cases in India as well as help to create self-awareness among the citizens with relevant information on the infection.

To use, just install Virtual Environment, Go to CMD
use command pip install virtualenv
pip install virtualenvwrapper-win
then
CD to your project directory and type
mkvirtualenv myenv
pip install -r requirements.txt
After that, Download Postgresql 12 software
Open Pgadmin use password - kt6uqn0kss while installing 
then open pgadmin with the same password and create a database named cbot
then just go back to CMD and type
python manage.py migrate
After that
python manage.py makemigrations
after that type
python manage.py runserver
Now your server is Running!
Go to browser Open 127.0.0.1:8000 to run the file!

Google Drive Link for Video Explanations --- 
https://drive.google.com/drive/folders/1i1Jncux6tmEAK6IRj4tKUECgb-xOxU6r?usp=sharing

