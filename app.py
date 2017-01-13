from flask import Flask, request, jsonify, render_template, send_from_directory
from sqlalchemy import create_engine
from boto import ec2

app = Flask(__name__)

e = create_engine('sqlite:///data.db')

@app.route('/', methods=['GET'])
def template():
    return render_template('index.html')


@app.route('/list', methods=['GET'])
def index():
    connDB = e.connect()
    result = e.execute("SELECT * FROM instances")
    lres = []
    for r in result:
        i = {}
        i['instance_id'] = r[0]
        i['public_dns_name'] = r[1]
        i['ip_address'] = r[2]
        i['instance_type'] = r[3]
        i['state'] = r[4]
        i['placement'] = r[5]
        lres.append(i)

    return jsonify(lres)

@app.route('/add', methods=['POST'])
def add():
    accessKeyId = request.json['accessKeyId']
    secretAccessKey = request.json['secretAccessKey']
    region = request.json['region']
    
    connAWS = ec2.connect_to_region(region,aws_access_key_id=accessKeyId, aws_secret_access_key=secretAccessKey)
    connDB = e.connect()

    rs = connAWS.get_all_instances()
    
    for r in rs:
        for i in r.instances:
            query = e.execute("INSERT INTO instances VALUES ('"+ i.id +"','"+ i.public_dns_name +"','"+ i.ip_address +"','"+ i.instance_type +"','"+ i.state +"', '"+ i.placement +"')")
    return jsonify({"result": "ok"})

if __name__ == "__main__":
    app.run(debug=True)