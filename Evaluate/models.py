from django.db import models
from Account.models import CustomUser

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.SET_NULL, null = True)
    የሰራተኛው_ሙሉ_ስም = models.CharField(max_length=100, null=True, blank=True)
    የቅርብ_ኃላፊው_ሙሉ_ስም = models.CharField(max_length=100, null=True, blank=True)
    የስራ_መደቡ_መጠሪያ = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self) -> str:
        return self.የሰራተኛው_ሙሉ_ስም

class የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model(models.Model):
    የሰራተኛው_ሙሉ_ስም = models.CharField(max_length=100)
    የቅርብ_ኃላፊው_ሙሉ_ስም = models.CharField(max_length=100)
    የስራ_መደቡ_መጠሪያ = models.CharField(max_length=100)
    ደረጃ = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.የሰራተኛው_ሙሉ_ስም
    
class የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_model(models.Model):
    ምዘናው_የተሞላለት_ስም = models.CharField(max_length=100)
    ምዘናውን_የሞላው_ኃላፊ_ስም = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.ምዘናው_የተሞላለት_ስም
    
class የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_model(models.Model):
    ምዘናው_የተሞላለት_ስም = models.CharField(max_length=100)
    ምዘናውን_የሞላው_ኃላፊ_ስም = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.ምዘናው_የተሞላለት_ስም 
    
class የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model(models.Model):
    ምዘናው_የተሞላለት_ስም = models.CharField(max_length=100)
    ምዘናውን_የሞላው_ኃላፊ_ስም = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.ምዘናው_የተሞላለት_ስም
    

class demoModel(models.Model):
    የሰራተኛው_ሙሉ_ስም = models.CharField(max_length=100, null=True, blank=True)
    የቅርብ_ኃላፊው_ሙሉ_ስም = models.CharField(max_length=100, null=True, blank=True)
    የስራ_መደቡ_መጠሪያ = models.CharField(max_length=100, null=True, blank=True)
    ደረጃ = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateTimeField( null=True, blank=True)
    end_date = models.DateTimeField( null=True, blank=True)

    ተገልጋይ_1 = models.IntegerField()
    ተገልጋይ_2 = models.IntegerField()
    ተገልጋይ_3 = models.IntegerField()

    ፋይናንስ_1 = models.IntegerField()
    ፋይናንስ_2 = models.IntegerField()
    ፋይናንስ_3 = models.IntegerField()
    ፋይናንስ_4 = models.IntegerField()
    ፋይናንስ_5 = models.IntegerField()
    ፋይናንስ_6 = models.IntegerField()

    የውስጥ_አሰራር_1 = models.IntegerField()
    የውስጥ_አሰራር_2 = models.IntegerField()
    የውስጥ_አሰራር_3 = models.IntegerField()
    የውስጥ_አሰራር_4 = models.IntegerField()
    የውስጥ_አሰራር_5 = models.IntegerField()
    የውስጥ_አሰራር_6 = models.IntegerField()
    የውስጥ_አሰራር_7 = models.IntegerField()
    
    መማርና_እድገት_1 = models.IntegerField()
    መማርና_እድገት_2 = models.IntegerField()
    መማርና_እድገት_3 = models.IntegerField()
    መማርና_እድገት_4 = models.IntegerField()
    መማርና_እድገት_5 = models.IntegerField()
    መማርና_እድገት_6 = models.IntegerField()
    መማርና_እድገት_7 = models.IntegerField()
    መማርና_እድገት_8 = models.IntegerField()
    መማርና_እድገት_9 = models.IntegerField()
    መማርና_እድገት_10 = models.IntegerField()
    መማርና_እድገት_11 = models.IntegerField()
    መማርና_እድገት_12 = models.IntegerField()
    user  = models.ForeignKey(CustomUser , on_delete=models.CASCADE , null = True)
    
    # def __str__(self) -> str:
    #     return self.user