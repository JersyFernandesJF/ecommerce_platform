# Generated by Django 5.0.3 on 2024-03-13 07:27

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shoppingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=3, max_digits=3)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=3)),
                ('provider', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(choices=[('cancelled', 'Cancelled'), ('inprogress', 'Progress'), ('paid', 'Paid')], max_length=16, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=3, max_digits=3)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(max_length=40)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('number_phone', models.CharField(max_length=17)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'authApp_user',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=3)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.orderdetails')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingApp.product')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='payment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.paymentdetails'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingApp.product')),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.shoppingsession')),
            ],
        ),
        migrations.AddField(
            model_name='shoppingsession',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.user'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.user'),
        ),
        migrations.CreateModel(
            name='UserAdress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('address_line1', models.CharField(max_length=50)),
                ('address_line2', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('telephone', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=30)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserPayment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('payment_type', models.CharField(choices=[('card', 'Card'), ('cash', 'Cash')], max_length=16, null=True)),
                ('provider', models.CharField(blank=True, max_length=15, null=True)),
                ('account_no', models.IntegerField(blank=True, null=True)),
                ('expiry', models.CharField(blank=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.user')),
            ],
        ),
    ]
