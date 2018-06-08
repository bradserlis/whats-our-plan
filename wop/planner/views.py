from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, GroupCreate, ActivityCreate
from .models import Group, Profile, Activity, User_Group
from wop.planner.forms import SignUpForm
from django.template import loader
from django.urls import reverse_lazy
import random


# Create your views here.

def index(request):
    return render(request, 'index.html', {'user_loggedin': not request.user.is_anonymous})


def profile(request):
    user = Profile.objects.get(user=request.user)
    groups = Group.objects.filter(users=user)
    activities = Activity.objects.filter(group__in=groups)
    print(activities)
    return render(request, 'profile.html', {'groups':groups, 'activities': activities })

# ===
# Activity
# ===

def get_random_activity(request, pk):
    reset_pool= None
    print('pk is', pk)
    group = Group.objects.get(id=pk)
    print('group is', group)
    pool = Activity.objects.filter(group_id=group).values().exclude(is_chosen=True)
    try: 
        reset_pool = Activity.objects.get(group_id=group, is_chosen=True)
        print('it passed')
    except:
        pass
        print('except')

    # print('pool looks like this:', pool.count())
    # print('reset_pool looks like this:', type(reset_pool))
    if reset_pool and pool.count()==0:
        return HttpResponseRedirect('/profile/')
    elif pool.count()>=1 and not reset_pool:
        print('1 false, 0 true')
        new_pool = []
        for id in pool:
            new_pool.append(id['id'])
        selected_index = new_pool[0]
        selected_activity = Activity.objects.get(id=selected_index)
        selected_activity.is_chosen=True
        selected_activity.save(update_fields=['is_chosen'])
        # return HttpResponseRedirect('/groups/'pk)
        return HttpResponseRedirect('/profile')

    print('here is the reset_pool', reset_pool)
    reset_pool.is_chosen = False
    print('here is the reset_pool...reset...', reset_pool)
    reset_pool.save(update_fields=['is_chosen'])
    print('pool is', pool)
    new_pool = []
    for id in pool:
        new_pool.append(id['id'])
    print('pool after running for in', new_pool)
    # without_last_chosen = pool.exclude(is_chosen == True)
    # print(without_last_chosen)
    temp_selected_index = random.randint(0, len(new_pool)-1)
    print('the range is:', len(pool))
    print('selected index is', temp_selected_index)
    print('the chosen one is', new_pool[temp_selected_index])
    selected_index = new_pool[temp_selected_index]
    # return new_pool[selected_index]
    selected_activity = Activity.objects.get(id=selected_index)
    # selected_activity = list(Activity.objects.filter(id=selected_index).values()) ###
    print('selected_activity before changing to TRUE', selected_activity)
    selected_activity.is_chosen = True
    # selected_activity[0]['is_chosen'] = True
    print('made it TRUE', selected_activity)
    selected_activity.save(update_fields=['is_chosen'])
    # print('selected_activity after changing is_chosen', selected_activity)
    # return HttpResponseRedirect('/groups/'pk)
    return HttpResponseRedirect('/groups/%s' % pk)


def activity_create(request, pk):
    if request.user.is_authenticated:
        form = ActivityCreate(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            group = Group.objects.get(id=pk)
            print('group is:', group)
            activity.group = group
            print('activity.group is:', activity.group)
            activity.save()
            return HttpResponseRedirect('/profile/')
        else:
            print('form was invalid')
            return render(request, 'groups_form.html', {'form':form})
        
    else:
        return HttpResponse('go away')

# ===
# Groups
# ===

def groups_list(request):
    user = Profile.objects.get(user=request.user)
    groups = Group.objects.exclude(users=user)
    return render(request, 'groups_list.html', {'groups':groups})

class GroupsView(generic.ListView):
    template_name = 'groups.html'
    context_object_name = 'groups' 

    def get_queryset(self):
        return Group.objects.order_by('-pub_date')

def groups_detail(request, pk):
    group = Group.objects.get(id=pk)
    group_users = User_Group.objects.filter(group=group).values()
    print('group_users:', group_users)
    person_in_group = False

    for person in group_users:
        print('person', person, 'user id', request.user.id)
        if person['user_id'] == request.user.id:
            person_in_group = True

    activities = None
    form = ActivityCreate
    try:
        activities = Activity.objects.filter(group_id=group).values()
        print(activities)
    except:
        pass
        print('it passed')
        print('it knew it was this group:', group)
        print(activities)
    return render(request, "groups_detail.html", {'group':group, 'activities': activities, 'form':form, 'person_in_group': person_in_group})

def groups_join(request, pk):
    group = Group.objects.get(id=pk)
    print('this is that group', group)
    user = (request.user)
    print('this is that user', user)
    user_group = User_Group()
    print('this is the user_group', User_Group)
    user_group.group = group
    user_group.user = user.profile
    print('this is user_group right before saved', user_group)
    user_group.save()
    return HttpResponseRedirect('/groups/')

def groups_form(request):
    form = GroupCreate
    return render(request, 'groups_form.html', {'form':form})

def groups_create(request):
    if request.user.is_authenticated:
        form = GroupCreate(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            user = (request.user)
            group.save()

            # Warning: ONLY do if user not already in group
            user_group = User_Group()
            user_group.group = group
            user_group.user = user.profile
            user_group.save()
            return HttpResponseRedirect('/groups/')
        else:
            print('form was invalid')
            return render(request, 'groups_form.html', {'form':form})
        
    else:
        return HttpResponse('go away')
# ===
# AUTH
# ===

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        print('POSTING to Login view')
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        print('form content', form)
        if form.is_valid():
            print('form is valid')
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                print('user is not none', user)
                if user.is_active:
                    print('user is active')
                    login(request, user)
                    print('logged in?????', request.user)
                    return HttpResponseRedirect('/profile')
                else:
                    print("The account has been disabled.")
                    return HttpResponseRedirect('/login')
            else:
                print("The username and/or password is incorrect.")
                return HttpResponseRedirect('/login')
        else:
            print('INVALID FORM')
            return HttpResponseRedirect('/login')
    else:
        print('login get method')
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

