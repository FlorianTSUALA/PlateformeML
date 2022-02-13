
class Employee(db.Document):
name = db.StringField()
email = db.StringField()
phone = db.StringField()
pub_date = db.DateTimeField(datetime.now)
 
@app.route('/')
def query_records():
employee = Employee.objects.all()
return render_template('useradmin.html', employee=employee)

@app.route('/updateemployee', methods=['POST'])
def updateemployee():
pk = request.form['pk']
namepost = request.form['name']
value = request.form['value']
employee_rs = Employee.objects(id=pk).first()
if not employee_rs:
    return json.dumps({'error':'data not found'})
else:
    if namepost == 'name':
        employee_rs.update(name=value)
    elif namepost == 'email':
        employee_rs.update(email=value)
    elif namepost == 'phone':
        employee_rs.update(phone=value)
return json.dumps({'status':'OK'})
 
@app.route('/add', methods=['GET', 'POST'])
def create_record():
txtname = request.form['txtname']
txtemail = request.form['txtemail']
txtphone = request.form['txtphone']
employeesave = Employee(name=txtname, email=txtemail, phone=txtphone)
employeesave.save()
return redirect('/')

@app.route('/delete/<string:getid>', methods = ['POST','GET'])
def delete_employee(getid):
print(getid)
employeers = Employee.objects(id=getid).first()
if not employeers:
    return jsonify({'error': 'data not found'})
else:
    employeers.delete() 
return redirect('/')