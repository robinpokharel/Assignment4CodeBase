# app.py

from flask import Flask, jsonify, make_response
import json
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Default Home Page'


def getInetAddress(line):
    items = line.split("inet addr:")
    if len(items) > 1:
        return items[1].split()[0]

    return None

def getInetName(i):
    items = i.split("Link")
    if len(items) > 0:
        return items[0].strip()

    return None

@app.route('/iproutes')
def iproutes():
    return 'ip routes'


@app.route('/interfaces')
def interfaces():

    interfaceList=[]
    ipAddressList=[]
    res={}
    d={}
    with open('interfaces.txt','r') as f:
        lines = f.readlines()
        try:
            for i in lines:
                if len(i) > 0:
                    interfaceName = getInetName(i)
                    ipAddress = getInetAddress(i)
                    if   all  ( [ipAddress, interfaceName]) :
                        ipAddressList.append(ipAddress)
                        interfaceList.append(interfaceName)

            d["ComputerInterfaces"] = dict ( zip(interfaceList, ipAddressList) )

            res = make_response(jsonify(d), 200)
            return res

        except Exception as err:
            print("Unexpected {}".format(err))

    return res


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

