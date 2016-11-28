from django.db import models

class Municipality(models.Model):
    """ Contains info on municipalities available """
    municipal_name = models.CharField(max_length=100)
    fir_name = models.CharField(max_length=100)  # Name from FIR Data
    municipal_id = models.IntegerField(unique=True)


class Node(models.Model):
    """ Main Node Information for Budget Tree """
    code = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self')
    item_type = models.CharField(max_length=6)
    municipality = models.ForeignKey(Municipality)


class Keywords(models.Model):
    """ Tags (user-generated?) for identifying nodes beyond description """
    keyword = models.CharField(max_length=50)
    detail = models.ManyToManyField(Node)


class EntryDetails(models.Model):
    """ Data for individual node instance """
    category = models.ForeignKey(Node)
    year = models.PositiveSmallIntegerField()
    amount = models.IntegerField()
    comments = models.TextField()


class ClosureTable(models.Model):
    """ Used to keep tree information in SQL format """
    ancestor = models.ForeignKey(Node, related_name='ancestor')
    descendant = models.ForeignKey(Node, related_name='descendant')
    depth = models.IntegerField()


# Closure model for Modeling tree to SQL
# http://mikehillyer.com/articles/managing-hierarchical-data-in-mysql/
# http://www.slideshare.net/billkarwin/models-for-hierarchical-data
# https://coderwall.com/p/lixing/closure-tables-for-browsing-trees-in-sql
