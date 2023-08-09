# Generated by Django 4.2.3 on 2023-07-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vox', '0024_alter_dubladore_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubladore',
            name='categoria',
            field=models.CharField(blank=True, choices=[('Idosa Feminina Leve', 'Idosa Feminina Leve'), ('Adulta Masculina Pesada', 'Adulta Masculina Pesada'), ('Adulta Feminina', 'Adulta Feminina'), ('Idosa Masculina Leve', 'Idosa Masculina Leve'), ('Infantil Feminina', 'Infantil Feminina'), ('Jovem Masculina Pesada', 'Jovem Masculina Pesada'), ('Adolescente Masculina', 'Adolescente Masculina'), ('Meia Idade Masculina', 'Meia Idade Masculina'), ('Jovem Feminina', 'Jovem Feminina'), ('Idosa Masculina Pesada', 'Idosa Masculina Pesada'), ('Idosa Feminina Pesada', 'Idosa Feminina Pesada'), ('Adulta Feminina Leve', 'Adulta Feminina Leve'), ('Infantil Masculina', 'Infantil Masculina'), ('Adulta Feminina Pesada', 'Adulta Feminina Pesada'), ('Adulta Masculina', 'Adulta Masculina'), ('Idosa Masculina', 'Idosa Masculina'), ('Adolescente Feminina', 'Adolescente Feminina'), ('Jovem Masculina Leve', 'Jovem Masculina Leve'), ('Idosa Feminina', 'Idosa Feminina'), ('Jovem Feminina Leve', 'Jovem Feminina Leve'), ('Meia Idade Feminina', 'Meia Idade Feminina'), ('Jovem Masculina', 'Jovem Masculina'), ('Adulta Masculina Leve', 'Adulta Masculina Leve'), ('Jovem Feminina Pesada', 'Jovem Feminina Pesada')], max_length=2500),
        ),
    ]