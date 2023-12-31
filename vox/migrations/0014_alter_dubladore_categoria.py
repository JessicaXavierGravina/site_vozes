# Generated by Django 4.2.2 on 2023-06-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vox', '0013_alter_dubladore_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubladore',
            name='categoria',
            field=models.CharField(choices=[('Infantil Feminina', 'Infantil Feminina'), ('Meia Idade Masculina', 'Meia Idade Masculina'), ('Adulta Masculina Pesada', 'Adulta Masculina Pesada'), ('Adulta Feminina Pesada', 'Adulta Feminina Pesada'), ('Idosa Feminina Leve', 'Idosa Feminina Leve'), ('Jovem Feminina Leve', 'Jovem Feminina Leve'), ('Idosa Masculina Leve', 'Idosa Masculina Leve'), ('Jovem Masculina Pesada', 'Jovem Masculina Pesada'), ('Meia Idade Feminina', 'Meia Idade Feminina'), ('Idosa Feminina Pesada', 'Idosa Feminina Pesada'), ('Adulta Feminina Leve', 'Adulta Feminina Leve'), ('Idosa Feminina', 'Idosa Feminina'), ('Infantil Masculina', 'Infantil Masculina'), ('Adulta Feminina', 'Adulta Feminina'), ('Adolescente Feminina', 'Adolescente Feminina'), ('Idosa Masculina', 'Idosa Masculina'), ('Jovem Masculina Leve', 'Jovem Masculina Leve'), ('Jovem Feminina', 'Jovem Feminina'), ('Jovem Masculina', 'Jovem Masculina'), ('Jovem Feminina Pesada', 'Jovem Feminina Pesada'), ('Adolescente Masculina', 'Adolescente Masculina'), ('Idosa Masculina Pesada', 'Idosa Masculina Pesada'), ('Adulta Masculina', 'Adulta Masculina'), ('Adulta Masculina Leve', 'Adulta Masculina Leve')], max_length=2500),
        ),
    ]