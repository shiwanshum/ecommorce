# Generated by Django 3.2.10 on 2022-02-04 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userpayment',
            name='order',
            field=models.ManyToManyField(to='ecommerce.Order'),
        ),
        migrations.AddField(
            model_name='userpayment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subcategories',
            name='categories_name',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.categories'),
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ManyToManyField(blank=True, to='ecommerce.Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.categories'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.size'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategories',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.subcategories'),
        ),
        migrations.AddField(
            model_name='orderstatus',
            name='Order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.order'),
        ),
        migrations.AddField(
            model_name='orderedbag',
            name='bag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.bag'),
        ),
        migrations.AddField(
            model_name='orderedbag',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='bag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.bag'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='offer',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product'),
        ),
        migrations.AddField(
            model_name='items',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.offer'),
        ),
        migrations.AddField(
            model_name='items',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product'),
        ),
        migrations.AddField(
            model_name='bag',
            name='item',
            field=models.ManyToManyField(blank=True, default=None, to='ecommerce.Items', verbose_name='Items'),
        ),
        migrations.AddField(
            model_name='bag',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]