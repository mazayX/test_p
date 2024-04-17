from flask import Flask
from flask import request, render_template
app = Flask(__name__)

user_id={'1':{'name':'Мавтей','age':15,'location':'Саратов'},
         '2':{'name':'Колян','age':14,'location':'Москва'},
         '3':{'name':'Юра','age':23,'location':'Саранск'},
         '4':{'name':'Дмитрий','age':44,'location':'Уфа'},
         '5':{'name':'Олег','age':21,'location':'Ялта'}}

@app.route('/')
def index():
 return render_template("put.html" )

@app.route('/information_users')
def information():
  inf=[]
  for i in user_id:
   inf.append(f"User - {i}: name {user_id[i]['name']}, age - {user_id[i]['age']}, location - {user_id[i]['location']}")
  return f"{inf[0]}\t{inf[1]}\t{inf[2]}\t{inf[3]}\t{inf[4]}"

@app.route('/new_user')
def new_user():
 name_new_user=request.args.get('name') #Метод для извлечения парметра
 age_new_user=request.args.get('age')
 location_new_user=request.args.get('location')
 user_id['6']={'name':name_new_user,'age':int(age_new_user),'location':location_new_user}
 return f"name = {name_new_user}; age = {age_new_user}; location = {location_new_user}"

@app.route('/ID')
def ID():
 return user_id


@app.route('/Table')
def Table():
 return render_template("table.html")


 
  
# @app.route('/user/<login>')
# def user(login):
#  if int(login)<101:
#   return f'Здравствуй пользователь N {login}'
#  else:
#   return 'Такого пользователя не существует'
 

if __name__=="__main__":
 app.run()