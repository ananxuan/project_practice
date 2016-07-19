#reuqest.path()除域名以外的请求路径，正斜杠开头'/hello/'
#request.get_host() 主机名 127.0.0.1:8000  www.example.com
#request.get_full_path()请求路径，可能包含查询字符 '/hello/?print=true'
#requet.is_secure 如果通过HTTPS访问则返回True，否则返回False

#BAD!
def ua_display_bad(request):
  ua = request.META['HTTP_USER_AGENT'] #might raise keyerror
  return HttpResponse('your browser is %s'%ua)
  
#GOOD1
def ua_dispaly_good1(request):
  try:
    ua = request.META['HTTP_USER_AGENT']
  except Keyerror:
    ua = 'unknown'
  return HttpResponse('your browser is %s' % ua)
  
#GOOD2
def ua_dispaly_good2(request):
  ua= request.META.get('HTTP_USER_AGENT','unknown')
  return HttpResponse('your browser is %s' % ua)
  
