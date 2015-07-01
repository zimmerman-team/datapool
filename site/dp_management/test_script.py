from dp_management import models

source = models.DataSource.objects.all()[0]
source.process()