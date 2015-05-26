#-*- coding:utf-8 -*-
from django.db import models

# Create your models here

class QQInfo(models.Model):

    qq = models.CharField("QQ号", max_length= 25)
    nick = models.CharField("昵称",  max_length= 64)
    sex = models.CharField("性别",  max_length= 20)
    position = models.CharField("群职位", max_length= 20, help_text= "成员;创始人;管理员")
    group_number = models.CharField("群号码", max_length= 25)

    class Meta:
        db_table = "qq_info"

def  qqInfoSave(info):

    qq_records = QQInfo( qq = info.pop("qq"), nick = info.pop("nick"), sex = info.pop("sex"),
                           position = info.pop("position"), group_number = info.pop("group_number") )
    qq_records.save()




class QQGroup(models.Model):

    name = models.CharField("群名字", max_length= 64)
    group_number = models.CharField("群号码", max_length= 25)
    qq = models.CharField("QQ号", max_length= 25)
    nick = models.CharField("昵称", max_length= 64)
    sex = models.CharField("性别", max_length= 20)
    position = models.CharField("群职位", max_length= 20)

    class Meta:
        db_table = "qq_group"

def groupInfoSave(info):

    qq_group_info = QQGroup( name = info.pop("name"), group_number = info.pop("group_number"),
                                qq = info.pop("qq"), nick = info.pop("nick"), sex = info.pop("sex"), position = info.pop("position") )
    qq_group_info.save()

