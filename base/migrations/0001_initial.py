# Generated by Django 4.0.4 on 2022-04-17 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('social_number', models.CharField(max_length=20)),
                ('nation_id', models.CharField(max_length=20)),
                ('salary_per_month', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True)),
                ('salary_per_work', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(default='employee.jpg', upload_to='employee/image')),
            ],
        ),
        migrations.CreateModel(
            name='Gardner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('social_number', models.CharField(max_length=20)),
                ('nation_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('qty', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('unit', models.CharField(choices=[('kg', 'کیلو گرام'), ('ser', 'سیر'), ('man', 'من'), ('boji', 'بوجی'), ('cartoon', 'کارتن')], default='kg', max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.category')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_type', models.CharField(choices=[('export', 'صادرات'), ('internal', 'داخلی')], default='export', max_length=20)),
                ('unit', models.CharField(choices=[('kg', 'کیلو گرام'), ('ser', 'سیر'), ('man', 'من'), ('boji', 'بوجی'), ('cartoon', 'کارتن')], default='kg', max_length=20)),
                ('price_per_unit', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('price_in_letter', models.CharField(max_length=200)),
                ('get_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('unit_price', models.CharField(choices=[('usd', 'دالر'), ('euro', 'یورو'), ('pk', 'کلدار'), ('ir', 'تومن'), ('afg', 'افغانی'), ('yen', 'ین چین')], default='afg', max_length=20)),
                ('created_at', models.DateField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('qty', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('unit', models.CharField(choices=[('kg', 'کیلو گرام'), ('ser', 'سیر'), ('man', 'من'), ('boji', 'بوجی')], default='kg', max_length=10)),
                ('stauts', models.CharField(choices=[('phase_1', 'خریداری'), ('phase_2', 'دسته بندی'), ('phase_3', 'فروش')], default='phase_2', max_length=20)),
                ('location', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('paid_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.employee')),
                ('gardner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.gardner')),
            ],
        ),
    ]
