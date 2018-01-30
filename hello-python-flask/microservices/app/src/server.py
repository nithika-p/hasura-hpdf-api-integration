from flask import Flask,render_template,request,redirect,send_file
import requests,json,wit,sys,ast
from .Object_response_class import Response_object
client = wit.Wit('ROMP5H3YEJBXQ76GNQHQYG4VHD2YGJ2D')

Client_msgs = []
Wit_Responses = []

cnt = 0

app = Flask(__name__)

@app.route("/")
def fInput():
	return render_template('sam.html')

@app.route("/",methods=['POST','GET'])
def fProcess():
	print(request.is_json)

	if request.method == "POST":
		global cnt
		Client_msgs.append(request.json.get('text'))	#getting json formatted text from frontend
		client_query = Client_msgs[cnt]	#for future use

		cnt+=1

		received_response = client.message(client_query)	#sending the client_query to wit app


		# Current_wit_Response = []	
		flag=0

		Object_list = []
		jSon_String =" "
		if len(received_response['entities'])!=0:
			flag=1
			for i in range(len(received_response['entities'])):
				entity=None
				value=None
				try:
					entity = list(received_response['entities'])[i]
					value = received_response['entities'][entity][0]['value']
				except:
					pass
				temp_object = Response_object(entity,value)
				Object_list.append(temp_object)
				# Wit_Responses.append([entity,value])
				# Current_wit_Response.append([entity,value])
		else:
			Current_wit_Response.append("Sorry wit could not understand what you just said!")
		if flag==1:
			jSon_String=json.dumps([e.toJson() for e in Object_list])
			return jSon_String
		else:
			return jsonify(jSon_String="Sorry wit could not understand what you just said!")
		# print(jsonify(Current_wit_Response))
		#return render_template('sam.html',my_list = Current_wit_Response)


if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)