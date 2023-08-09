# Generated by Django 4.2.2 on 2023-07-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vox', '0021_alter_dubladore_canta_alter_dubladore_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubladore',
            name='categoria',
            field=models.CharField(blank=True, choices=[('Idosa Feminina Leve', 'Idosa Feminina Leve'), ('Adulta Masculina Leve', 'Adulta Masculina Leve'), ('Infantil Feminina', 'Infantil Feminina'), ('Jovem Feminina', 'Jovem Feminina'), ('Idosa Feminina', 'Idosa Feminina'), ('Adulta Feminina Leve', 'Adulta Feminina Leve'), ('Jovem Masculina Leve', 'Jovem Masculina Leve'), ('Jovem Masculina', 'Jovem Masculina'), ('Adulta Feminina Pesada', 'Adulta Feminina Pesada'), ('Idosa Feminina Pesada', 'Idosa Feminina Pesada'), ('Infantil Masculina', 'Infantil Masculina'), ('Adolescente Masculina', 'Adolescente Masculina'), ('Meia Idade Feminina', 'Meia Idade Feminina'), ('Adolescente Feminina', 'Adolescente Feminina'), ('Jovem Feminina Pesada', 'Jovem Feminina Pesada'), ('Meia Idade Masculina', 'Meia Idade Masculina'), ('Idosa Masculina Pesada', 'Idosa Masculina Pesada'), ('Adulta Masculina', 'Adulta Masculina'), ('Adulta Feminina', 'Adulta Feminina'), ('Adulta Masculina Pesada', 'Adulta Masculina Pesada'), ('Idosa Masculina', 'Idosa Masculina'), ('Idosa Masculina Leve', 'Idosa Masculina Leve'), ('Jovem Feminina Leve', 'Jovem Feminina Leve'), ('Jovem Masculina Pesada', 'Jovem Masculina Pesada')], max_length=2500),
        ),
        migrations.AlterField(
            model_name='dubladore',
            name='nascimento',
            field=models.DateField(null=True, verbose_name='Data de Nascimento'),
        ),
    ]