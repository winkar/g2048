from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from model import m2048


def home(request):
    return render_to_response('base.html',{})

game=m2048()
def start(request):
    game.init()
    for index,item in enumerate(game.board):
        request.session[str(index)]=item
    return render_to_response('gaming.html',{'item':game.board}) 

def gaming(request,vec):
    for index in range(len(game.board)):
        game.board[index]=request.session[str(index)]

    game.move(vec)
    game.generate()

    for index,item in enumerate(game.board):
        request.session[str(index)]=item

    if game.isFailed():
        return render_to_response('gaming.html',{'item':game.board,'failed':1})

    if game.isWon():
        return render_to_response('gaming.html',{'item':game.board,'Success':1})

    return render_to_response('gaming.html',{'item':game.board,'notyet':1})


def restart(request):
    return render_to_response('restart.html',{})

