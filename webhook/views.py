from django.shortcuts import render
import json
from django.http import HttpResponse
import requests

api_url = "https://garageclub2.eu.teamwork.com/"
username = "twp_dTNCmN8bk2fSi6FanbR7OJT8uqVW_eu"
password = "a"

# Create your views here.


def action(request):
    action = request.GET['action']
    if action == "create":
        plate = request.GET['plate']
        make = request.GET['make']
        model = request.GET['model']

        payload = create_taask(request,plate,make,model)

        return HttpResponse(json.dumps(payload), content_type="application/json")
    
    elif action == "reserved":
        plate = request.GET['plate']
        make = request.GET['make']
        model = request.GET['model']
        payload = reserved(request,plate,make,model)

        return HttpResponse(json.dumps(payload), content_type="application/json")

    elif action == "available":
        plate = request.GET['plate']
        make = request.GET['make']
        model = request.GET['model']
        payload = available(request,plate,make,model)

        return HttpResponse(json.dumps(payload), content_type="application/json")

    elif action == "delivered":
        plate = request.GET['plate']
        payload = delivered(request,plate)

        return HttpResponse(json.dumps(payload), content_type="application/json")

    else:
        payload = {}
        payload['Error'] = "Your action is not correct"
        return HttpResponse(json.dumps(payload), content_type="application/json")

# 1
def create_task(plate,make,model):

    url = api_url+"/tasklists/1713276/tasks.json"
    payload = {  
            "todo-item": {
                "content": plate[1:]+"-"+make+" "+model, 
                "responsible-party-id": "457025",
                } 
            }
    response = requests.post(url, auth=(username, password), data=json.dumps(payload, indent = 3))
    print(response.json(),"*******************************")
    return(response.json())

def create_sub_tak(id,plate,make,model,payload):
    url = api_url+"/tasks/"+id+".json"
    payload = {
        "todo-item": {
            "content": plate[1:]+"-"+make+" "+model,
            "responsible-party-id": "466716",
            "tags": "PT"
        }
    }
    response = requests.post(url, auth=(username, password), data= json.dumps(payload, indent = 4))
    payload['sub-task1-response'] = response.json()

    payload = {
        "todo-item": {
            "content": plate[1:]+"-"+make+" "+model, 
            "responsible-party-id": "452385",
            "tags": "LIMPIEZA"
        }
    }
    response = requests.post(url, auth=(username, password), data= json.dumps(payload, indent = 4))
    payload['sub-task2-response'] = response.json()


    payload = {
        "todo-item": {
            "content": plate[1:]+"-"+make+" "+model, 
            "responsible-party-id": "452387",
            "tags": "Pintura"
        }
    }
    response = requests.post(url, auth=(username, password), data= json.dumps(payload, indent = 4))
    payload['sub-task2-response'] = response.json()

    payload = {
        "todo-item": {
            "content": plate[1:]+"-"+make+" "+model, 
            "responsible-party-id": "466639",
            "tags": "Video"
        }
    }
    response = requests.post(url, auth=(username, password), data= json.dumps(payload, indent = 4))
    payload['sub-task3-response'] = response.json()
    return payload

def create_taask(request,plate,make,model):

    # http://localhost:8000/create-task/E123LEP/AUDI/RS4/

    payload = {}
    payload['plate'] = plate
    payload['make'] = make
    payload['model'] = model

    task_res = create_task(plate,make,model)
    payload['task-response'] = task_res

    payload = create_sub_tak(task_res['id'],plate,make,model,payload)


    return payload

#2
def get_all_tasks_of_project():
    url = api_url+"/projects/446109/tasks.json"
    response = requests.get(url, auth=(username, password))
    return(response.json())

def get_id_of_task_by_plate(temp_all_tasks,plate):

    for t in temp_all_tasks['todo-items']:
        temp_hold = t['content'].split("-")
        print(plate[1:],t['id'],temp_hold[0])
        if plate[1:] == temp_hold[0]:
            return t['id']
    return None

