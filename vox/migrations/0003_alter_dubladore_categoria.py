# Generated by Django 4.2.2 on 2023-06-20 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vox', '0002_dubladore_audio2_dubladore_audio3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubladore',
            name='categoria',
            field=models.CharField(choices=[('JOVEM_FEMININA_LEVE', 'Jovem Feminina Leve'), ('ADULTA_FEMININA_PESADA', 'Adulta Feminina Pesada'), ('ADULTA_MASCULINA_LEVE', 'Adulta Masculina Leve'), ('IDOSA_MASCULINA_PESADA', 'Idosa Masculina Pesada'), ('ADULTA_MASCULINA_PESADA', 'Adulta Masculina Pesada'), ('MEIA_IDADE_FEMININA', 'Meia Idade Feminina'), ('IDOSA_FEMININA', 'Idosa Feminina'), ('ADULTA_FEMININA_LEVE', 'Adulta Feminina Leve'), ('IDOSA_FEMININA_LEVE', 'Idosa Feminina Leve'), ('JOVEM_MASCULINA_LEVE', 'Jovem Masculina Leve'), ('ADULTA_FEMININA', 'Adulta Feminina'), ('JOVEM_FEMININA', 'Jovem Feminina'), ('JOVEM_MASCULINA_PESADA', 'Jovem Masculina Pesada'), ('INFANTIL_FEMININA', 'Infantil Feminina'), ('INFANTIL_MASCULINA', 'Infantil Masculina'), ('JOVEM_MASCULINA', 'Jovem Masculina'), ('IDOSA_FEMININA_PESADA', 'Idosa Feminina Pesada'), ('JOVEM_FEMININA_PESADA', 'Jovem Feminina Pesada'), ('ADOLESCENTE_FEMININA', 'Adolescente Feminina'), ('ADOLESCENTE_MASCULINA', 'Adolescente Masculina'), ('MEIA_IDADE_MASCULINA', 'Meia Idade Masculina'), ('ADULTA_MASCULINA', 'Adulta Masculina'), ('IDOSA_MASCULINA', 'Idosa Masculina'), ('IDOSA_MASCULINA_LEVE', 'Idosa Masculina Leve')], max_length=2500),
        ),
    ]