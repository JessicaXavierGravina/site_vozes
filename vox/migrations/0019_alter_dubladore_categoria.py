# Generated by Django 4.2.2 on 2023-07-07 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vox', '0018_alter_dubladore_categoria_alter_dubladore_etnia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubladore',
            name='categoria',
            field=models.CharField(choices=[('Jovem Feminina Pesada', 'Jovem Feminina Pesada'), ('Adulta Feminina', 'Adulta Feminina'), ('Adulta Feminina Pesada', 'Adulta Feminina Pesada'), ('Infantil Masculina', 'Infantil Masculina'), ('Jovem Masculina Pesada', 'Jovem Masculina Pesada'), ('Idosa Feminina', 'Idosa Feminina'), ('Adolescente Masculina', 'Adolescente Masculina'), ('Jovem Masculina', 'Jovem Masculina'), ('Infantil Feminina', 'Infantil Feminina'), ('Idosa Masculina', 'Idosa Masculina'), ('Adulta Masculina Pesada', 'Adulta Masculina Pesada'), ('Idosa Feminina Leve', 'Idosa Feminina Leve'), ('Idosa Masculina Pesada', 'Idosa Masculina Pesada'), ('Jovem Feminina Leve', 'Jovem Feminina Leve'), ('Idosa Masculina Leve', 'Idosa Masculina Leve'), ('Meia Idade Feminina', 'Meia Idade Feminina'), ('Adulta Feminina Leve', 'Adulta Feminina Leve'), ('Adulta Masculina Leve', 'Adulta Masculina Leve'), ('Adolescente Feminina', 'Adolescente Feminina'), ('Jovem Masculina Leve', 'Jovem Masculina Leve'), ('Adulta Masculina', 'Adulta Masculina'), ('Meia Idade Masculina', 'Meia Idade Masculina'), ('Jovem Feminina', 'Jovem Feminina'), ('Idosa Feminina Pesada', 'Idosa Feminina Pesada')], max_length=2500),
        ),
    ]