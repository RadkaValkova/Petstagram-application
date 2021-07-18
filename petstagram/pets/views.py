from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetForm, EditPetForm
from petstagram.pets.models import Pet, Like


def list_pets(request):
    all_pets = Pet.objects.all()
    # cat_pets = Pet.objects.filter(type=Pet.TYPE_CHOICE_CAT) - filter only cats
    context = {
        'pets': all_pets,
    }
    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    comments = pet.comment_set.all()
    context = {
        'pet': pet,
        'comment_form': CommentForm(
            initial={
                'pet_pk': pk,
            }
        ),
        'comments': comments,
    }
    return render(request, 'pets/pet_detail.html', context)


# def comment_pet(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = Comment(
#             text=form.cleaned_data['text'],
#             pet=pet,
#         )
#         comment.save()
#     return redirect('pet details', pet.id)

def comment_pet(request,pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect('pet details',pk)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet,
    )
    like.save()
    return redirect('pet details', pet.id)


def create_pet(request):
    if request.method == 'GET':
        form = PetForm()
        context = {
            'form': form,
        }
        return render(request, 'pets/pet_create.html', context)
    else:
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list pets')
        context = {
            'form': form,
        }
        return render(request, 'pets/pet_create.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditPetForm(instance=pet)
        context = {
            'form': form,
            'pet': pet,
        }
        return render(request, 'pets/pet_edit.html', context)
    else:
        form = EditPetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('list pets')
        context = {
            'form': form,
            'pet': pet,
        }
        return render(request, 'pets/pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
        }
        return render(request, 'pets/pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')
