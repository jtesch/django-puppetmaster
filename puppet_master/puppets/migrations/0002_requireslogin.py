from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('puppets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='puppet',
            name='requires_login',
            field=models.BooleanField(default=False),
        )
    ]