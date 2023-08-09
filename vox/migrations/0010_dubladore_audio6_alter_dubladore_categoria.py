# Generated by Django 4.2.2 on 2023-06-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vox', '0009_delete_caracteristica_alter_dubladore_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dubladore',
            name='audio6',
            field=models.FileField(blank=True, upload_to='music/'),
        ),
        migrations.AlterField(
            model_name='dubladore',
            name='categoria',
            field=models.CharField(choices=[('Meia Idade Masculina', 'Meia Idade Masculina'), ('Jovem Feminina Pesada', 'Jovem Feminina Pesada'), ('Adolescente Feminina', 'Adolescente Feminina'), ('Idosa Feminina Leve', 'Idosa Feminina Leve'), ('Idosa Feminina', 'Idosa Feminina'), ('Jovem Masculina Leve', 'Jovem Masculina Leve'), ('Adulta Masculina Pesada', 'Adulta Masculina Pesada'), ('Jovem Masculina Pesada', 'Jovem Masculina Pesada'), ('Meia Idade Feminina', 'Meia Idade Feminina'), ('Adulta Masculina', 'Adulta Masculina'), ('Idosa Masculina', 'Idosa Masculina'), ('Adolescente Masculina', 'Adolescente Masculina'), ('Jovem Feminina', 'Jovem Feminina'), ('Idosa Masculina Leve', 'Idosa Masculina Leve'), ('Infantil Feminina', 'Infantil Feminina'), ('Idosa Feminina Pesada', 'Idosa Feminina Pesada'), ('Adulta Feminina Pesada', 'Adulta Feminina Pesada'), ('Idosa Masculina Pesada', 'Idosa Masculina Pesada'), ('Jovem Masculina', 'Jovem Masculina'), ('Adulta Feminina', 'Adulta Feminina'), ('Adulta Feminina Leve', 'Adulta Feminina Leve'), ('Jovem Feminina Leve', 'Jovem Feminina Leve'), ('Infantil Masculina', 'Infantil Masculina'), ('Adulta Masculina Leve', 'Adulta Masculina Leve')], max_length=2500),
        ),
    ]