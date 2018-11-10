from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger


def page(request,obj,count=5):
    '''分页公共方法'''

    paginator = Paginator(obj, count)

    page = request.GET.get("page")

    try:
        contacts = paginator.get_page(page)
    except EmptyPage:
        contacts = paginator.page(1)
    except PageNotAnInteger:
        contacts = paginator.page(paginator.num_pages)

    return contacts