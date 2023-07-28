# Generated by Django 4.2.3 on 2023-07-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vox', '0028_alter_dubladore_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubladore',
            name='categoria',
            field=models.CharField(blank=True, choices=[('Adolescente Feminina', 'Adolescente Feminina'), ('Meia Idade Masculina', 'Meia Idade Masculina'), ('Adulta Masculina Leve', 'Adulta Masculina Leve'), ('Jovem Feminina Pesada', 'Jovem Feminina Pesada'), ('Idosa Feminina Pesada', 'Idosa Feminina Pesada'), ('Adulta Feminina', 'Adulta Feminina'), ('Idosa Feminina', 'Idosa Feminina'), ('Jovem Masculina Leve', 'Jovem Masculina Leve'), ('Infantil Feminina', 'Infantil Feminina'), ('Jovem Masculina', 'Jovem Masculina'), ('Idosa Masculina Leve', 'Idosa Masculina Leve'), ('Idosa Masculina Pesada', 'Idosa Masculina Pesada'), ('Adolescente Masculina', 'Adolescente Masculina'), ('Idosa Masculina', 'Idosa Masculina'), ('Jovem Feminina', 'Jovem Feminina'), ('Adulta Feminina Pesada', 'Adulta Feminina Pesada'), ('Jovem Feminina Leve', 'Jovem Feminina Leve'), ('Adulta Masculina Pesada', 'Adulta Masculina Pesada'), ('Meia Idade Feminina', 'Meia Idade Feminina'), ('Jovem Masculina Pesada', 'Jovem Masculina Pesada'), ('Adulta Feminina Leve', 'Adulta Feminina Leve'), ('Idosa Feminina Leve', 'Idosa Feminina Leve'), ('Adulta Masculina', 'Adulta Masculina'), ('Infantil Masculina', 'Infantil Masculina')], max_length=2500),
        ),
    ]
