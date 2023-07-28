# Generated by Django 4.2.3 on 2023-07-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vox', '0025_alter_dubladore_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubladore',
            name='categoria',
            field=models.CharField(blank=True, choices=[('Idosa Masculina', 'Idosa Masculina'), ('Idosa Masculina Leve', 'Idosa Masculina Leve'), ('Idosa Masculina Pesada', 'Idosa Masculina Pesada'), ('Adulta Feminina', 'Adulta Feminina'), ('Infantil Masculina', 'Infantil Masculina'), ('Idosa Feminina Pesada', 'Idosa Feminina Pesada'), ('Infantil Feminina', 'Infantil Feminina'), ('Adulta Feminina Pesada', 'Adulta Feminina Pesada'), ('Meia Idade Feminina', 'Meia Idade Feminina'), ('Idosa Feminina Leve', 'Idosa Feminina Leve'), ('Adulta Masculina Pesada', 'Adulta Masculina Pesada'), ('Jovem Masculina Pesada', 'Jovem Masculina Pesada'), ('Adulta Masculina Leve', 'Adulta Masculina Leve'), ('Adulta Feminina Leve', 'Adulta Feminina Leve'), ('Jovem Masculina Leve', 'Jovem Masculina Leve'), ('Adolescente Masculina', 'Adolescente Masculina'), ('Jovem Feminina Pesada', 'Jovem Feminina Pesada'), ('Jovem Masculina', 'Jovem Masculina'), ('Meia Idade Masculina', 'Meia Idade Masculina'), ('Adulta Masculina', 'Adulta Masculina'), ('Jovem Feminina Leve', 'Jovem Feminina Leve'), ('Adolescente Feminina', 'Adolescente Feminina'), ('Jovem Feminina', 'Jovem Feminina'), ('Idosa Feminina', 'Idosa Feminina')], max_length=2500),
        ),
    ]
