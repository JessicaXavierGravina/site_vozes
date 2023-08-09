# Generated by Django 4.2.2 on 2023-06-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vox', '0014_alter_dubladore_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubladore',
            name='categoria',
            field=models.CharField(choices=[('Adulta Feminina', 'Adulta Feminina'), ('Adolescente Feminina', 'Adolescente Feminina'), ('Meia Idade Masculina', 'Meia Idade Masculina'), ('Jovem Feminina Leve', 'Jovem Feminina Leve'), ('Jovem Feminina', 'Jovem Feminina'), ('Infantil Feminina', 'Infantil Feminina'), ('Meia Idade Feminina', 'Meia Idade Feminina'), ('Idosa Feminina', 'Idosa Feminina'), ('Idosa Feminina Pesada', 'Idosa Feminina Pesada'), ('Infantil Masculina', 'Infantil Masculina'), ('Idosa Masculina Pesada', 'Idosa Masculina Pesada'), ('Idosa Masculina', 'Idosa Masculina'), ('Jovem Masculina Pesada', 'Jovem Masculina Pesada'), ('Idosa Feminina Leve', 'Idosa Feminina Leve'), ('Adulta Masculina', 'Adulta Masculina'), ('Jovem Masculina', 'Jovem Masculina'), ('Jovem Feminina Pesada', 'Jovem Feminina Pesada'), ('Adulta Feminina Leve', 'Adulta Feminina Leve'), ('Adulta Masculina Leve', 'Adulta Masculina Leve'), ('Adulta Feminina Pesada', 'Adulta Feminina Pesada'), ('Idosa Masculina Leve', 'Idosa Masculina Leve'), ('Adulta Masculina Pesada', 'Adulta Masculina Pesada'), ('Jovem Masculina Leve', 'Jovem Masculina Leve'), ('Adolescente Masculina', 'Adolescente Masculina')], max_length=2500),
        ),
    ]