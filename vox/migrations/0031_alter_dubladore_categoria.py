# Generated by Django 4.2.3 on 2023-07-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vox', '0030_alter_dubladore_categoria_alter_dubladore_etnia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubladore',
            name='categoria',
            field=models.CharField(blank=True, choices=[('IdosaFemininaPesada', 'Idosa Feminina Pesada'), ('AdolescenteMasculina', 'Adolescente Masculina'), ('JovemMasculina', 'Jovem Masculina'), ('AdolescenteFeminina', 'Adolescente Feminina'), ('JovemMasculinaLeve', 'Jovem Masculina Leve'), ('IdosaMasculinaPesada', 'Idosa Masculina Pesada'), ('InfantilFeminina', 'Infantil Feminina'), ('InfantilMasculina', 'Infantil Masculina'), ('AdultaFeminina', 'Adulta Feminina'), ('JovemFeminina', 'Jovem Feminina'), ('MeiaIdadeMasculina', 'Meia Idade Masculina'), ('IdosaMasculinaLeve', 'Idosa Masculina Leve'), ('IdosaFeminina', 'Idosa Feminina'), ('IdosaMasculina', 'Idosa Masculina'), ('IdosaFemininaLeve', 'Idosa Feminina Leve'), ('AdultaMasculina', 'Adulta Masculina'), ('MeiaIdadeFeminina', 'Meia Idade Feminina'), ('JovemMasculinaPesada', 'Jovem Masculina Pesada'), ('AdultaFemininaLeve', 'Adulta Feminina Leve'), ('AdultaMasculinaPesada', 'Adulta Masculina Pesada'), ('AdultaMasculinaLeve', 'Adulta Masculina Leve'), ('JovemFemininaPesada', 'Jovem Feminina Pesada'), ('AdultaFemininaPesada', 'Adulta Feminina Pesada'), ('JovemFemininaLeve', 'Jovem Feminina Leve')], max_length=2500),
        ),
    ]