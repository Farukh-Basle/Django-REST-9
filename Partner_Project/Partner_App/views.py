
from django.shortcuts import render
import requests
from django.http import HttpResponse
import json

def EmployeeListView(request):
    response = requests.get('http://127.0.0.1:1400/api/employees/')

    if response.status_code==200:
        try:
            dict_data = json.loads(response.text)
        except ValueError:
            return HttpResponse('Sorry, You are not getting JSON Response')
        else:
            return HttpResponse(dict_data)
    else:
        print(response.status_code)
        return HttpResponse(response.text)

def EmployeeDetailView(request,pk):
    response = requests.get('http://127.0.0.1:1400/api/employees/'+str(pk)+'/')

    if response.status_code==200:
        try:
            return HttpResponse(response,content_type='application/json')
        except ValueError:
            return HttpResponse('Sorry, You are not getting JSON Response')
    else:
        print(response.status_code)
        return HttpResponse(response.text)

def EmployeeDeleteView(request,pk):
    response = requests.delete('http://127.0.0.1:1400/api/employees/'+str(pk)+'/')

    if response.status_code==204:
        json_data = json.dumps({"message" : "Requested resource deleted successfully."})
        return HttpResponse(json_data,content_type='application/json')

    else:
        print(response.status_code)
        json_data = json.dumps({"message": "Requested resource not available to delete."})
        return HttpResponse(json_data, content_type='application/json')

def EmployeeCreateView(request):
    payload = {
        "eno" : 10,
        "ename" : "Sachin",
        "salary" : 10000
    }
    response = requests.post('http://127.0.0.1:1400/api/employees/', data=payload)

    if response.status_code==201:
        json_data = json.dumps({"message": "Requested resource created successfully."})
        return HttpResponse(json_data, content_type='application/json')
    else:
        json_data = json.dumps({"message": "Requested resource not created."})
        return HttpResponse(json_data, content_type='application/json')

def EmployeeUpdateView(request,pk):
    response = requests.get('http://127.0.0.1:1400/api/employees/'+str(pk)+'/')
    if response.status_code==200:
        payload = {
            "eno": 10,
            "ename": "Master Sachin",
            "salary": 15000
        }
        response = requests.put('http://127.0.0.1:1400/api/employees/'+str(pk)+'/',
                                data=payload)

        if response.status_code==200:
            json_data = json.dumps({"message": "Requested resource updated successfully."})
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = json.dumps({"message": "Requested resource not updated successfully."})
            return HttpResponse(json_data, content_type='application/json')
    else:
        json_data = json.dumps({"message": "Requested resource not available to GET."})
        return HttpResponse(json_data, content_type='application/json')



def get_all_employees(request):
    response = requests.get('http://127.0.0.1:1400/api/employees/')

    if response.status_code==200:
        employee_list = json.loads(response.text)
        context = {
            'employee_list' : employee_list
        }
        return render(request, 'get_all_employees.html', context)

    else:
        context = {
            "error" : "Employees data not available to display."
        }
        return render(request, 'get_all_employees.html', context)











