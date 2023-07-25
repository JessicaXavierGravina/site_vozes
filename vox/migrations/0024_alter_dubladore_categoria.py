# Generated by Django 4.2.3 on 2023-07-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vox', '0023_alter_dubladore_categoria_alter_dubladore_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubladore',
            name='categoria',
            field=models.CharField(blank=True, choices=[('Adulta Feminina Pesada', 'Adulta Feminina Pesada'), ('Idosa Masculina', 'Idosa Masculina'), ('Jovem Feminina Pesada', 'Jovem Feminina Pesada'), ('Idosa Masculina Leve', 'Idosa Masculina Leve'), ('Jovem Masculina', 'Jovem Masculina'), ('Adolescente Masculina', 'Adolescente Masculina'), ('Jovem Feminina', 'Jovem Feminina'), ('Idosa Feminina Pesada', 'Idosa Feminina Pesada'), ('Adulta Masculina', 'Adulta Masculina'), ('Jovem Masculina Pesada', 'Jovem Masculina Pesada'), ('Adulta Masculina Leve', 'Adulta Masculina Leve'), ('Infantil Masculina', 'Infantil Masculina'), ('Idosa Feminina', 'Idosa Feminina'), ('Idosa Feminina Leve', 'Idosa Feminina Leve'), ('Meia Idade Feminina', 'Meia Idade Feminina'), ('Meia Idade Masculina', 'Meia Idade Masculina'), ('Adulta Masculina Pesada', 'Adulta Masculina Pesada'), ('Jovem Masculina Leve', 'Jovem Masculina Leve'), ('Adulta Feminina', 'Adulta Feminina'), ('Idosa Masculina Pesada', 'Idosa Masculina Pesada'), ('Adulta Feminina Leve', 'Adulta Feminina Leve'), ('Infantil Feminina', 'Infantil Feminina'), ('Adolescente Feminina', 'Adolescente Feminina'), ('Jovem Feminina Leve', 'Jovem Feminina Leve')], max_length=2500),
        ),
    ]
