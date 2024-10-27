from flask import Flask,request,jsonify
app = Flask(__name__)
task =[{
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, Cheese, Pizza, Fruit",
        "done": False
       },
       {
         "id": 2,
         "title": "Learn Python",
         "description": "Need to find a good Python tutorial on the web",
          "done": False
        }
]
@app.route('/task/<task_id>',methods=['GET'])
def get_task(id):
   return task[int(id)]
if __name__ == '__main__':
   app.run(debug=True)