def update_task(task_id):
    url = api_url+"/tasks/"+task_id+".json"
    payload = {  
            "todo-item": { 
                "todo-list-id": "1713321"
                } 
            }
    response = requests.put(url, auth=(username, password), data=json.dumps(payload, indent = 2))

    return(response.json())

def get_sub_task(task_id):
    url = api_url+"/tasks/"+task_id+"/subtasks.json"
    response = requests.get(url, auth=(username, password))
    temp = response.json()
    for sub_t in temp['todo-items']:
        if sub_t['tags'][0]['name'] == "Video":
            return sub_t['id']
    return(None)

def update_sub_task(task_id):
    url = api_url+"/tasks/"+task_id+".json"
    print("Here")
    print(task_id)
    payload = {  
            "todo-item": {
                "completed": True
                } 
            }
    response = requests.put(url, auth=(username, password), data=json.dumps(payload, indent = 2))

    return(response.json())

def delete_sub_task(task_id):
    url = api_url+"/tasks/"+task_id+".json"
    response = requests.delete(url, auth=(username, password))
    print(response.json())

def reserved(request,plate,make,model):

    temp_all_tasks = get_all_tasks_of_project()
    temp_task_id = get_id_of_task_by_plate(temp_all_tasks,plate)

    payload = {}
    payload['Task_id'] = temp_task_id

    if payload['Task_id'] == None:
        payload['status'] = "Not Found"
        task_res = create_task(plate,make,model)
        payload['Task_id'] = task_res['id']

        create_sub_tak(payload['Task_id'],plate,make,model,payload)
       
    payload['Update_Response'] = update_task(str(payload['Task_id']))
    temp_sub_tasks_id = get_sub_task(str(payload['Task_id']))
    print(temp_sub_tasks_id,"*******id")
    if temp_sub_tasks_id != None:
        print(temp_sub_tasks_id,"*******id in")
        payload['sub_tak_Update_Response'] = delete_sub_task(str(temp_sub_tasks_id))
    return payload

#3
def update_task_available(task_id):
    url = api_url+"/tasks/"+task_id+".json"
    payload = {  
            "todo-item": { 
                "todo-list-id": "1713276"
                } 
            }
    response = requests.put(url, auth=(username, password), data=json.dumps(payload, indent = 2))

    return(response.json())

def video_sub_task(id,plate,make,model):
    url = api_url+"/tasks/"+id+".json"
    payload = {
        "todo-item": {
            "content": plate[1:]+"-"+make+" "+model, 
            "responsible-party-id": "466639",
            "tags": "Video"
        }
    }
    response = requests.post(url, auth=(username, password), data= json.dumps(payload, indent = 4))
    payload['sub-task3-response'] = response.json()
    

def available(request,plate,make,model):
    temp_all_tasks = get_all_tasks_of_project()
    temp_task_id = get_id_of_task_by_plate(temp_all_tasks,plate)

    payload = {}
    payload['Task_id'] = temp_task_id

    if payload['Task_id'] == None:
        payload['Error'] = "Plate does not exist" 
    else:  
        payload['Update_Response'] = update_task_available(str(payload['Task_id']))

        payload['sub_tak_Update_Response'] = video_sub_task(str(payload['Task_id']),plate,make,model)
            
    return payload


#4
def delivered(request,plate):
    temp_all_tasks = get_all_tasks_of_project()
    payload = {}
    for t in temp_all_tasks['todo-items']:
        temp = t['content'].split("-")
        if plate[1:] == temp[0]:
            if t['parentTaskId'] == "":
                payload['Task_id'] = t['id']
                if 1682372 == t['todo-list-id']:
                    payload['Update_Response'] = update_task(str(payload['Task_id']))
            else:
                payload['Complete_Response'] = update_sub_task(str(t['id']))
    payload['MAin_task_Complete_Response'] = update_sub_task(str(payload['Task_id']))
    return payload



