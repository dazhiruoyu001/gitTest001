import requests,pprint



def login(username,password):
    payload = {
        'username': username,
        'password': password
    }
    # data参数 就是构造消息体的
    response = requests.post("http://localhost/api/mgr/loginReq",
                             data=payload)

    # 获取结果，返回给调用者
    retDict = response.json()
    # 打印出结果
    print(retDict)

    return retDict,response.cookies


def add_course(name,desc,displayidx,sessionid):
    pl = {
        'action': 'add_course',
        'data' : '''
                {
                  "name":"%s",
                  "desc":"%s",
                  "display_idx":"%s"
                }
        ''' %  (name,desc,displayidx)
    }


    reponse = requests.post('http://localhost/api/mgr/sq_mgr/',
                            data=pl,
                            cookies={'sessionid': sessionid})

    retDict = reponse.json()

    print(retDict)
    return retDict


def list_course(sessionid):
    params = {
        'action':'list_course',
        'pagenum':'1',
        'pagesize':20
    }

    response = requests.get("http://localhost/api/mgr/sq_mgr/",                                                 params=params,
                            cookies={'sessionid': sessionid})
    # 获取结果，返回给调用者
    retDict = response.json()
    pprint.pprint(retDict)
    return retDict



def modify_course(courseid,name,desc,displayidx,sessionid):
    pl = {
        'action': 'modify_course',
        'id' : courseid,
        'data' : f'''
                {{
                  "name":"{name}",
                  "desc":"{desc}",
                  "display_idx":"{displayidx}"
                }}
        '''
    }


    reponse = requests.put('http://localhost/api/mgr/sq_mgr/',
                            data=pl,
                            cookies={'sessionid': sessionid})

    retDict = reponse.json()

    print(retDict)
    return retDict


def delete_course(courseid,sessionid):
    payload = {
        'action': 'delete_course',
        'id': f'{courseid}'
    }

    response = requests.delete("http://localhost/api/mgr/sq_mgr/",
                               data=payload,
                                cookies={'sessionid': sessionid})

    r = response.json()
    pprint.pprint(r)
    return r

