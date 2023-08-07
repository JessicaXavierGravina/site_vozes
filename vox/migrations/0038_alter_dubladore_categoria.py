# Generated by Django 4.2.3 on 2023-08-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vox', '0037_alter_dubladore_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubladore',
            name='categoria',
            field=models.CharField(blank=True, choices=[('AdultaMasculina', 'Adulta Masculina'), ('IdosaFeminina', 'Idosa Feminina'), ('AdultaFeminina', 'Adulta Feminina'), ('MeiaIdadeFeminina', 'Meia Idade Feminina'), ('JovemMasculina', 'Jovem Masculina'), ('JovemFemininaPesada', 'Jovem Feminina Pesada'), ('AdultaMasculinaPesada', 'Adulta Masculina Pesada'), ('IdosaFemininaPesada', 'Idosa Feminina Pesada'), ('JovemMasculinaPesada', 'Jovem Masculina Pesada'), ('AdultaMasculinaLeve', 'Adulta Masculina Leve'), ('AdolescenteMasculina', 'Adolescente Masculina'), ('JovemFeminina', 'Jovem Feminina'), ('InfantilMasculina', 'Infantil Masculina'), ('IdosaMasculinaPesada', 'Idosa Masculina Pesada'), ('IdosaMasculina', 'Idosa Masculina'), ('InfantilFeminina', 'Infantil Feminina'), ('JovemMasculinaLeve', 'Jovem Masculina Leve'), ('AdultaFemininaPesada', 'Adulta Feminina Pesada'), ('IdosaMasculinaLeve', 'Idosa Masculina Leve'), ('MeiaIdadeMasculina', 'Meia Idade Masculina'), ('AdultaFemininaLeve', 'Adulta Feminina Leve'), ('AdolescenteFeminina', 'Adolescente Feminina'), ('IdosaFemininaLeve', 'Idosa Feminina Leve'), ('JovemFemininaLeve', 'Jovem Feminina Leve')], max_length=2500),
        ),
    ]