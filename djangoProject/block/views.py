from django.shortcuts import render
from django.http import HttpResponse
from block import models
from block.My_Forms import EmpForm
from blockchain_ex import Blockchain, Block_ex
import time
from django.core.exceptions import ValidationError
import json


# Create your views here.
def user_exist(request):
    return HttpResponse("users exist")


def add_emp(request):
    if request.method == 'GET':
        form = EmpForm()
        return render(request, "add_emp.html", {"form": form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():  # 进行数据校验
            data = form.cleaned_data
            data.pop('r_salary')
            print(data)

            models.Emp.objects.create(**data)
            return HttpResponse("OK")
        else:
            print(form.errors)
            clean_errors = form.errors.get("__all__")
            print(222, clean_errors)
        return render(request, "add_emp.html", {"form": form, "clean_errors": clean_errors})


def home_page(request):
    return render(request, "tables.html")


def chart_page(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        key = request.POST.get("key")
        address = request.POST.get("address")
        simple_block = models.SimpleBlock(name=name, key=key, address=address)
        simple_block.save()
    return render(request, "charts.html")


def new_transaction(request):
    if request.method == 'POST':
        parameters = request.POST.get("parameters")
        blockchain.add_new_transaction(parameters)
        blockchain.mine()
        block_to_save = blockchain.last_block
        print(block_to_save.timestamp)
        block_save = models.Block(index=block_to_save.index, previous_hash=block_to_save.previous_hash,
                                  timestamp=block_to_save.timestamp, nonce=block_to_save.nonce, transactions=block_to_save.transactions)
        block_save.save()
        print(block_to_save.index)
    return render(request, "new_transaction_post.html")




blockchain = Blockchain()
blockchain.create_genesis_block()
peers = set()
