from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from datetime import date


#formの内容をDBに追加する処理
@login_required
def index(request):
    #form送信されたかをチェック
    if request.method == "POST":
        #ブラウザから送られてきたデータを取り出す。request.POST[”○○”]
        title = request.POST["title"]
        reason = request.POST["reason"]
        due_date = request.POST.get("due_date") or None
        #DBに保存
        Task.objects.create(
            title=title,
            reason=reason,
            due_date=due_date,
            user=request.user,
            )
        return redirect('/ToDo/')
    
    today = date.today()
    
    incomplete_tasks = Task.objects.filter(user=request.user, done=False).order_by("due_date")
    complete_tasks = Task.objects.filter(user=request.user, done=True).order_by("due_date")
    
    for task in incomplete_tasks:
        if task.due_date:
            task.days_left = (task.due_date - today).days
            task.days_left_abs = abs(task.days_left)
        else:
            task.days_left = None
            task.days_left_abs = None
    
    for task in complete_tasks:
        if task.due_date:
            task.days_left = (task.due_date - today).days
        else:
            task.days_left = None
    
    
    return render(request, "ToDo/index.html", {
    "incomplete_tasks": incomplete_tasks,
    "complete_tasks": complete_tasks,
    "today": date.today(),
    "today": today
    })

def done(request, task_id):
    #()の中を取得
    task = Task.objects.get(id=task_id)
    
    task.done = not task.done
    #saveでDBを更新
    task.save()
    #一覧に戻る
    return redirect('/ToDo/')

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/ToDo/')

@login_required
def edit(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == "POST":

        title = request.POST["title"]
        reason = request.POST["reason"]

        task.title = title
        task.reason = reason

        task.save()

        return redirect('/ToDo/')
    else:
        return render(request, "ToDo/edit.html", {"task": task})
    

