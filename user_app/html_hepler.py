#coding:utf-8

from django.utils.safestring import mark_safe


class PageInfo:
    def __init__(self,current_page,all_count,per_item=10):
        #print current_page,all_count # 2 11
        self.CurrentPage = current_page
        self.AllCount = all_count
        self.PerItem = per_item

    @property
    def start(self):

        return (self.CurrentPage-1) * self.PerItem

    @property
    def end(self):

        return self.CurrentPage * self.PerItem

    @property
    def all_page_count(self):

        temp = divmod(self.AllCount,self.PerItem)
        if temp[1] == 0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0] + 1
        return all_page_count


def Pager(page,all_page_count):

    page_html = []


    if page <= 1:
        prev_html = "<li class='next'><a href='#'>上一页</a></li>"
    else:
        prev_html = "<li class='next'><a href='/project_manage/?page=%d'>上一页</a></li>" % (page - 1)

    page_html.append(prev_html)

    if all_page_count < 11:
        begin = 0
        end = all_page_count
    else:
        if page < 6:
            begin = 0
            end = 11
        else:
            if page + 6 > all_page_count:
                begin = page -  6
                end = all_page_count
            else:
                begin = page - 5
                end = page + 5

    for i in range(begin,end):
        #print begin,end
        if page == i+1:
            a_html = "<li class='prev disabled'><a href = '/project_manage/?page=%d'>%d</a></li>"%(i+1,i+1)
        else:
            a_html = "<li class='prev disabled'><a href = '/project_manage/?page=%d'>%d</a></li>" % (i+1, i+1)

        page_html.append(a_html)
    next_html = "<li class='next'><a href = '/project_manage/?page=%d'>下一页</a></li>" % (page + 1)
    page_html.append(next_html)
    page_string = mark_safe("".join(page_html))
    return page_string
