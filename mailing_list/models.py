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


class MailingListSetup(models.Model):
	STATUS = (('Active','Active'),('Inactive','Inactive'))
	mailing_list = models.ForeignKey('MailingList',on_delete = models.CASCADE,db_column = 'CG_ML_STP_ID')
	parameter = models.CharField(max_length = 255,db_column = 'CG_ML_STP_PARAMETER')
	value = models.CharField(max_length = 500,null = True,db_column = 'CG_ML_STP_VALUE')
	inclusion_flag = models.BooleanField(default = False,db_column = 'CG_ML_STP_INC_FLG')
	status = models.CharField(max_length = 20,null = True,choices = STATUS)


# class Campaign(models.Model):
# 	CAMPAIGN_STATUS = (('Draft','draft'),('Co-author Validation','co_author_validation'),('Approval Waiting','approval_waiting'),('Confirmed','confirmed'),('Scheduled','scheduled'),('Sent','sent'))
# 	id = models.AutoField(primary_key = True,db_column = 'CG_CAMPAIGN_ID')
# 	name = models.CharField(max_length = 255,db_column = 'CG_CAMPAIGN_NAME')
# 	description = models.TextField(null = True,db_column = 'CG_CAMPAIGN_DESC')
# 	creation_date = models.DateField(db_column = 'CG_CAMPAIGN_CREATION_DT')
# 	creator = models.ForeignKey('users.User',db_column = 'CG_CAMPAIGN_CREATOR_CUID')
# 	mailing_list = models.ForeignKey('mailing_list.MailingList',null = True,db_column = 'CG_ML_ID')
# 	status = models.CharField(max_length = 20,null = True,db_column = 'CG_CAMPAIGN_STATUS')
# 	clone = models.CharField(max_length = 15,null = True,db_column = 'CG_CAMPAIGN_CLONE_ID')
# 	template = models.ForeignKey('mailing_templates',null = True,db_column = 'CG_MT_ID')
# 	exclusion = models.TextField(null = True,db_column = 'CG_CAMPAIGN_EXC')
# 	inclusion = models.TextField(null = True,db_column = 'CG_CAMPAIGN_INC')
# 	campaign_from = models.CharField(null = True,max_length = 255,db_column = 'CG_CAMPAIGN_FROM')
# 	campaign_cc = models.CharField(null = True,max_length = 255,db_column = 'CG_CAMPAIGN_CC')
# 	campaign_bcc = models.CharField(null = True,max_length = 255,db_column = 'CG_CAMPAIGN_BCC')
# 	campaign_body = models.TextField(null = True,db_column = 'CG_CAMPAIGN_BODY')
# 	recurrence = models.CharField(null = True,db_column = 'CG_CAMPAIGN_REC_ID')

# 	class Meta:
# 		db_table = 'CG_Campaign_tbl'


# class CampaignAuthor(models.Model):
# 	campaign = models.ForeignKey('Campaign',on_delete = models.CASCADE,db_column = 'CG_CAMPAIGN_ID')
# 	user = models.ForeignKey('users.User',on_delete = models.CASCADE,db_column = 'CG_CAMPAIGN_USER_ID')
# 	role = models.ForeignKey('users.Roles',on_delete = models.CASCADE,db_column = 'CG_CAMPAIGN_USER_ROLE')
# 	flag = models.CharField(max_length = 2,null = True,db_column = 'CG_CAMPAIGN_USER_EDIT_FLG')
# 	last_updated_date = models.DateTimeField(auto_now = True,db_column = 'CG_CAMPAIGN_USER_LAST_DATE')
# 	status = models.CharField(max_length = 20,null = True,db_column = 'CG_CAMPAIGN_USER_STATUS')

# 	class Meta:
# 		db_table = 'CG_Campaign_author_tbl'

# class CampaignReader(models.Model):
# 	campaign = models.ForeignKey('Campaign',on_delete = models.CASCADE,db_column = 'CG_CAMPAIGN_ID')
# 	reader = models.ForeignKey('users.User',on_delete = models.CASCADE,db_column = 'CG_CAMPAIGN_READER_ID')
# 	status = models.CharField(max_length = 20,null = True,db_column = 'CG_CAMPAIGN_USER_STATUS')

# 	class Meta:
# 		db_table = 'CG_Campaign_reader_tbl'


# class CampaignApprover(models.Model):
# 	ACTION = (('Approve','approve'),('Reject','reject'),('Pending','pending'))
# 	campaign = models.ForeignKey('Campaign',on_delete = models.CASCADE,db_column = 'CG_CAMPAIGN_ID')
# 	level = models.CharField(max_length = 2,db_column = 'CG_CAMPAIGN_APV_LVL')
# 	approver = models.CharField(max_length = 255,db_column = 'CG_CAMPAIGN_APV_NAME')
# 	cuid = models.CharField(max_length = 2,db_column = 'CG_CAMPAIGN_APV_CUID')
# 	action = models.CharField(max_length = 50,db_column = 'CG_CAMPAIGN_APV_ACTN')
# 	date_of_action = models.DateTimeField(db_column = 'CG_CAMPAIGN_APV_ACTNDT')
# 	comment = models.TextField(null = True,db_column = 'CG_CAMPAIGN_APV_COMMENTS')
# 	status = models.CharField(max_length = 20,db_column = 'CG_CAMPAIGN_APV_STATUS')

# 	class Meta:
# 		db_table = 'CG_Campaign_approver_tbl'