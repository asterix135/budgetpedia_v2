from django.db import models

class LineItem(models.Model):
    code = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self')
    item_type = models.CharField(max_length=6)

# Closure model for Modeling tree to SQL
# http://mikehillyer.com/articles/managing-hierarchical-data-in-mysql/
# http://www.slideshare.net/billkarwin/models-for-hierarchical-data
# https://coderwall.com/p/lixing/closure-tables-for-browsing-trees-in-sql


class Keywords(models.Model):
    keyword = models.CharField(max_length=50)
    detail = models.ManyToManyField(LineItem)


class CostDetails(models.Model):
    category = models.ForeignKey(LineItem)
    year = models.PositiveSmallIntegerField()
    amount = models.IntegerField()
    multiplier = models.IntegerField()
    currency = models.CharField(max_length=15)
