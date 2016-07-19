#show all reuqest.META data
def dispaly_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append('<tr><td>%s</td></tr>'%(k,v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

#create a search chart
def search_form(request):
    return render_to_response('search_form.html')
# def search(request):
#     if 'q' in request.GET：#类字典对象，有一部分字典的方法（get keys values)可能远来自《form》表单提交，也可能是URL中的查询字符串
#         message = 'You searched for:%r' % request.GET['q']
#     else:
#         message = 'You submmited an empty form.'
#     return HttpResponse(message)

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)#用filter查找含q的书籍，icontains是查找关键字
        return render_to_response('search_results.html',
            {'books':books,'query':q}
    else:
        # return HttpResponse('Please submit a search term.')
        return render_to_response('search_form.html',{'error':True})
        
