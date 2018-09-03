from django.db import models

# Create your models here.
from django.db import models
# from users import models

# Create your models here.

class MailingList(models.Model):
	LIST_TYPES = (('Public','Public'),('Shared','Shared'))
	STATUS = (('Active','Active'),('Inactive','Inactive'))
	id = models.AutoField(primary_key = True,db_column = 'CG_ML_ID')
	name = models.CharField(max_length = 255,db_column = 'CG_ML_NAME')
	description = models.TextField(null = True,db_column = 'CG_ML_DESC')
	creation_date = models.DateField(db_column = 'CG_ML_CREATION_DATE')
	creator = models.ForeignKey('users.User',on_delete = models.CASCADE,db_column = 'CG_ML_CREATOR_ID',null = True,related_name = 'mailing_list_creator')
	modification_date = models.DateField(db_column = 'CG_ML_MODIFICATION_DATE',null = True)
	modifier = models.ForeignKey('users.User',on_delete = models.CASCADE,db_column = 'CG_ML_MODIFIER_ID',null = True, related_name = 'mailing_list_modifier')
	type_of_list = models.CharField(max_length = 20,choices = LIST_TYPES,db_column = 'CG_ML_TYPE')
	status = models.CharField(max_length = 20,choices = STATUS,db_column = 'CG_ML_STATUS')

	class Meta:
		db_table = 'CM_Mailing_list_tbl'

class MailingListUser(models.Model):
	ACCESS_TYPES = (('Public','Public'),('Shared','Shared'))
	mailing_list = models.ForeignKey('MailingList',on_delete = models.CASCADE,db_column = 'CG_ML_ID')
	mailing_user = models.ForeignKey('users.User',on_delete = models.CASCADE, db_column = 'CG_ML_USER_ID')
	access_type = models.CharField(max_length = 20,choices = ACCESS_TYPES)

	class Meta:
		db_table = 'CM_Mailing_list_usr_tbl'


class MailingListCustomerUpload(models.Model):
	list_id = models.ForeignKey('MailingList',on_delete = models.CASCADE,db_column = 'CG_ML_CU_ID')
	emails = models.TextField(null = True,db_column = 'CG_ML_CU_EMAILS')

	class Meta:
		db_table = 'CM_Mailing_list_custupl_tbl'

