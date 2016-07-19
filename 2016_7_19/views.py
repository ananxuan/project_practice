from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


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
        
#create a contact function
def contact(request):
    errors = []
    if request.method == 'POST':#用户浏览表单这个值不存在，只有表单提交这个值才出现
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('mesage', ''):
            errors.append('Enter a message')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['sunject'],
                request.POST['message']，
                request.POST.get('email', 'xuan@sina.com'),
                ['siteowner@example.com],
            )#参数列表（主题、正文、寄信人、收信人）
            return HttpResponseRedirect('/contact/thanks/')#邮件发送后网页将重定向值一个包含成功信息的页面，未完成
    return render_to_response('contact_form.html',
        {'errors': errors}
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    
        
        
