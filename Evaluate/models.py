from django.db import models
from Account.models import CustomUser

# Create your models here.
class የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model(models.Model):
    user  = models.ForeignKey(CustomUser , on_delete=models.CASCADE , null = True)
    የሰራተኛው_ሙሉ_ስም = models.CharField(max_length=100, null=True, blank=True)
    የቅርብ_ኃላፊው_ሙሉ_ስም = models.CharField(max_length=100, null=True, blank=True)
    የስራ_መደቡ_መጠሪያ = models.CharField(max_length=100, null=True, blank=True)
    ደረጃ = models.CharField(max_length=100, null=True, blank=True)
    d1 = models.IntegerField(null = True)
    d2 = models.IntegerField(null = True)
    m1 = models.IntegerField(null = True)
    m2 = models.IntegerField(null = True)
    y1 = models.IntegerField(null = True)
    y2 = models.IntegerField(null = True)

    ተገልጋይ_1 = models.IntegerField(null=True, blank=True)
    ተገልጋይ_2 = models.IntegerField(null=True, blank=True)
    ተገልጋይ_3 = models.IntegerField(null=True, blank=True)

    ፋይናንስ_1 = models.IntegerField(null=True, blank=True)
    ፋይናንስ_2 = models.IntegerField(null=True, blank=True)
    ፋይናንስ_3 = models.IntegerField(null=True, blank=True)
    ፋይናንስ_4 = models.IntegerField(null=True, blank=True)
    ፋይናንስ_5 = models.IntegerField(null=True, blank=True)
    ፋይናንስ_6 = models.IntegerField(null=True, blank=True)

    የውስጥ_አሰራር_1 = models.IntegerField(null=True, blank=True)
    የውስጥ_አሰራር_2 = models.IntegerField(null=True, blank=True)
    የውስጥ_አሰራር_3 = models.IntegerField(null=True, blank=True)
    የውስጥ_አሰራር_4 = models.IntegerField(null=True, blank=True)
    የውስጥ_አሰራር_5 = models.IntegerField(null=True, blank=True)
    የውስጥ_አሰራር_6 = models.IntegerField(null=True, blank=True)
    የውስጥ_አሰራር_7 = models.IntegerField(null=True, blank=True)
    
    መማርና_እድገት_1 = models.IntegerField(null=True, blank=True)
    መማርና_እድገት_2 = models.IntegerField(null=True, blank=True)
    መማርና_እድገት_3 = models.IntegerField(null=True, blank=True)
    መማርና_እድገት_4 = models.IntegerField(null=True, blank=True)
    መማርና_እድገት_5 = models.IntegerField(null=True, blank=True)
    መማርና_እድገት_6 = models.IntegerField(null=True, blank=True)
    መማርና_እድገት_7 = models.IntegerField(null=True, blank=True)
    መማርና_እድገት_8 = models.IntegerField(null=True, blank=True)
    መማርና_እድገት_9 = models.IntegerField(null=True, blank=True)
    መማርና_እድገት_10 = models.IntegerField(null=True, blank=True)
    መማርና_እድገት_11 = models.IntegerField(null=True, blank=True)
    መማርና_እድገት_12 = models.IntegerField(null=True, blank=True)
    user  = models.ForeignKey(CustomUser , on_delete=models.CASCADE , null = True)
    
    def __str__(self) -> str:
        return self.የሰራተኛው_ሙሉ_ስም
    
class የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_model(models.Model):
    user = models.ForeignKey(CustomUser, null = True, on_delete = models.CASCADE, blank = True)
    ምዘናው_የተሞላለት_ስም = models.CharField(max_length=100)
    ምዘናውን_የሞላው_ኃላፊ_ስም = models.CharField(max_length=100)
    d1 = models.IntegerField(null = True)
    d2 = models.IntegerField(null = True)
    m1 = models.IntegerField(null = True)
    m2 = models.IntegerField(null = True)
    y1 = models.IntegerField(null = True)
    y2 = models.IntegerField(null = True)
    value1 = models.IntegerField(null = True)
    value2 = models.IntegerField(null = True)
    value3 = models.IntegerField(null = True)
    value4 = models.IntegerField(null = True)
    value5 = models.IntegerField(null = True)
    value6 = models.IntegerField(null = True)
    value7 = models.IntegerField(null = True)
    value8 = models.IntegerField(null = True)
    value9 = models.IntegerField(null = True)
    value10 = models.IntegerField(null = True)
    
    def __str__(self) -> str:
        return self.ምዘናው_የተሞላለት_ስም
    
class የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_model(models.Model):
    user = models.ForeignKey(CustomUser, null = True, on_delete = models.CASCADE, blank = True)
    ምዘናው_የተሞላለት_ስም = models.CharField(max_length=100)
    ምዘናውን_የሞላው_ኃላፊ_ስም = models.CharField(max_length=100)
    d1 = models.IntegerField(null = True)
    d2 = models.IntegerField(null = True)
    m1 = models.IntegerField(null = True)
    m2 = models.IntegerField(null = True)
    y1 = models.IntegerField(null = True)
    y2 = models.IntegerField(null = True)
    value1 = models.IntegerField(null = True)
    value2 = models.IntegerField(null = True)
    value3 = models.IntegerField(null = True)
    value4 = models.IntegerField(null = True)
    value5 = models.IntegerField(null = True)
    value6 = models.IntegerField(null = True)
    value7 = models.IntegerField(null = True)
    value8 = models.IntegerField(null = True)
    value9 = models.IntegerField(null = True)
    value10 = models.IntegerField(null = True)
    
    def __str__(self) -> str:
        return self.ምዘናው_የተሞላለት_ስም 
    
class የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model(models.Model):
    ምዘናው_የተሞላለት_ስም = models.CharField(max_length=100)
    ምዘናውን_የሞላው_ኃላፊ_ስም = models.CharField(max_length=100)
    d1 = models.IntegerField(null = True)
    d2 = models.IntegerField(null = True)
    m1 = models.IntegerField(null = True)
    m2 = models.IntegerField(null = True)
    y1 = models.IntegerField(null = True)
    y2 = models.IntegerField(null = True)
    value1 = models.IntegerField(null = True)
    value2 = models.IntegerField(null = True)
    value3 = models.IntegerField(null = True)
    value4 = models.IntegerField(null = True)
    value5 = models.IntegerField(null = True)
    value6 = models.IntegerField(null = True)
    value7 = models.IntegerField(null = True)
    value8 = models.IntegerField(null = True)
    value9 = models.IntegerField(null = True)
    value10 = models.IntegerField(null = True)
    
    def __str__(self) -> str:
        return self.ምዘናው_የተሞላለት_ስም
    
class የድርጊት_መርሃ_ግብር_ቅፅ_model(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.SET_NULL, null = True)
    የሰራተኛው_ሙሉ_ስም = models.CharField(max_length=100, null=True, blank=True)
    የቅርብ_ኃላፊው_ሙሉ_ስም = models.CharField(max_length=100, null=True, blank=True)
    የስራ_መደቡ_መጠሪያ = models.CharField(max_length=100, null=True, blank=True)
    ደረጃ = models.CharField(max_length=100, null=True, blank=True)
    d1 = models.IntegerField(null = True)
    d2 = models.IntegerField(null = True)
    m1 = models.IntegerField(null = True)
    m2 = models.IntegerField(null = True)
    y1 = models.IntegerField(null = True)
    y2 = models.IntegerField(null = True)
    
    def __str__(self) -> str:
        return self.የሰራተኛው_ሙሉ_ስም