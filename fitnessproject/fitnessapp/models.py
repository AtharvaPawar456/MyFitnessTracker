from django.db import models

# Create your models here.


# from django.db import models

class UserAccountDetails(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    emailid = models.CharField(max_length=50)

    phoneno = models.CharField(max_length=50)
    accountPack = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    points = models.PositiveIntegerField(default=0, null=True)

    
    def __str__(self):
        return f"{self.id} - {self.user_name} - Pack: {self.accountPack}"


class PaymentsTracking(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    
    plan = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100) # success / fail
    
    timestamp = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id} - {self.user_name} - Plan:{self.plan} - Amount:{self.amount} - Status:{self.status} - Timestamp:{self.timestamp}"


class DailyTracking(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    
    imgPath = models.CharField(max_length=300)
    myheight = models.CharField(max_length=100)
    myweigth = models.CharField(max_length=100)
    
    toDayCalories = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=100)

    
    def __str__(self):
        return f"{self.id} - {self.user_name} - Calories:{self.toDayCalories} - Height:{self.myheight} - Weigth:{self.myweigth} - Timestamp:{self.timestamp}"




# class SecurityFinding(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=50)

#     file_name = models.TextField()
#     file_path = models.TextField(blank=True, null=True)
#     result_file_path = models.TextField()

#     github_link = models.TextField(blank=True, null=True)
#     mode = models.TextField(blank=True, null=True) # semgrep / securegrep
    
#     comment = models.TextField(blank=True, null=True) # 
    
#     total_findings = models.PositiveIntegerField(blank=True, null=True)
#     # high_severity_findings = models.PositiveIntegerField(blank=True, null=True)
#     # medium_severity_findings = models.PositiveIntegerField(blank=True, null=True)
#     # low_severity_findings = models.PositiveIntegerField(blank=True, null=True)
#     # llama_result_file_path = models.TextField(blank=True, null=True)
    
#     def __str__(self):
#         return f"{self.id} - {self.user_name} file:{self.file_name})"







# class LlmFindingResponse(models.Model):


#     id = models.AutoField(primary_key=True)

#     scanid = models.IntegerField(default=0)

#     user_name = models.CharField(max_length=50, default="")
#     projectName = models.CharField(max_length=500, default="")
#     file_name = models.TextField()
    
#     llmresponse = models.TextField(blank=True, null=True) # semgrep / securegrep
    
#     # findings data
    
#     line = models.CharField(max_length=100, default="")
#     code = models.CharField(max_length=1000, default="")
#     message = models.CharField(max_length=10000, default="")
#     MetadataCategory = models.CharField(max_length=100, default="")
#     MetadataConfidence = models.CharField(max_length=100, default="")
#     MetadataImpact = models.CharField(max_length=100, default="")

#     CWE = models.CharField(max_length=1000, default="")
#     OWASP = models.CharField(max_length=1000, default="")
#     Subcategory = models.CharField(max_length=1000, default="")
#     Technology = models.CharField(max_length=1000, default="")
#     Severity = models.CharField(max_length=1000, default="")

#     def __str__(self):
#         return f"llm res for {self.id} - {self.user_name} file:{self.file_name})"
    






# class Product(models.Model):
#     Product_id = models.AutoField(primary_key=True)
#     product_name = models.CharField(max_length=50)
#     category = models.CharField(max_length=50, default="")
#     slug = models.CharField(max_length=100, default="")
#     price = models.IntegerField(default=0)
#     desc = models.CharField(max_length=300)
#     image = models.ImageField(upload_to="tze/images", default="")
#     testimoniallink = models.CharField(max_length=300, default="")
#     ytlink = models.CharField(max_length=300, default="")
#     benifits = models.CharField(max_length=300, default="")
#     how_to_use = models.CharField(max_length=400, default="")
#     doc_link = models.CharField(max_length=300, default="")
#     net_Qty = models.CharField(max_length=100, default="")
#     pack_of = models.CharField(max_length=50, default="")
#     # pub_date = models.DateField()
#     # subcategory = models.CharField(max_length=30, default="")

#     def __str__(self):
#         return self.product_name
    
# mem: member
# class Contact(models.Model):
#     mem_id = models.AutoField(primary_key=True)

#     mem_name = models.CharField(max_length=60, default="")
#     mem_image = models.ImageField(upload_to="tze/contactImages", default="")
#     mem_desc = models.CharField(max_length=300, default="")
#     mem_email = models.CharField(max_length=100, default="")
#     mem_phone = models.IntegerField(default=0)
#     mem_fb_link = models.CharField(max_length=100, default="")
#     mem_IG_link = models.CharField(max_length=100, default="")
#     mem_status = models.CharField(max_length=100, default="")
#     mem_tag = models.CharField(max_length=20, default="")

#     def __str__(self):
#         return self.mem_name
    
# class Contact(models.Model):
#     msg_id = models.AutoField(primary_key=True)

#     name = models.CharField(max_length=50, default="")
#     email = models.CharField(max_length=70, default="")
#     phone = models.IntegerField(default=0)
#     msg = models.CharField(max_length=500, default="")


#     def __str__(self):
#         return self.name