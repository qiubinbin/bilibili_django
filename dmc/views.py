from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Dmc


def Dmc_detail(request, dmc_id):  # Create your views here.
    # try:
    #     dmc = Dmc.objects.get(id=dmc_id)
    #     context = {'dmc': dmc}
    #     # return render(request, 'dmc.html', context)  # 将字典传入模板,在html用{{}}引用
    #     return render_to_response('dmc.html', context)  # 同上
    # except Dmc.DoesNotExist:
    #     raise Http404('不存在')
    # # return HttpResponse('<h1>Dmc的标题:%s</h1><br>Dmc的内容:%s' % (dmc.title, dmc.content))  # <br>是换行
    # 或者以下方法：
    dmc = get_object_or_404(Dmc, id=dmc_id)
    context = {'dmc': dmc}
    return render_to_response('dmc.html', context)


def Dmc_list(request):
    dmcs = Dmc.objects.filter(is_deleted=False)  # 过滤删除项
    context = {'dmcs': dmcs}
    return render_to_response('dmc_list.html', context)
