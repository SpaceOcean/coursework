from django.shortcuts import render, HttpResponse
import json

def mainpage(request):
    database = open('database.json')
    db = database.read()
    database.close()
    db_json = json.loads(db)
    return render(request, 'filmlist/filmlist.html', {'films': db_json})

def filmpage(request, film_id):
    database = open('database.json')
    db = database.read()
    database.close()
    db_json = json.loads(db)
    for i in db_json:
        if i["id"]==film_id:
            return render(request, 'filmlist/film.html/', {'movie': i, 'films': db_json})
def addnew(request):
    if request.POST:
        database = open('database.json')
        db = database.read()
        database.close()
        db_json = json.loads(db)
        film_id = db_json[-1]["id"] + 1
        new_film = {
            "id": film_id,
            "title": request.POST.get("title"),
            "img_url": request.POST.get("img_url"),
            "video": request.POST.get("video"),
            "country": request.POST.get("country"),
            "genre": request.POST.get("genre"),
            "director": request.POST.get("director"),
            "actors": request.POST.get("actors"),
            "description": request.POST.get("description"),
            "pegi": request.POST.get("pegi"),
            "duration": request.POST.get("duration")
        }
        db_json.append(new_film)
        database = open('database.json', 'w').write(json.dumps(db_json))
    return render(request, 'admin/admin.html')

def login(request):
    data = open('users.json').read()
    data = json.loads(data)
    if request.POST:
        for i in data:
            if i['login'] == request.POST.get('username') and i['password'] == request.POST.get('password'):
                database = open('database.json')
                db = database.read()
                database.close()
                db_json = json.loads(db)
                return render(request, 'admin/admin.html')
            else:
                return render(request, 'admin/error.html')
    return render(request, 'admin/login.html')
