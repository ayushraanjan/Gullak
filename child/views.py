from django.shortcuts import render
from parent.models import Task, Approval


def submit(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_img = request.FILES['image']
        task_title = request.POST.get('title')
        task_description = request.POST.get('description')
        task_id = request.POST.get('id')
        Approval.objects.create(parent=request.user, title=task_title, description=task_description, image=uploaded_img)

def submission(request):
    if request.method == 'POST':
        task_id = request.POST.get('Task.id')
        task_to_submit = Task.objects.get(id=task_id)
        task_title = task_to_submit.title
        task_description = task_to_submit.description

        return render(request, 'submission.html', {
            'task_title': task_title,
            'task_description': task_description,
            'task_id': task_id,
        })
        


def dashboard(request):
    tasks_list = Task.objects.all()
    return render (request, 'dashboard.html', {
        'tasks_list':tasks_list,

    })


